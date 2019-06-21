# <pep8-80 compliant>

"""__init__"""

import bpy

from .preferences import RizomUVBridgeAddonPreferences
from .operators.file_operations import ExportToRizom, ImportFromRizom,\
    EditInRizom
from .operators.addon_operations import ResetBridgeSettings,\
    ResetRizomUVSettings
from .ui.bridge_panel import RizomUVBridgePanel, RizomUVSettingsPanel

bl_info = {  # pylint: disable=invalid-name
    "name": "RizomUV Bridge",
    "description": "Streamlined workflow between Blender and RizomUV.",
    "author": "MattA",
    "version": (0, 2, 1),
    "blender": (2, 80, 0),
    "location": "View3D > Sidebar",
    "wiki_url": "https://mattashpole.github.io/BlenderRizomUVBridge/",
    "tracker_url": ("https://github.com/MattAshpole/"
                    "BlenderRizomUVBridge/issues"),
    "category": "UV"
}

CLASSES = [RizomUVBridgeAddonPreferences,
           ExportToRizom,
           ImportFromRizom,
           EditInRizom,
           ResetBridgeSettings,
           ResetRizomUVSettings,
           RizomUVBridgePanel,
           RizomUVSettingsPanel]


def register():
    """register operators and menus"""

    for cls in CLASSES:
        bpy.utils.register_class(cls)


def unregister():
    """unregister operators and menus"""

    for cls in CLASSES:
        bpy.utils.unregister_class(cls)
