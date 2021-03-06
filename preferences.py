# <pep8-80 compliant>

"""Addon user preferences in addon menu"""

import bpy


class RizomUVBridgeAddonPreferences(bpy.types.AddonPreferences):
    """Addon user settings."""

    bl_idname = "rizomuv_bridge"

    rizomuv_path_des = "Path to the RizomUV executable"
    rizomuv_path: bpy.props.StringProperty(
        name="Rizom Path", subtype='FILE_PATH',
        description=rizomuv_path_des,
        default=R"C:\Program Files\Rizom Lab\RizomUV 2019\rizomuv.exe")

    # Export settings
    script_run_des = "Run a LUA script when Rizom launches"
    script_run: bpy.props.EnumProperty(
        name="Script", default='NO_SCRIPT', items=(
            ('NO_SCRIPT', "No Script",
             "Exports current UV layout in its present condition"),
            ('FLATTEN', "Flatten UVs",
             "Flat UV projection"),
            ('PELT', "Autoseams: Pelt",
             "Performs a quick auto unwrap using the pelt algorithm"),
            ('MOSAIC', "Autoseams: Mosaic",
             "Performs a quick auto unwrap using the mosaic algorithm"),
            ('SHARP_EDGES', "Autoseams: Sharp Edges",
             "Performs a quick auto unwrap using the sharp edges algorithm"),
            ('BOX', "Autoseams: Box",
             "Performs a quick auto unwrap using the box algorithm")
        ), description=script_run_des
    )

    auto_uv_des = ("Create an automatic UV map and return to blender"
                   " (Autoseams Scripts)")
    auto_uv: bpy.props.BoolProperty(name="Auto UV", default=False,
                                    description=auto_uv_des)

    # Import settings
    seams_des = ("Creates seams edges from UV"
                 " island boundaries after importing")
    seams: bpy.props.BoolProperty(name="Mark Seams", description=seams_des,
                                  default=True)
    sharp_des = ("Creates sharp edges from UV"
                 " island boundaries after importing")
    sharp: bpy.props.BoolProperty(name="Mark Sharp", description=sharp_des,
                                  default=True)

    reveal_hidden_des = ("Reveal any hidden objects/collections that "
                         "were updated during the import process")
    reveal_hidden: bpy.props.BoolProperty(name="Show Hidden",
                                          description=reveal_hidden_des,
                                          default=True)

    # RizomUV settings
    shell_pad_des = "Pixel padding between each UV island"
    shell_pad: bpy.props.IntProperty(name="Island Padding", default=16, min=0,
                                     subtype='PIXEL', soft_max=32,
                                     description=shell_pad_des)

    map_res_des = "The horizontal resoultion of the texture map"
    map_res: bpy.props.IntProperty(name="Map Resolution", default=2048, min=0,
                                   subtype='PIXEL', description=map_res_des)

    image_path_des = "Texture to be loaded into RizomUV"
    image_path: bpy.props.StringProperty(name="", subtype='FILE_PATH',
                                         default="Texture Image (optional)",
                                         description=image_path_des)

    init_orient_des = "Pre-orient islands by bounding box before packing"
    init_orient: bpy.props.EnumProperty(
        name="", default='1', items=(
            ('0', "No Pre-Orientation",
             "Do not pre-orient islands"),
            ('1', "Horizontal Pre-Orientation",
             "Pre-orient islands horizontally"),
            ('2', "Vertical Pre-Orientation",
             "Pre-orient islands vertically")
        ), description=init_orient_des
    )

    orient_step_des = "Step angle for finding best orientation while packing"
    orient_step: bpy.props.IntProperty(name="Step Angle", default=90,
                                       min=0, max=180, subtype='ANGLE',
                                       description=orient_step_des)

    mutations_des = ("Maximum number of trials to find best packing solution")
    mutations: bpy.props.IntProperty(name="Mutations", default=1,
                                     max=1000, min=0,
                                     description=mutations_des)

    pack_qual_des = "Resolution of the packing algorithm"
    pack_qual: bpy.props.IntProperty(name="Quality", default=200, max=1000,
                                     min=0, description=pack_qual_des)

    sharp_value_des = "Edges at a greater angle will be cut"
    sharp_value: bpy.props.IntProperty(name="Edge Angle", default=70,
                                         max=180, min=0, subtype='ANGLE',
                                         description=sharp_value_des)

    cut_handles_des = "Cut Handles"
    cut_handles: bpy.props.BoolProperty(name="Handles Cutter", default=True,
                                        description=cut_handles_des)

    link_holes_des = "Cut links between holes"
    link_holes: bpy.props.BoolProperty(name="Pipes Cutter", default=True,
                                       description=link_holes_des)

    mosaic_value_des = "Higher number equals more islands but less distortion"
    mosaic_value: bpy.props.FloatProperty(name="Segments", default=0.5,
                                          max=0.99, min=0.0,
                                          description=mosaic_value_des)

    leaf_des = "Cut leaf sections"
    leaf: bpy.props.BoolProperty(name="Leaf", default=False,
                                 description=leaf_des)

    branch_des = "Cut branch sections"
    branch: bpy.props.BoolProperty(name="Branch", default=False,
                                 description=branch_des)

    trunk_des = "Cut trunk sections"
    trunk: bpy.props.BoolProperty(name="Trunk", default=False,
                                 description=trunk_des)

    def draw(self, context):
        """Draw UI."""

        layout = self.layout

        row = layout.row()
        row.scale_y = 1.25
        row.prop(self, "rizomuv_path")
