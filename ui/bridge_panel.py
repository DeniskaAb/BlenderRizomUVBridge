# <pep8-80 compliant>

"""RizomUV Bridge user-interface."""

import os
import tempfile

import bpy

import rizomuv_bridge.ma_utils.utils as mutil


class RizomUVBridgePanel(bpy.types.Panel):
    """Main UI panel"""

    bl_idname = "PANEL_PT_RizomUVBridge"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "RizomUV"
    bl_context = "objectmode"
    bl_label = "RizomUV Bridge"

    def draw(self, context):
        """Draw the UI."""

        temp_file = tempfile.gettempdir() + os.sep + "rizom_temp.fbx"

        props = bpy.context.preferences.addons["rizomuv_bridge"].preferences

        layout = self.layout

        # Import/Export
        box = layout.box()
        row = box.row(align=True)
        row.label(text="UV Operations:", icon='UV_DATA')

        row = box.row(align=True)
        row.scale_y = 1.25
        if not os.path.exists(temp_file) or props.auto_uv is True:
            row.enabled = False
        row.operator("ruv.rizom_edit", text="Edit", icon='FILE_CACHE')

        row = box.row(align=True)
        row.scale_y = 1.25
        if props.auto_uv is True:
            export = "Export (Auto UV)"
        else:
            export = "Export"
        row.operator("ruv.rizom_export", text=export, icon='EXPORT')
        row.operator("ruv.rizom_import", text="Import", icon='IMPORT')

        #row = box.row(align=True)
        #row.scale_y = 1.25
        #if not mutil.get_meshes(False):
            #row.enabled = False
        #row.operator("ruv.rizom_import", text="Import", icon='IMPORT')

        #--------------------------------------#
        #--------------------------------------#

        # Export Settings
        box = layout.box()
        row = box.row(align=True)
        row.label(text="Export Settings:", icon='EXPORT')

        split = box.split()
        col = split.column()
        col.scale_y = 1.25
        if props.script_run != 'NO_SCRIPT':
            col.enabled = False
            props.preserve_uv = False
        col.prop(props, "preserve_uv")

        col = split.column()
        col.scale_y = 1.25
        if props.script_run == 'NO_SCRIPT':
            col.enabled = False
            props.auto_uv = False
        col.prop(props, "auto_uv")

        row = box.row(align=True)
        row.scale_y = 1.25
        row.prop(props, "script_run")

        if props.script_run == 'SHARP_EDGES':

            # Sharp edge value
            row = box.row(align=True)
            row.scale_y = 1.25
            row.prop(props, "sharp_value")

            # Link holes and cut handles options
            row = box.row(align=True)
            row.scale_y = 1.25
            row.prop(props, "link_holes", toggle=True)
            row.prop(props, "cut_handles", toggle=True)


        elif props.script_run == 'MOSAIC':

            # Segments value
            row = box.row(align=True)
            row.scale_y = 1.25
            row.prop(props, "mosaic_value")

            # Link holes and cut handles options
            row = box.row(align=True)
            row.scale_y = 1.25
            row.prop(props, "link_holes", toggle=True)
            row.prop(props, "cut_handles", toggle=True)

        elif props.script_run == 'PELT':

            # Link holes and cut handles options
            row = box.row(align=True)
            row.scale_y = 1.25
            row.prop(props, "link_holes", toggle=True)
            row.prop(props, "cut_handles", toggle=True)

        elif props.script_run == 'BOX':

            # Link holes and cut handles options
            row = box.row(align=True)
            row.scale_y = 1.25
            row.prop(props, "link_holes", toggle=True)
            row.prop(props, "cut_handles", toggle=True)

        if props.script_run != 'NO_SCRIPT':
            props.preserve_uv = False

        #--------------------------------------#
        #--------------------------------------#

        # Import Settings
        box = layout.box()
        row = box.row(align=True)
        row.label(text="Import Settings:", icon='IMPORT')

        row = box.row(align=True)
        row.scale_y = 1.25
        row.prop(props, "seams")
        row.prop(props, "reveal_hidden")

        #--------------------------------------#
        #--------------------------------------#

        box = layout.box()
        row = box.row(align=True)
        row.label(text="Reset Settings:", icon='PREFERENCES')

        row = box.row(align=True)
        row.scale_y = 1.25
        row.operator("ruv.rizomuv_config_reset",
                     text="RizomUV Settings", icon='LOOP_BACK')
        row.operator("ruv.bridge_config_reset",
                     text="Bridge Settings", icon='LOOP_BACK')


class RizomUVSettingsPanel(bpy.types.Panel):
    """Rizom settings panel"""

    bl_idname = "PANEL_PT_RizomUVSettings"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "RizomUV"
    bl_context = "objectmode"
    bl_label = "RizomUV Settings"

    def draw(self, context):
        """Draw the UI."""

        props = bpy.context.preferences.addons["rizomuv_bridge"].preferences

        layout = self.layout
        box = layout.box()

        row = box.row(align=True)
        row.label(text="Viewport:", icon='VIEW3D')

        row = box.row(align=True)
        row.scale_y = 1.25
        row.prop(props, "image_path")

        #--------------------------------------#
        #--------------------------------------#

        layout = self.layout
        box = layout.box()

        row = box.row(align=True)
        row.label(text="Layout:", icon='GROUP_UVS')

        row = box.row(align=True)
        row.scale_y = 1.25
        row.prop(props, "shell_pad")
        row.prop(props, "map_res")

        #--------------------------------------#
        #--------------------------------------#

        box = layout.box()
        row = box.row(align=True)
        row.label(text="Packing:", icon='PACKAGE')
        row = box.row(align=True)
        row.scale_y = 1.25
        row.prop(props, "pack_qual")
        row.prop(props, "mutations")
        row = box.row(align=True)
        row.scale_y = 1.25
        row.prop(props, "init_orient")
        row.prop(props, "orient_step")

        #--------------------------------------#
        #--------------------------------------#
