# <pep8-80 compliant>

"""Operations concerning all types of file transfer."""

import os
import subprocess
import tempfile

import bpy

import rizomuv_bridge.ma_utils.lua_functions as lua
import rizomuv_bridge.ma_utils.utils as mutil

TEMP_PATH = tempfile.gettempdir() + os.sep + "rizom_temp.fbx"


class ExportToRizom(bpy.types.Operator):
    """Send the UVs to RizomUV."""

    bl_description = "Export objects to a temp file and open it in RizomUV"
    bl_idname = "ruv.rizom_export"
    bl_label = "Export (RizomUV)"
    bl_options = {'REGISTER', 'INTERNAL'}

    @classmethod
    def poll(cls, context):
        """Check context is correct to run the operator."""

        return context.active_object is not None, os.path.isfile(TEMP_PATH)

    def uv_map_checks(self, objs):
        """Check UV maps are valid for use in Rizom.

        Args:
            objs (list): A list of bpy_types.Objects to run through UV checks.

        Returns:
            Boolean: Returns True if checks are passed, False if not.

        """

        valid = False

        # Check map names do not contain periods
        uv_maps = objs[0].data.uv_layers

        for uvmap in uv_maps:
            name = uvmap.name
            check = "." in name
            if check:
                self.report(
                    {'ERROR'},
                    "RizomUV Bridge: Remove any periods"
                    + " from your UV Map name: " + name)
                return valid

        # Check each objects UV maps are the same
        check_names = [uvmap.name for uvmap in objs[0].data.uv_layers]
        for obj in objs:
            names = [uvmap.name for uvmap in obj.data.uv_layers]

            # Check UV Maps exist
            if not names:
                self.report({'ERROR'}, "RizomUV Bridge: The selected objects"
                            + " have no UV maps assigned.")
                return valid

            if names == check_names:
                continue
            else:
                self.report({'ERROR'}, "RizomUV Bridge: "
                            + '"' + obj.name + '"'
                            + " UV maps do not match those of "
                            + '"' + objs[0].name + '"')
                return valid

        valid = True

        return valid

    def export_file(self, context):
        """Export the file."""

        props = bpy.context.preferences.addons["rizomuv_bridge"].preferences

        act_obj = bpy.context.active_object
        sel_objs = mutil.get_meshes(True)
        out_objs = []

        bpy.ops.ed.undo_push()
        if not self.uv_map_checks(sel_objs):
            return {'CANCELLED'}

        for obj in sel_objs:
            new_obj = obj.copy()
            new_obj.name = obj.name + "_rizom"
            bpy.context.scene.collection.objects.link(new_obj)
            out_objs.append(new_obj)

        bpy.ops.object.select_all(action='DESELECT')

        # Clear any modifiers and reset active UV index ready for export
        for obj in out_objs:
            bpy.data.objects[obj.name].select_set(True)
            obj.modifiers.clear()
            obj.data.uv_layers.active_index = 0

        bpy.ops.export_scene.fbx(
            filepath=TEMP_PATH, use_selection=True, global_scale=1.0,
            object_types={'MESH'}, use_mesh_edges=False, bake_anim=False,
            axis_forward='-Z', axis_up='Y'
        )

        mutil.delete_meshes(out_objs)

        for obj in sel_objs:
            bpy.data.objects[obj.name].select_set(True)

        context.view_layer.objects.active = act_obj

        script = lua.write_script()
        prefs = bpy.context.preferences.addons["rizomuv_bridge"].preferences
        exe = prefs.rizomuv_path

        try:
            process = subprocess.Popen([exe, '-cfi' + script])
        except FileNotFoundError:
            self.report(
                {'ERROR'},
                "RizomUV Bridge: Check your path to RizomUV is set correctly")
            return {'CANCELLED'}

        if props.auto_uv:
            process.communicate()

        if not props.auto_uv:
            self.report({'INFO'}, "RizomUV Bridge: "
                        + str(len(sel_objs)) + " object(s) exported")

        return None

    def execute(self, context):
        """Operator execution code."""

        local_view = context.space_data.local_view
        props = bpy.context.preferences.addons["rizomuv_bridge"].preferences

        if local_view:
            bpy.ops.view3d.localview(frame_selected=False)

        self.export_file(context)

        if props.auto_uv:
            try:
                bpy.ops.ruv.rizom_import()
                self.report({'INFO'}, "RizomUV Bridge: UV maps transferred")
            except RuntimeError:
                pass

        if local_view:
            bpy.ops.view3d.localview(frame_selected=False)

        return {'FINISHED'}


