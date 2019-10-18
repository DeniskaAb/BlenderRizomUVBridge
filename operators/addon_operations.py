# <pep8-80 compliant>

"""Operations for changing the addon itself."""

import bpy


class ResetBridgeSettings(bpy.types.Operator):
    """Reset bridge addon settings to default values."""

    bl_description = "Reset bridge settings"
    bl_idname = "ruv.bridge_config_reset"
    bl_label = "Reset all Bridge Settings"
    bl_options = {'REGISTER', 'INTERNAL'}

    def execute(self, context):
        """Operator execution code"""

        props = bpy.context.preferences.addons["rizomuv_bridge"].preferences

        preferences = [
            "script_run",
            "auto_uv",
            "seams",
            "sharp_value",
            "cut_handles",
            "link_holes",
            "mosaic_value"
        ]

        for preference in preferences:
            props.property_unset(preference)

        self.report({'INFO'}, "RizomUV Bridge: Bridge settings reset")

        return {'FINISHED'}


class ResetRizomUVSettings(bpy.types.Operator):
    """Reset RizomUV settings to default values."""

    bl_description = "Reset RizomUV settings"
    bl_idname = "ruv.rizomuv_config_reset"
    bl_label = "Reset all RizomUV Settings"
    bl_options = {'REGISTER', 'INTERNAL'}

    def execute(self, context):
        """Operator execution code"""

        props = bpy.context.preferences.addons["rizomuv_bridge"].preferences

        preferences = [
            "shell_pad",
            "map_res",
            "image_path",
            "init_orient",
            "orient_step",
            "mutations",
            "pack_qual"
        ]

        for preference in preferences:
            props.property_unset(preference)

        self.report({'INFO'}, "RizomUV Bridge: RizomUV settings reset")

        return {'FINISHED'}
