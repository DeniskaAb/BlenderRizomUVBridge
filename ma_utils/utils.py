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

    objs = []

    if selected:
        objs = bpy.context.selected_objects
        objs = [item for item in objs if item.type == 'MESH']

        if not objs:
            objs = [bpy.context.active_object]

    elif not selected:
        for item in bpy.data.objects:
            objs = [item for item in bpy.data.objects if item.type == 'MESH']

    return objs


def delete_meshes(objs):
    """Delete object data without using operators"""

    for obj in objs:
        bpy.data.objects.remove(bpy.data.objects[obj.name], do_unlink=True)


def set_object_context(context_mode):
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

    mode = bpy.context.scene.tool_settings.mesh_select_mode

    if vert or edge or face:
        bpy.context.scene.tool_settings.mesh_select_mode = [vert, edge, face]

    return mode


def collections_reveal(objs):
    """Reveal hidden collections if they contain any of
    the supplied objects.

    Args:
        objs (list): A list of bpy_types.Object items

    Returns:
        list: List of collections that have been revealed.

    """

    collections = bpy.context.view_layer.layer_collection.children
    sorted_collections = []

    for col in collections:
        user_col = col.collection
        for obj in user_col.objects:
            if obj in objs:
                sorted_collections.append(col)

    col_hidden_list = [
        col for col in sorted_collections if col.hide_viewport is True]
    col_exclude_list = [
        col for col in sorted_collections if col.exclude is True]

    for col in col_hidden_list:
        col.hide_viewport = False

    for col in col_exclude_list:
        col.exclude = False

    return col_hidden_list, col_exclude_list


def collections_hide(col_hide_list, col_exclude_list):
    """Hide collections in list"""

    for col in col_hide_list:
        col.hide_viewport = True

    for col in col_exclude_list:
        col.exclude = True


def objects_reveal(objs):
    """Reveal hidden objects.

    Args:
        objs (list): A list of bpy_types.Object items

    Returns:
        list: List of objects that have been revealed.

    """

    hidden_objs = [obj for obj in objs if not obj.visible_get()]

    for obj in hidden_objs:
        obj.hide_set(False)

    return hidden_objs


def objects_hide(objs):
    """Hide given objects.

    Args:
        objs (list): A list of bpy_types.Object items

    """

    for obj in objs:
        obj.hide_set(True)
