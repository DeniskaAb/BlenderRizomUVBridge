# <pep8-80 compliant>

"""Utility functions for use in addons"""

import bpy


def get_meshes(selected):
    """Get selected objects and filter for meshes

    Args:
        selected (bool): True for selected objects, False for all objects

    Returns:
        list: A list of selected bpy_types.Object items

    """

    if selected:
        objs = bpy.context.selected_objects
        objs = [item for item in objs if item.type == 'MESH']

        if not objs:
            objs = [bpy.context.active_object]

    elif not selected:
        for item in bpy.data.objects:
            objs = [item for item in bpy.data.objects if item.type == 'MESH']

    return objs


def set_object_context(context_mode):  # pylint: disable=unused-argument
    """Set the objects context.

    Args:
        context_mode (str): 'OBJECT' or 'EDIT'

    Returns:
        string: Original object context.

    """

    og_context = bpy.context.object.mode
    bpy.ops.object.mode_set(mode=context_mode)

    return og_context


def sel_mode(vert=None, edge=None, face=None):
    """Get selection mode

    Args:
        vert (bool): Vertex selection mode.
        edge (bool): Edge selection mode.
        face (bool): Face selection mode.

    Returns:
        bpy_prop_array: Array of booleans representing active selection modes.

    """

    sel_mode = bpy.context.scene.tool_settings.mesh_select_mode

    if vert or edge or face:
        bpy.context.scene.tool_settings.mesh_select_mode = [vert, edge, face]

    return sel_mode