---
layout: default
title: Using The Bridge
parent: Usage & Installation
nav_order: 2
---
# Usage
{: .no_toc }

## Table of contents
{: .no_toc .text-delta }

1. TOC
{:toc}

---

## Panel Location

The RizomUV Bridge panel can be found in the 3D View Sidebar, the hotkey for the default "Blender" keymap to show the sidebar is **N**.

**Info:** The panel is only enabled in object mode.
{: .notice .notice-info}

---

## RizomUV Bridge

---

## UV Operations

### Load Recent File

The **Load Recent File** button opens RizomUV with the most recent file loaded and whatever progress was saved, it will not export anything at all from blender. This button will be unavailable if you have never exported anything from the bridge before.

### Export

Select one or more objects and click the **Export** button, RizomUV will open with your objects loaded and run a auto UV script (if you selected one). If the **Auto UV** box is checked this button will instead create an automatic UV map and instantly apply it in blender, to use this option you must have a script selected.

**Warning:** Your UV map names must not contain any periods.
{: .notice .notice-warning}

**Warning:** Each object needs to have the same UV maps. For example, if the first object has two UV maps: map1 and map2, every object you are exporting should have those maps.
{: .notice .notice-warning}

### Import

Click the **Import** button, each UV set on your original objects will be updated. You do not need to have any objects selected, the bridge will automatically find all matching objects and update the UV maps.

**Warning:** The script uses name matching to transfer the UV maps so it is important that you do not change the names of your original objects between operations.
{: .notice .notice-warning}

---

## Export Settings

### Preserve UVs

When this is option is enabled objects exported usuing the bridge will have their existing UVs preserved. If it is disabled the UVs will be projected upon loading into Rizom.

**Info:** Preserve UVs will automatically be disabled if any autoseams script is selected.
{: .notice .notice-info}

### Auto UV

This enables the automatic UV mapping functionality, while this is checked clicking on export will cause RizomUV to perform the autoseams script you have selected before closing and transferring the UV map to your blender objects.

### Script

These are scripts that will be automatically run when RizomUV opens, they automatically place seams and pack a quick UV map. I often begin by using one of these scripts then finalize the UV map manually.

The scripts have user configurable settings that will appear directly underneath the script selection box.

**Info:** These scripts will respect the settings that you choose in the **RizomUV Settings** panel, if you select a high number of mutations for example; it will take longer for the script to complete.
{: .notice .notice-info}



---

## Import Settings

### Mark Seams

When this is checked Blender will automatically mark the boundaries of all UV islands as sharp edges upon import. 

### Show Hidden

When this is checked the bridge will automatically reveal any hidden objects that have their UV map updated upon import. If it is left unchecked these objects will remain hidden (UV maps will still be updated).

---

## RizomUV Settings

---

## Viewport

### Texture Image Export

This field allows you to select a texture map that you can see in the RizomUV viewport and grid background. Once RizomUV opens you need to set your shading mode to **Viewport Texture Custom**, your texture will then be visible.

**Warning:** The file format must be one of: .tiff, .png, .jpg, .tga or .bmp
{: .notice .notice-warning}

---

## Layout

### Island Padding

This sets the **margin** and **spacing** settings in RizomUV, it controls the number of pixels between each island and the numbe of pixels between the tile border and the islands.

### Map Resolution

This sets the **Map Rez** setting in RizomUV, it controls the horizontal resolution of the texture map.

---

## Packing

### Quality

This sets the **Quality** setting in RizomUV, it controls the resolution of the packing algorithm.

**Info:** Higher numbers will result in more precise packs but longer computation times.
{: .notice .notice-info}

### Mutations

This sets the **Mutations** setting in RizomUV, it controls the number of trials when finding the best packing solution.

**Info:** Higher numbers will usually result in better packs but longer computation times.
{: .notice .notice-info}

### Pre-Orientation

This sets the **Initial Orientation** setting in RizomUV, it controls the bounding box pre-orientation before packing.

### Step Angle

This sets the **Step** setting in RizomUV, it controls the step angle when finding the bets orientation while packing.

---

## Addon Preferences

---

## Reset Settings

### Bridge settings

This will reset every setting inside the **RizomUV Bridge** panel.

### RizomUV settings

This will reset every setting inside the **RizomUV Settings** panel.

---

## RizomUV Path

### Rizom Path

This allows you to change the path to the RizomUV executable, it is important that this is set correctly.