class ImportFromRizom(bpy.types.Operator):
    """Get the UVs from RizomUV."""

    bl_description = "Import UVs from RizomUV"
    bl_idname = "ruv.rizom_import"
    bl_label = "Import (RizomUV)"
    bl_options = {'REGISTER', 'UNDO', 'INTERNAL'}

    @classmethod
    def poll(cls, context):
        """Check context is correct to run the operator."""

        return len(mutil.get_meshes(False)) > 0 and\
            os.path.isfile(TEMP_PATH)

    @staticmethod
    def mark_seams_and_sharp(_mark_seams, _mark_sharp):
        """Mark seams and sharp edges on import."""

        bpy.ops.object.mode_set(mode='EDIT')
        vert, face, edge = mutil.sel_mode(False, True, False)
        bpy.ops.mesh.select_all(action='SELECT')
        bpy.ops.mesh.mark_sharp(clear=True)
        bpy.ops.mesh.select_all(action='DESELECT')
        bpy.ops.uv.seams_from_islands(mark_seams=_mark_seams, mark_sharp=_mark_sharp)
        mutil.sel_mode(vert, face, edge)
        bpy.ops.object.mode_set(mode='OBJECT')

    @staticmethod
    def valid_act_obj(context, uv_objs, show_obj_list):
        """Trys to set the active object to one that is not hidden,
        defaults to arbitrary object if this is not possible.

        Args:
            uv_objs (list): A list of bpy_types.Objects marked for update.
            show_obj_list (list): A list bpy_types.Objects marked as hidden.

        Returns:
            bpy_types.Object: Active object.

        """

        valid_objs = [obj for obj in uv_objs if obj not in show_obj_list]

        try:
            context.view_layer.objects.active = valid_objs[0]
        except IndexError:
            context.view_layer.objects.active = uv_objs[0]

        act_obj = bpy.context.active_object

        return act_obj

    @staticmethod
    def uv_transfer_loop(context, uv_objs, act_obj):
        """Loop through each UV map/object and transfer them."""

        for obj in uv_objs:
            rizom_obj = bpy.data.objects[obj.name + "_rizom"]
            bpy.data.objects[obj.name].select_set(True)
            context.view_layer.objects.active = rizom_obj

            og_index = obj.data.uv_layers.active_index
            uvmap_list = act_obj.data.uv_layers

            # Each UV map in the obj
            for uvmap in uvmap_list:
                obj.data.uv_layers.active = obj.data.uv_layers[uvmap.name]
                rizom_obj.data.uv_layers.active\
                    = rizom_obj.data.uv_layers[uvmap.name]

                bpy.ops.object.join_uvs()

            # Reset for next iteration
            obj.data.uv_layers.active_index = og_index
            bpy.ops.object.select_all(action='DESELECT')

    def import_file(self, context):
        """Import the file, transfer the UVs and delete imported objects."""

        bpy.ops.ed.undo_push()
        bpy.ops.import_scene.fbx(filepath=TEMP_PATH)

        rizom_objs = [
            obj for obj in bpy.data.objects if obj.name.endswith("_rizom")]

        # Remove rizom suffix and compare all objs in scene for matching name
        uv_objs = [bpy.data.objects[(obj.name.replace("_rizom", ""))] for obj
                   in rizom_objs if (obj.name.replace("_rizom", ""))
                   in bpy.data.objects]

        # Reveal objs and collections, objs need to be visible for UV join
        col_hide_list, col_exclude_list = mutil.collections_reveal(uv_objs)
        show_obj_list = mutil.objects_reveal(uv_objs)

        if not uv_objs:
            self.report(
                {'ERROR'},
                "RizomUV Bridge: There are no matching objects in the scene")
            bpy.ops.ed.undo()
            return {'CANCELLED'}

        bpy.ops.object.select_all(action='DESELECT')

        act_obj = self.valid_act_obj(context, uv_objs, show_obj_list)

        # Updated OBJ/UV Map count, just for outputting to the user later
        report_count = (len(uv_objs), len(act_obj.data.uv_layers))

        self.uv_transfer_loop(context, uv_objs, act_obj)

        mutil.delete_meshes(rizom_objs)

        for obj in uv_objs:
            bpy.data.objects[obj.name].select_set(True)

        context.view_layer.objects.active = act_obj

        self.report({'INFO'}, "RizomUV Bridge: " + str(report_count[1])
                    + " UV map(s) updated" + " on " + str(report_count[0])
                    + " object(s)")

        return col_hide_list, col_exclude_list, show_obj_list

    def execute(self, context):
        """Operator execution code."""

        local_view = context.space_data.local_view
        props = bpy.context.preferences.addons["rizomuv_bridge"].preferences

        if local_view:
            bpy.ops.view3d.localview(frame_selected=False)

        try:
            col_hide_list, col_exclude_list, show_obj_list = self.import_file(
                context)
        except ValueError:
            pass
        except KeyError:
            self.report({'ERROR'}, "RizomUV Bridge: No matching items found")
            bpy.ops.ed.undo()
            return {'CANCELLED'}

        if props.seams or prop.sharp:
            try:
                self.mark_seams_and_sharp(props.seams, prop.sharp)
            except RuntimeError:
                pass

        if not props.reveal_hidden:
            try:
                mutil.collections_hide(col_hide_list, col_exclude_list)
                mutil.objects_hide(show_obj_list)
            except UnboundLocalError:
                pass

        if local_view:
            bpy.ops.view3d.localview(frame_selected=False)

        return {'FINISHED'}


class EditInRizom(bpy.types.Operator):
    """Open the last file in Rizom (No export)."""

    bl_description = "Open the most recent file in Rizom (no export)"
    bl_idname = "ruv.rizom_edit"
    bl_label = "Edit (RizomUV)"
    bl_options = {'REGISTER', 'INTERNAL'}

    @staticmethod
    def open_file():
        """Open most recent file in RizomUV"""
        script = lua.write_script_edit()

        prefs = bpy.context.preferences.addons["rizomuv_bridge"].preferences

        subprocess.Popen([prefs.rizomuv_path, TEMP_PATH, '-cfi' + script])

    def execute(self, context):
        """Operator execution code."""

        self.open_file()
        self.report(
            {'INFO'}, "RizomUV Bridge: Loading your most recent file")

        return {'FINISHED'}
