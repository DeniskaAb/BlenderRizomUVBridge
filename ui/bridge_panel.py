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
        row.operator("ruv.rizom_edit", text="Load Recent File", icon='FILE_CACHE')

        row = box.row(align=True)
        row.scale_y = 1.25
        if props.auto_uv is True:
            export = "Export (Auto UV)"
        else:
            export = "Export"
        row.operator("ruv.rizom_export", text=export, icon='EXPORT')
        row.operator("ruv.rizom_import", text="Import", icon='IMPORT')

        #--------------------------------------#
        #--------------------------------------#

        # Export Settings
        box = layout.box()
        row = box.row(align=True)
        row.label(text="Export Settings:", icon='EXPORT')

        split = box.split()

        col = split.column()
        col.scale_y = 1.25
        if props.script_run in ('NO_SCRIPT', 'FLATTEN'):
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

            # Leaf/Branch/Trunk selections
            row = box.row(align=True)
            row.scale_y = 1.25
            row.prop(props, "leaf", toggle=True)
            row.prop(props, "branch", toggle=True)
            row.prop(props, "trunk", toggle=True)

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

        col = box.column(align=True)
        col.scale_y = 1.25
        col.prop(props, "seams")
        col.prop(props, "sharp")
        col.prop(props, "reveal_hidden")

        #--------------------------------------#
        #--------------------------------------#


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


class RizomUVPreferencesPanel(bpy.types.Panel):
    """Addon preferences panel"""

    bl_idname = "PANEL_PT_RizomUVPreferences"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "RizomUV"
    bl_context = "objectmode"
    bl_label = "Addon Preferences"

    def draw(self, context):
        """Draw the UI."""

        props = bpy.context.preferences.addons["rizomuv_bridge"].preferences

        layout = self.layout
        box = layout.box()

        #--------------------------------------#
        #--------------------------------------#

        row = box.row(align=True)
        row.label(text="Reset Settings:", icon='PREFERENCES')

        row = box.row(align=True)
        row.scale_y = 1.25
        row.operator("ruv.bridge_config_reset",
                     text="Bridge Settings", icon='LOOP_BACK')
        row.operator("ruv.rizomuv_config_reset",
                     text="RizomUV Settings", icon='LOOP_BACK')

        #--------------------------------------#
        #--------------------------------------#

        box = layout.box()
        row = box.row(align=True)
        row.label(text="RizomUV Path:", icon='FILEBROWSER')

        row = box.row()
        row.scale_y = 1.25
        row.prop(props, "rizomuv_path")