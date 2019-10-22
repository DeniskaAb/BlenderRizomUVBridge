# <pep8-80 compliant>

"""LUA Script functions for RizomUV operations."""

import tempfile
import os
import bpy

TEMP_PATH = tempfile.gettempdir() + os.sep + "rizom_temp.fbx"
TEMP_PATH = '/'.join(TEMP_PATH.split('\\'))


def script_paths(key):
    """Dictionary of LUA scripts.

    returns:
        str: The Path of the specified script.

    """

    scripts_dir = os.path.abspath(os.path.dirname(__file__))\
        .replace("ma_utils", "lua_scripts\\")

    scripts_dic = {
        'NO_SCRIPT': scripts_dir + "blank.lua",
        'PELT': scripts_dir + "pelt_algorithm.lua",
        'MOSAIC': scripts_dir + "mosaic_algorithm.lua",
        'SHARP_EDGES': scripts_dir + "sharp_edge_algorithm.lua",
        'BOX': scripts_dir + "box_algorithm.lua",
        'CONSTRUCT': scripts_dir + "py_construct.lua",
        'FLATTEN': scripts_dir + "flatten.lua"
    }

    script = scripts_dic[key]

    return script


def script_settings():
    """User settings for the scripts.

    returns:
        str: String needed to set the correct setting.

    """

    props = bpy.context.preferences.addons["rizomuv_bridge"].preferences

    if props.script_run == 'SHARP_EDGES':
        settings = ("ZomSet({Path="'"Vars.AutoSelect.SharpEdges.Angle"'""
                    + ", Value=" + str(props.sharp_value) + "})" + "\n"
                    + "ZomSet({Path="'"Vars.AutoSelect.LinkHoles"'""
                    + ", Value=" + str(props.link_holes).lower() + "})" + "\n"
                    + "ZomSet({Path="'"Vars.AutoSelect.CutHandles"'""
                    + ", Value=" + str(props.cut_handles).lower() + "})"
                    + "\n")

    elif props.script_run == 'MOSAIC':
        settings = ("ZomSet({Path="'"Vars.AutoSelect.Mosaic.Developability"'""
                    + ", Value=" + str(props.mosaic_value) + "})" + "\n"
                    + "ZomSet({Path="'"Vars.AutoSelect.LinkHoles"'""
                    + ", Value=" + str(props.link_holes).lower() + "})" + "\n"
                    + "ZomSet({Path="'"Vars.AutoSelect.CutHandles"'""
                    + ", Value=" + str(props.cut_handles).lower() + "})"
                    + "\n")

    elif props.script_run == 'PELT':
        settings = ("ZomSet({Path="'"Vars.AutoSelect.LinkHoles"'""
                    + ", Value=" + str(props.link_holes).lower() + "})" + "\n"
                    + "ZomSet({Path="'"Vars.AutoSelect.CutHandles"'""
                    + ", Value=" + str(props.cut_handles).lower() + "})"
                    + "\n"
                    + "ZomSet({Path="'"Vars.AutoSelect.Hierarchical.Leafs"'""
                    + ", Value=" + str(props.leaf).lower() + "})" + "\n"
                    + "ZomSet({Path="'"Vars.AutoSelect.Hierarchical.Branches"'""
                    + ", Value=" + str(props.branch).lower() + "})" + "\n"
                    + "ZomSet({Path="'"Vars.AutoSelect.Hierarchical.Trunk"'""
                    + ", Value=" + str(props.trunk).lower() + "})" + "\n")


    elif props.script_run == 'BOX':
        settings = ("ZomSet({Path="'"Vars.AutoSelect.LinkHoles"'""
                    + ", Value=" + str(props.link_holes).lower() + "})" + "\n"
                    + "ZomSet({Path="'"Vars.AutoSelect.CutHandles"'""
                    + ", Value=" + str(props.cut_handles).lower() + "})"
                    + "\n")

    else:
        settings = ""

    return settings


def export_settings_str():
    """Strings used to write export settings when constructing the LUA script.

        returns:
            list: A list of strings that can be used in LUA scripts.

        """
    props = bpy.context.preferences.addons["rizomuv_bridge"].preferences

    valid_extensions = (".tiff", ".png", ".jpg", ".tga", ".bmp")

    image = ("ZomLoadUserTexture("'"' + props.image_path + '"'")")
    if props.image_path.lower().endswith(valid_extensions):
        image = '/'.join(image.split('\\'))

    else:
        image = ""

    return [image]


