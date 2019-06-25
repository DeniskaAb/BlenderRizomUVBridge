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
STABLE
{: .label .label-green }

### Fixed

- Fixed RuntimeError exception upon clicking import with objects in a hidden collection but no matching objects for import in the scene.
- Fixed bug with `get_meshes()` util function returning a variable referenced before assigned error.
- **Auto UV** checkbox now automatically unchecks itself if no unwrap script is selected, this prevents user from activating auto uv then switching off the unwrap script which leads to the automatic uv procedure doing nothing.

### Improved

- Optimised code: approx 56% performance increase for export, approx 84% performance increase for import.
- Error report improvements.