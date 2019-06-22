# <pep8-80 compliant>

"""Operations concerning all types of file transfer."""

import os
import subprocess
import tempfile
import bpy
import rizomuv_bridge.ma_utils.utils as mutil
import rizomuv_bridge.ma_utils.lua_functions as lua

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

        return context.active_object is not None

    def uv_map_checks(self, objs):
        """Check UV maps are valid for use in Rizom"""

        valid = False

        for obj in objs:
            uv_maps = obj.data.uv_layers

            for uvmap in uv_maps:
                name = uvmap.name
                check = name.isalnum()
                if not check:
                    self.report(
                        {'ERROR'},
                        "RizomUV Bridge: Invalid UV Map name: " + name)
                    bpy.ops.ed.undo()
                    return valid

        count_check = len(objs[0].data.uv_layers)

        for obj in objs[1:]:
            uv_maps = len(obj.data.uv_layers)
            if uv_maps != count_check:
                self.report({'ERROR'}, "RizomUV Bridge: "
                            + '"' + obj.name + '"'
                            + " UV map count is not equal to that of "
                            + '"' + objs[0].name + '"')
                bpy.ops.ed.undo()
                return valid

        check_names = [uvmap.name for uvmap in objs[0].data.uv_layers]
        for obj in objs:
            names = [uvmap.name for uvmap in obj.data.uv_layers]
            if names == check_names:
                continue
            else:
                self.report({'ERROR'}, "RizomUV Bridge: "
                            + '"' + obj.name + '"'
                            + " has UV maps not present on "
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

        for obj in out_objs:
            bpy.data.objects[obj.name].select_set(True)
            obj.modifiers.clear()
            obj.data.uv_layers.active_index = 0

        bpy.ops.export_scene.fbx(
            filepath=TEMP_PATH, use_selection=True, global_scale=1.0,
            object_types={'MESH'}, use_mesh_edges=False, bake_anim=False,
            axis_forward='-Z', axis_up='Y'
        )

        bpy.ops.object.delete(use_global=False, confirm=False)

        for obj in sel_objs:
            bpy.data.objects[obj.name].select_set(True)

        context.view_layer.objects.active = act_obj

        script = lua.write_script()
        prefs = bpy.context.preferences.addons["rizomuv_bridge"].preferences
        exe = prefs.rizomuv_path

        process = subprocess.Popen([exe, TEMP_PATH, '-cfi' + script])
        if props.auto_uv:
            process.communicate()

        if not props.auto_uv:
            self.report({'INFO'}, "RizomUV Bridge: "
                        + str(len(sel_objs)) + " object(s) exported")

    def execute(self, context):
        """Operator execution code."""

        local_view = context.space_data.local_view
        props = bpy.context.preferences.addons["rizomuv_bridge"].preferences

        if local_view:
            bpy.ops.view3d.localview(frame_selected=False)

        self.export_file(context)

        if props.auto_uv:
            bpy.ops.ruv.rizom_import()
            self.report({'INFO'}, "RizomUV Bridge: UV maps transferred")

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

        return mutil.get_meshes(False) is not None

    @staticmethod
    def mark_seams():
        """Mark seams as sharp edges on import"""

        bpy.ops.object.mode_set(mode='EDIT')
        vert, face, edge = mutil.sel_mode(False, True, False)
        bpy.ops.mesh.select_all(action='SELECT')
        bpy.ops.mesh.mark_sharp(clear=True)
        bpy.ops.mesh.select_all(action='DESELECT')
        bpy.ops.uv.seams_from_islands(mark_seams=True, mark_sharp=True)
        mutil.sel_mode(vert, face, edge)
        bpy.ops.object.mode_set(mode='OBJECT')

    @staticmethod
    def collections_reveal():
        """Reveal hidden collections.

        Returns:
            list: List of collections that have been revealed.

        """

        collections = bpy.context.view_layer.layer_collection.children

        col_list = [col for col in collections if col.hide_viewport is True]

        for col in col_list:
            col.hide_viewport = False

        return col_list

    @staticmethod
    def collections_hide(col_list):
        """Hide collections in list"""

        for col in col_list:
            col.hide_viewport = True

    def import_file(self, context):
        """Import the file, transfer the UVs and delete imported objects."""

        bpy.ops.ed.undo_push()
        bpy.ops.import_scene.fbx(filepath=TEMP_PATH)

        scene_objs = bpy.data.objects
        rizom_objs = [obj for obj in scene_objs if obj.name.endswith("_rizom")]

        uv_objs = []
        for obj in rizom_objs:
            name = obj.name.replace("_rizom", "")
            try:
                uv_obj = bpy.data.objects[name]
            except KeyError:
                continue
            uv_objs.append(uv_obj)

        if not uv_objs:
            self.report(
                {'ERROR'},
                "RizomUV Bridge: There are no matching objects in the scene")
            bpy.ops.ed.undo()
            return {'CANCELLED'}

        bpy.ops.object.select_all(action='DESELECT')

        col_list = self.collections_reveal()

        context.view_layer.objects.active = uv_objs[0]
        act_obj = bpy.context.active_object

        uv_obj_count = len(uv_objs)
        uv_map_count = len(act_obj.data.uv_layers)

        for obj in uv_objs:
            rizom_obj = bpy.data.objects[obj.name + "_rizom"]
            bpy.data.objects[obj.name].select_set(True)
            context.view_layer.objects.active = rizom_obj

            og_index = obj.data.uv_layers.active_index
            uvmap_list = act_obj.data.uv_layers

            for uvmap in uvmap_list:
                name = uvmap.name
                obj.data.uv_layers.active = obj.data.uv_layers[name]
                rizom_obj.data.uv_layers.active\
                    = rizom_obj.data.uv_layers[name]

                bpy.ops.object.join_uvs()

            obj.data.uv_layers.active_index = og_index
            bpy.ops.object.select_all(action='DESELECT')

        rizom_objs = [obj for obj in mutil.get_meshes(False)
                      if obj.name.endswith("_rizom")]

        for obj in rizom_objs:
            bpy.data.objects[obj.name].select_set(True)
            bpy.ops.object.delete(use_global=False, confirm=False)

        for obj in uv_objs:
            bpy.data.objects[obj.name].select_set(True)

        context.view_layer.objects.active = act_obj

        self.collections_hide(col_list)

        self.report({'INFO'}, "RizomUV Bridge: " + str(uv_map_count)
                    + " UV map(s) updated" + " on " + str(uv_obj_count)
                    + " object(s)")

    def execute(self, context):
        """Operator execution code."""

        local_view = context.space_data.local_view
        props = bpy.context.preferences.addons["rizomuv_bridge"].preferences

        if local_view:
            bpy.ops.view3d.localview(frame_selected=False)

        try:
            self.import_file(context)
        except KeyError:
            self.report({'ERROR'}, "RizomUV Bridge: Item names do not match")
            bpy.ops.ed.undo()
            return {'CANCELLED'}

        if props.seams:
            self.mark_seams()

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
        exe = prefs.rizomuv_path

        subprocess.Popen([exe, TEMP_PATH, '-cfi' + script])

    def execute(self, context):
        """Operator execution code."""

        self.open_file()
        self.report(
            {'INFO'}, "RizomUV Bridge: Loading your most recent file")

        return {'FINISHED'}