def ruv_settings_str():
    """Strings used to write RizomUV settings when constructing
     the LUA script.

    returns:
        list: A list of strings that can be used in LUA scripts.

    """

    props = bpy.context.preferences.addons["rizomuv_bridge"].preferences

    shell_padding = ("ZomIslandGroups({Mode='SetGroupsProperties',"
                     " WorkingSet='Visible', MergingPolicy=8322,"
                     " GroupPaths={ 'RootGroup' },"
                     " Properties={Pack={SpacingSize="
                     + str(props.shell_pad/props.map_res) + "}}})")

    tile_padding = ("ZomIslandGroups({Mode='SetGroupsProperties',"
                    " WorkingSet='Visible', MergingPolicy=8322,"
                    " GroupPaths={ 'RootGroup' },"
                    " Properties={Pack={MarginSize="
                    + str(props.shell_pad/props.map_res) + "}}})")

    map_res = ("ZomSet({Path='Prefs.PackOptions.MapResolution',"
               " Value=" + str(props.map_res) + "})")

    orient_step = ("ZomIslandGroups"
                   "({Mode='SetGroupsProperties', WorkingSet='Visible',"
                   " MergingPolicy=8322, GroupPaths={ 'RootGroup' },"
                   " Properties={Pack={Rotate={Step="
                   + str(props.orient_step) + "}}}})")

    preorient = ("ZomIslandGroups({Mode='SetGroupsProperties',"
                 " WorkingSet='Visible', MergingPolicy=8322, GroupPaths="
                 "{ 'RootGroup' }, Properties={Pack={Rotate={Mode="
                 + props.init_orient + "}}}})")

    quality = ("ZomIslandGroups({Mode='SetGroupsProperties',"
               " WorkingSet='Visible', MergingPolicy=8322,"
               " GroupPaths={ 'RootGroup' },"
               " Properties={Pack={Resolution=" + str(props.pack_qual)
               + "}}})")

    mutations = ("ZomIslandGroups({Mode='SetGroupsProperties',"
                 " WorkingSet='Visible', MergingPolicy=8322,"
                 " GroupPaths={ 'RootGroup' },"
                 " Properties={Pack={MaxMutations=" + str(props.mutations)
                 + "}}})")

    return [shell_padding, tile_padding, map_res, orient_step, preorient,
            quality, mutations]


def load_file():
    """Function to load the file into rizom.

    returns:
        str: LUA script to import the file.

    """

    file_load = ("ZomLoad({File={Path=" + '"' + TEMP_PATH + '"' + ","
                 "ImportGroups=true, XYZUVW=true,"
                 " UVWProps=true}})")

    return file_load


def save_file():
    """Function to save the file as a precaution.

    returns:
        str: LUA script to overwrite the imported fbx file.

    """

    file_save = ("ZomSave({File={Path=" + '"' + TEMP_PATH + '"' + ","
                 "UVWProps=true, FBX={UseUVSetNames=true}},"
                 " __UpdateUIObjFileName=true})")

    return file_save


def write_script_edit():
    """Construct script to be used by edit operator.

    returns:
        str: The Path of the resulting script.

    """

    setting_str = ruv_settings_str()
    save = save_file()

    preset_script = script_paths('NO_SCRIPT')
    lua_preset = open(preset_script, "r")
    preset_content = lua_preset.read()
    lua_preset.close()

    final_script = script_paths('CONSTRUCT')
    lua_final = open(final_script, "w")
    lua_final.truncate(0)

    for string in setting_str:
        lua_final.write(" ".join([string]) + "\n")

    lua_final.write(" ".join([preset_content, save]) + "\n")

    lua_final.close()

    return final_script


def write_script():
    """Construct the final lua script to be loaded on startup.

    returns:
        str: The Path of the resulting script.

    """

    props = bpy.context.preferences.addons["rizomuv_bridge"].preferences

    strings = ruv_settings_str() + export_settings_str()
    script_setting = script_settings()
    load = load_file()
    save = save_file()
    suffix = "ZomSet({Path="'"Prefs.FileSuffix"'", Value="'""'"})"

    preset_script = script_paths(props.script_run)
    lua_preset = open(preset_script, "r")
    preset_content = lua_preset.read()
    lua_preset.close()

    final_script = script_paths('CONSTRUCT')
    lua_final = open(final_script, "w")
    lua_final.truncate(0)

    lua_final.write(load + "\n" + suffix)
    lua_final.write("\n" + script_setting)

    for string in strings:
        lua_final.write(" ".join([string]) + "\n")

    lua_final.write("".join([preset_content, "\n", save]))

    if props.auto_uv is True:
        lua_final.write("\n" + "ZomQuit()")

    lua_final.close()

    return final_script
