# Toontown Public Rigs

This is a set of public use rigs, for both personal use and groups, that have been set up to work with Toontown repos to preserve old animations, while allowing the creation of new ones.

Adding new content to Toontown is difficult due to the broken state of ripped rigs, and hopefully these resources should encourage more people to try out creating for the community. Every step of the process of making the rigs exists here so that modifications can be made.

# Quick Start

_Note: you will need some knowledge on how cmd/shell, python, and Blender work_.

1. Install:
- [Panda3D](https://www.panda3d.org/)
- Toontown Source (Either [Open Toontown](https://github.com/open-toontown/open-toontown) or [Toontown School House](https://github.com/Toontown-Open-Source-Initiative/Toontown-School-House) work.) Download the resources for your source as well!
- [Blender](https://www.blender.org/)
- [YABEE](https://github.com/Toontown-Event-Horizon/YABEE)
- [CGDive Game Rig Tools](https://toshicg.gumroad.com/l/game_rig_tools)
- Any IDE or a text editor (i.e. [Pycharm](https://www.jetbrains.com/pycharm/), [Notepad++](https://notepad-plus-plus.org/downloads/), whatever you prefer to edit Python with)
2. Download either:
Want to modify the rig:
- All files in this repository
Just want to add new animations:
- Only download the **baked** and **gameready** files.
3. Open one of the projects. Make sure _YABEE_, _Game Rig Tools_, and Blender's preinstalled *Rigify* is installed/enabled. If you are unsure how, follow this [guide](https://github.com/Pullusb/How_to_install_Blender_addons).
4. Attach textures to the Cog from your Toontown repo's resources, located within the **maps** folder within **phase_3.5**.
5. When the project opens: Press **A** to select everything in the scene. Go to the **File** tab, and if you installed YABEE correctly select the **Panda3d (.egg)** option.

![image](https://github.com/user-attachments/assets/f63073bb-dafe-4353-aa6e-ad8bfa029761)

6. A window should pop up, make sure your settings look like this:

![image](https://github.com/user-attachments/assets/e324f7a4-3f77-4acb-af7d-822ea38206a1)

7. Export the rig. Then rinse and repeat with the other rigs (Make sure if you are modifying the Cogs or Toons you do _all of the variants_ since you will need to change code later.)
8. You will need to run Panda3D's **egg-optchar** to expose parts of the rig needed for it to work correctly in game. Open up powershell (on Windows) or shell (on Linux/MacOS) in the directory, and run the following command so that the rig has all the meshes and joints exposed for them to work properly:

Cogs:

```
egg-optchar FileName.egg -keepall -inplace -flag arms -flag hands -flag legs -flag torso -expose ATTACH-meter -expose ATTACH-head -expose ATTACH-hold.L -expose ATTACH-hold.R -expose ATTACH-shadow
```
To make sure it ran correctly, double clicking on .bam files should open them to a view of the model. Pressing **shift-L** will display the model's contents in the console, and should look like this:

![image](https://github.com/user-attachments/assets/c7fead19-ff4e-454f-a701-9f2fd2b095a4)

10. Then, run **egg2bam** on all of the files. If you have Windows you can use the provided **bulkegg2bam** powershell script in the repo to convert any .eggs placed in its folder to .bams when running.
11. Replace the old animation files in resources with the new ones. You will need to do some navigating to find where they are all located, look in **Suit.py/Toon.py** for references. Usually, most Toon animations are under phase_3/models/char and the same paths under phase_3.5 and phase_4, but not all of them. Most Suit animations are in phase_3.5 and phase_5.
12. Last step, I swear. You need to replace all references to exposed joints for suits in the codebase with the new names. If you are using Pycharm you can `ctrl+shift+r` to do Find and Replace in every file. The conversions are:

Cogs:
```
joint_Lhold -> ATTACH-hold.L
joint_Rhold -> ATTACH-hold.R
joint_head -> ATTACH-head
joint_attachMeter -> ATTACH-meter
joint_shadow -> ATTACH-shadow
```

13. Profit! Adding new animations would be as simple as animating -> exporting -> and coding it in. If you want to practice, I would recommend replacing already existing animations with new ones to avoid having to code right away.

# How Does This Work?

For a detailed explanation look [here](https://www.toontowneventhorizon.com/posts/backstage-cog-rigs/)!

The old rigs from TTO are unanimatable due to the lossy method of converting to the .bam format. In addition, TTO team used a metarig format that is no longer around. However, to avoid losing many animations, but still have the ability to add new ones, you can "transfer" the animations over to a new rig by setting up the old rig to puppet the new one. Essenitally then moving them over, hopefully seamlessly.

# Can I modify the rig?

**Yes!** We actually encourage it! Although you'd want experience with Blender's rigify system, its possible to add your own custom Cog model, rig, and export with our tools the same way if you want.

# What is TODO?

Currently there are a number of things that are being worked on including:
- Toon rigs
- Better tools for getting new animations in.
- Rig improvements for TTO accuracy
