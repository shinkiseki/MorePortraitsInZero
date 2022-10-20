# More Portraits in Zero
Adds more portraits (Akatsuki, Azure, and completely new) in the **NISA Steam version of Trails from Zero**.

Created by: ShinKiseki (Reddit: [u/ShinKiseki](https://www.reddit.com/user/ShinKiseki); Twitter: [Shin_Kiseki](https://twitter.com/Shin_Kiseki))  
Latest release: v0.3.0 (released 2022-10-16)  
Last updated: 2022-10-19  
Compatible with: Trails from Zero v1.3.7  
  
Watch the release trailer here: Coming soon!

## Installation instructions
1.  Download the latest release of More Portraits in Zero. This should include, among other files, a data folder.
2.  Identify the folder where the Steam edition of Trails from Zero lives. Within this folder, there should be, among other files, the game itself (zero.exe) and a data folder. This is the __root folder__ of the game.
3.  Drag the mod's data folder into the root folder. This will copy all the mod files into the root folder, placing all files into the correct subfolders. Please note that this will replace some of the original scena (scenario) files.
4.  The mod has now been installed! New portraits will now be shown in-game.
5.  To uninstall the mod, use Steam's option to verify integrity of game files (Properties -> Local Files -> Verify integrity of game files...). This will revert all scena files back to normal. Note that the added portraits will not be removed.

## List of added characters
Completed characters in **bold**. Characters not previously included in the [Geofront version](https://www.youtube.com/watch?v=gPqF-cjxZ3c) of this mod are labeled as new.
*   **Wendy (completed files: 2/2)**
*   **Chaco (2/2)**
*   **Scott (14/14)**
*   **Wenzel (11/11)**
*   **Lynn (11/11)**
*   **Aeolia (11/11)**
*   **Pierre (2/2)**
*   **Mireille (3/3)**
*   **Sully (6/6)**
*   Abbas (0/6)
*   Michel (0/3)
*   **[NEW!] Fernand (2/2)**
*   **[NEW!] Franz (6/6)**
*   New character #3 (0/3)
*   New character #4 (0/3)

## Gameplay screenshots
### Wendy
![gameplay_screenshot_wendy_01](/gameplay_screenshots/gameplay_screenshot_wendy_01.jpg)

### Chaco
![gameplay_screenshot_chaco_01](/gameplay_screenshots/gameplay_screenshot_chaco_01.jpg)

### Scott
![gameplay_screenshot_scott_01](/gameplay_screenshots/gameplay_screenshot_scott_01.jpg)

### Wenzel
![gameplay_screenshot_wenzel_01](/gameplay_screenshots/gameplay_screenshot_wenzel_01.jpg)

### Lynn
![gameplay_screenshot_lynn_01](/gameplay_screenshots/gameplay_screenshot_lynn_01.jpg)

### Aeolia
![gameplay_screenshot_aeolia_01](/gameplay_screenshots/gameplay_screenshot_aeolia_01.jpg)

### Pierre
![gameplay_screenshot_pierre_01](/gameplay_screenshots/gameplay_screenshot_pierre_01.jpg)

### Fernand
![gameplay_screenshot_fernand_01](/gameplay_screenshots/gameplay_screenshot_fernand_01.jpg)

### Franz
![gameplay_screenshot_franz_01](/gameplay_screenshots/gameplay_screenshot_franz_01.jpg)

### Mireille
![gameplay_screenshot_mireille_01](/gameplay_screenshots/gameplay_screenshot_mireille_01.jpg)
![gameplay_screenshot_mireille_02](/gameplay_screenshots/gameplay_screenshot_mireille_02.jpg)

### Sully
![gameplay_screenshot_sully_01](/gameplay_screenshots/gameplay_screenshot_sully_01.jpg)
![gameplay_screenshot_sully_02](/gameplay_screenshots/gameplay_screenshot_sully_02.jpg)

## Reporting issues
If there is a bug encountered over the course of using this mod, I would appreciate being notified so that I may make the proper fixes.

For those comfortable with GitHub, please report any issues. The most helpful way to report an issue is to provide a screenshot and note when/where this is occurring. This will help identify the issue, then test that the issue has been resolved.

GitHub not your style? Feel free to message me via Reddit or Twitter. I am also around on Discord via several Falcom-related servers, including The Geofront.

For those using GitHub, please report these (or other) issues if they are discovered (once the issue is reported, I will label the issue accordingly):
*   **[Text]** There are typos, missing dialogue, or some other issue with the text. Pretty self-explanatory. While the primary focus is on text issues created by the mod itself, typos from the original game are also okay to report.
*   **[Portrait]** The wrong character portrait is used. This might be that the wrong character's portrait is appearing, or the right character has an expression inappropriate for their dialogue. The latter may be subjective to an extent, but feedback is always welcome.
*   **[Portrait]** The character might be missing a portrait altogether. This may be intentional (characters off-screen do not have portraits, for instance), but for the most part, the supported characters should have portraits.
*   **[Text box]** The text box may close and reopen between lines of dialogue, instead of remaining open. For characters without portraits, each line of dialogue creates a new text box; in other words, after each line, the text box closes, and another one opens to display the next line. For characters with portraits, this is different; a single text box opens for the entire set of dialogue, only closing after the last line. As part of the mod, the intent is for characters with added portraits to have their text boxes stay open for their entire dialogue.
*   **[Text box]** The text box size looks weird. As noted with the previous point, a single text box opens for an entire set of dialogue, rather than a new text box for each line. The text box will be long enough to accommodate the longest line of text; consequently, shorter lines of text may look weird. To an extent, this can be addressed by shifting words around to make each line approximately the same length, thus better filling out the text box.
*   **[Non-text box bug]** While unlikely, it's possible that the mod introduces some game-impacting bug.
*   **[Misc.]** There's probably something I've forgotten to list--let me know and I'll sort it out.

## The creation process
As there have been some elaborate steps taken to develop the assets and tools necessary to make this mod a reality, I'm providing a (hopefully) brief overview of how this mod was made. I'll be covering three parts: creating the raw image portrait files, converting the raw images to the proper format, and editing the scena (scenario) files.

To start, this mod includes portraits from three separate sources: Ao no Kiseki (also known as Trails to Azure), Akatsuki no Kiseki (a Trails gacha title never released in English), and the great work of [YuzuKiyochii](https://twitter.com/YuzuKiyochii). The Azure portraits were sourced from the Geofront version of Azure, so it was possible to directly port those back into Zero with no other modifications necessary.

For the Akatsuki images, though, this process was not as straightforward. Rather than each portrait being stored in a separate file, Akatsuki stores one large image per character:
![01-original_wendy](/documentation/01-original_wendy.png)

TBD

## Compatibility with other mods
*   [Inevitable Zero](https://github.com/Kyuuhachi/Inevitable-Zero)
    *   Currently incompatible due to modifying some of the same files. A combined mod is possible in the forseeable future upon the completion of More Portraits in Zero.
## Credits
*   [YuzuKiyochii](https://twitter.com/YuzuKiyochii) for the creation of all-new portraits for new characters #3 and #4.
*   [Graber](https://twitter.com/AdrianGraber) for [the version of EDDecompiler](https://github.com/AGraber/EDDecompiler) used for developing this mod.
*   Ouroboros for the development of the original [EDDecompiler](https://github.com/Ouroboros/EDDecompiler).

## Changelog
*   2022-10-20: Updated the number of total files for Sully (Sully appears as "Boy" in two files). Files for Sully completed. Added newly discovered issues to text files issue.
*   2022-10-19: Updated a portrait for Aeolia. Files for Mireille completed.
*   2022-10-17: Fixed issue where Pierre's portraits wouldn't appear when in his office (c1160.py).
*   2022-10-16: Released v0.3.0. New character #2 revealed (Franz). Added two new portraits for Pierre. Files for Pierre and Franz completed. Added folder of documentation images and updated README to include section about the creation process.
*   2022-10-14: Released v0.2.0. Updated scena files to correct several typos present in the original files, including an error causing "Ozelle" to be named "Zell" in some instances. Files for Scott, Wenzel, Lynn, and Aeolia completed. Added newly discovered issues to text issues file. Added folder of sample images and added images to README.
*   2022-10-13: Updated scena files to correct several typos present in the original files. More files for Scott, Wenzel, Lynn, and Aeolia completed. Added newly discovered issues to text issues file.
*   2022-10-11: Added a new portrait for Aeolia. Updated several Aeolia portraits. Updated scena files to correct several typos present in the original files. Files for Scott, Wenzel, Lynn, and Aeolia partially completed. Reorganized known text issues file and added newly discovered issues.
*   2022-10-09: Released v0.1.0. Added a new portrait for Chaco. New character #1 revealed (Fernand). Files for Wendy, Chaco, and Fernand completed. Updated README to include credits section and instructions for reporting issues, and installation instructions. Added list of known text issues fixed in this mod for documentation.
*   2022-10-07: Added all portraits (face) and half-busts (visual).
*   2022-10-06: Updated README to include to-do list.
*   2022-10-04: Creation of repository.
