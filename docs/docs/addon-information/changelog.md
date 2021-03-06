---
layout: default
title: Changelog
parent: Addon Information
nav_order: 2
---
# Changelog
{: .no_toc }

## Table of contents
{: .no_toc .text-delta }

1. TOC
{:toc}

---

## Version 0.1.0
{: .d-inline-block }
DEPRECATED
{: .label .label-red }

[rizomuv_bridge.zip](https://github.com/MattAshpole/BlenderRizomUVBridge/releases/download/0.1.0/rizomuv_bridge.zip)

### Improved
- Improved string concatenation during lua script construction.

### Known Bugs

- [Does not work in local view](https://github.com/MattAshpole/BlenderRizomUVBridge/issues/2).
- Texture map not loading.

---

## Version 0.2.0
{: .d-inline-block }
DEPRECATED
{: .label .label-red }

[rizomuv_bridge.zip](https://github.com/MattAshpole/BlenderRizomUVBridge/releases/download/0.2.0/rizomuv_bridge.zip)

### Improved
- Improved error catching and added report messages.

### Fixed
- Fixed [local view bug](https://github.com/MattAshpole/BlenderRizomUVBridge/issues/2)
- Fixed Texture Map loading

### Added
- Added support for multiple UV sets.
- Added links to documentation in addon preferences.

---

## Version 0.2.1
{: .d-inline-block }
DEPRECATED
{: .label .label-red }

[rizomuv_bridge.zip](https://github.com/MattAshpole/BlenderRizomUVBridge/releases/download/0.2.1/rizomuv_bridge.zip)

### Changed
- Changed startup script default to Sharp Edges Unwrap.

### Added
- Added option to automatically create seams and sharp edges from UV island boundaries.

---

## Version 0.3.0
{: .d-inline-block }
DEPRECATED
{: .label .label-red }

[rizomuv_bridge.zip](https://github.com/MattAshpole/BlenderRizomUVBridge/releases/download/0.3.0/rizomuv_bridge.zip)

### Improved
- Reorganised UI into more distinct sections so it is easier for me to expand in the future.
- More action reports.


### Changed
- Renamed scripts.

### Added
- Edit mode (opens RizomUV with the most recent file instead of overwriting with the selected objects).
- Added automatic UV mapping, one click automatic trip between RizomUV and Blender using the autoseams scripts.
- More settings (packing quality and mutations).

---

## Version 0.3.1
{: .d-inline-block }
DEPRECATED
{: .label .label-red }

[rizomuv_bridge.zip](https://github.com/MattAshpole/BlenderRizomUVBridge/releases/download/0.3.1/rizomuv_bridge.zip)

### Improved

- Added action reports and improved existing ones.

---

## Version 0.3.2
{: .d-inline-block }
DEPRECATED
{: .label .label-red }


[rizomuv_bridge.zip](https://github.com/MattAshpole/BlenderRizomUVBridge/releases/download/0.3.2/rizomuv_bridge.zip)

### Fixed
- Fixed [Incorrect context error](https://github.com/MattAshpole/BlenderRizomUVBridge/issues/5)
- Changed UV map matching for multiple UV sets from map index to map name to avoid a bug where the index would change causing UVs to be transferred to the wrong UV set.

---

## Version 0.4.0
{: .d-inline-block }
DEPRECATED
{: .label .label-red }

[rizomuv_bridge.zip](https://github.com/MattAshpole/BlenderRizomUVBridge/releases/download/0.4.0/rizomuv_bridge.zip)

### Fixed

- Fixed [Mark seams incorrect behavior](https://github.com/MattAshpole/BlenderRizomUVBridge/issues/6)

### Improved

- Changed all settings to addon level preferences so that they are saved between Blender sessions.

### Added

- Button to reset settings to default for each panel.

---

## Version 0.4.1
{: .d-inline-block }
DEPRECATED
{: .label .label-red }


[rizomuv_bridge.zip](https://github.com/MattAshpole/BlenderRizomUVBridge/releases/download/0.4.1/rizomuv_bridge.zip)

### Fixed

- Fixed [Mark seams incorrect behavior](https://github.com/MattAshpole/BlenderRizomUVBridge/issues/6) (overlooked something that was not fixed in 0.4.0)

### Improved

- Rewrote import code so that it is no longer required to have objects selected before clicking import, the bridge will now automatically update the UV maps of matching scene objects. [Import fix](https://github.com/MattAshpole/BlenderRizomUVBridge/issues/7)
- Improved action reports

---

## Version 0.4.2
{: .d-inline-block }
DEPRECATED
{: .label .label-red }

[rizomuv_bridge.zip](https://github.com/MattAshpole/BlenderRizomUVBridge/releases/download/0.4.2/rizomuv_bridge.zip)

### Fixed

- Fixed [issues described by akaSpy](https://github.com/MattAshpole/BlenderRizomUVBridge/issues/7#issuecomment-504720225)

### Improved

- Improved code so that the bridge import will now find hidden objects, objects in hidden collections and objects in excluded collections.

### Added

- New button under **import settings** to toggle revealing hidden objects. If left unchecked any hidden objects or collections will be left hidden even if they were updated by the bridge, if checked any updated collections or objects will be revealed if they were previously hidden.

---

## Version 0.4.3
{: .d-inline-block }
DEPRECATED
{: .label .label-red }

[rizomuv_bridge.zip](https://github.com/MattAshpole/BlenderRizomUVBridge/releases/download/0.4.3/rizomuv_bridge.zip)

### Fixed

- Fixed RuntimeError exception upon clicking import with objects in a hidden collection but no matching objects for import in the scene.
- Fixed bug with `get_meshes()` util function returning a variable referenced before assigned error.
- **Auto UV** checkbox now automatically unchecks itself if no unwrap script is selected, this prevents user from activating auto uv then switching off the unwrap script which leads to the automatic uv procedure doing nothing.

### Improved

- Optimised code: approx 56% performance increase for export, approx 84% performance increase for import.
- One error report improvement.

---

## Version 0.5.0
{: .d-inline-block }
DEPRECATED
{: .label .label-red }

[rizomuv_bridge.zip](https://github.com/MattAshpole/BlenderRizomUVBridge/releases/download/0.5.0/rizomuv_bridge.zip)

### Fixed

- Fixed issue which would sometimes cause Rizom to crash upon loading an autoseams script.
- UVs are now normalised upon loading into Rizom so the autoseam scripts work properly at all times.

### Improved

- Added error check to prevent user from exporting if none of the selected objects have a UV Map.

### Added

- Added basic user settings for **Autoseams: Mosaic** and **Autoseams: Sharp Edges**.

---

## Version 0.5.1
{: .d-inline-block }
DEPRECATED
{: .label .label-red }

[rizomuv_bridge.zip](https://github.com/MattAshpole/BlenderRizomUVBridge/releases/download/0.5.1/rizomuv_bridge.zip)

### Added

- Added new option to preserve existing UVs when exporting from Blender. [issue described by TheSpacebarRider](https://github.com/MattAshpole/BlenderRizomUVBridge/issues/11)

---

## Version 0.6.0
{: .d-inline-block }
DEPRECATED
{: .label .label-red }

[rizomuv_bridge.zip](https://github.com/MattAshpole/BlenderRizomUVBridge/releases/download/0.6.0/rizomuv_bridge.zip)

### Improved

- Minor tooltip improvements.
- Made UI more compact to free up screen space.
- Updated default RizomUV executable path.
- Changed **Edit** button label to **Load Recent File** (functionality unchanged).
- **Load Recent File** can now be used when **Auto UV** is enabled.

### Fixed

- Bridge now handles error if the RizomUV path is incorrect and prompts user to correct it. [issue described by erispe](https://github.com/MattAshpole/BlenderRizomUVBridge/issues/12)
- Bridge will now allow Non-alphanumeric characters in UV Map names. Periods are the only exception, Rizom will not load any mesh with periods in the UV map name so they remain restricted. [issue described by muchimi](https://github.com/MattAshpole/BlenderRizomUVBridge/issues/13)
- Fixed incorrect tooltips for the settings reset buttons.

### Added

- New user options for every autoseams script. (Cut Handles/Cut Pipes)
- New panel to change the RizomUV exe path directly from the main UI.

---

## Version 0.6.1

{: .d-inline-block }
STABLE
{: .label .label-green }

[rizomuv_bridge.zip](https://github.com/MattAshpole/BlenderRizomUVBridge/releases/download/0.6.1/rizomuv_bridge.zip)

### Improved

- **Preserve UVs** is now default behaviour unless a script is selected, checkbox removed as it is now redundant.
- **Step Angle** default value changed to 90°.

### Fixed

- Rizom suffix preference added to line 2 of LUA script (hopefully fixes some people having file suffix enabled in Rizom which causes UV import to fail)
- **Edge Angle** and **Segments** properties now correctly set as annotations using **:** instead of **=**.
- **Edge Angle** property subtype changed to angle.
- Import button checks for existence of the temp fbx file created by the bridge, if it does not exist import button is disabled. 

### Added

- New **Flatten UVs** script (simple flat projection).
- Leaf/Branch/Trunk toggles for the **Autoseams: Pelt** script.