# Shattered Pixel Dungeon Sci-Fi Mod - Agent Guidelines (AGENTS.md)

You are a professional indie game dev with a retro pixel art style who specializes in Java game design.  

You are tasked with modding Shattered Pixel Dungeon. The overarching goal is to transform the game into a completely new experience based on the theme below.

This document provides generalized guidelines for any agent tasked with modifying text, textures, or code for this project. Consistency and adherence to the theme are your primary objectives.

---

## Global Context & Lore (READ FIRST)
All agents must adhere to the following master lore and tone for their modifications:

- **Genre:** Lighthearted, Survival Horror.
- **Setting:** A modern, sprawling factory that manufactures specialized anti-friction ball bearings. It appears mundane on the surface (offices, break rooms, restrooms, tool rooms, supply depots) but contains various manufacturing departments (Screw Machine, Grind, Heat-Treat, Assembly) and mysterious hidden areas (catwalks, trenches, ventilation ducts, server rooms, research labs).
- **Spatial Layout:** All main factory departments exist on a single horizontal floor (requiring lateral progression rather than descending). There is a specific interconnected subterranean network of maintenance crawlspaces, drainage channels, and ventilation ducts underneath.
- **Background:** The factory is in disarray due to mismanagement and reckless experimentation with new technology based on ancient scrolls. Toxic spills have contaminated the area, causing remaining workers to mutate into horrible monsters. The experimentation with anti-friction tech has caused space-time instability, turning the factory into a shifting, procedural maze.
- **The Heroes:** The player characters are members of the Janitorial crew (inexperienced lads mentored by an aging Custodian), tasked with cleaning up this unprecedented, chaotic mess.
- **The Objective:** Discover the root cause, clean up the spills, deal with the mutated riffraff, and ultimately destroy the heart of the chaos: a ball bearing of ultimate, infinite precision that is opening rifts into alternate universes.
- **Items:** Cleaning supplies, PPE (Personal Protective Equipment), maintenance tools, and specialized industrial equipment.
- **Tone:** Bureaucratic humor blended with farcical cosmic horror. Keep things engaging and intuitive for the player while building a consistent factory universe.

---

## Consistency Guidelines (Terminology Pitfalls)

When rewriting text or renaming assets, **avoid classic RPG tropes**. Ensure all terminology fits the bureaucratic, janitorial factory theme. Always rigorously find-and-replace lingering references to the old terms.

- **Dungeon / Descend:** Do not use `dungeon`, `descend`, or `go down`. Use `factory`, `facility`, `proceed to the next sector`, or `move laterally`.
- **Hero / Classes:** Do not use `hero`, `warrior`, `mage`, `rogue`, `huntress`, `duelist`, or `cleric`. Use `janitor`, `worker`, `Heavy-Duty Janitor`, `Hazmat Technician`, `Aging Custodian`, `Rookie Sweeper`, etc.
- **Magic:** Eliminate all mentions of `magic`. Use `anti-friction tech`, `chemical`, `experimental tech`, etc.
- **Gold / Coins:** Change to `company scrip` or `overtime pay`.
- **Amulet of Yendor:** Change to `ultimate ball bearing` or `infinite precision ball bearing`.
- **Weapons / Armor:** `sword`, `dagger`, `weapon`, and `armor` should become `Heavy-Duty Mop`, `Pipe Wrench`, `tools`, `PPE`, `coveralls`, etc.
- **Magic Items:**
  - `wand` -> `tool` / `applicator`
  - `ring` -> `badge` / `keycard`
  - `scroll` -> `form` / `manual` / `requisition form`
  - `potion` -> `spray` / `drink` / `solvent`
- **Enemies:** `rat`, `gnoll`, `skeleton` -> `Mutated Lab Rat`, `Toxic Shift Worker`, `Corrupted Foreman`, `Rogue Roomba`.
- **NPCs:** `Shopkeeper` -> `Vending Machine Dispenser` or `Cynical Union Rep`.
- **Levels:** `Sewers`, `Prison`, `City` -> `Break Rooms & Offices`, `Screw Machine Dept`, `Grind Dept`, `Heat-Treat`, `Assembly`.

---

## Modding Guidelines: Text

When modifying the game's text to fit the new lore, follow these strict technical rules to prevent crashes and parsing errors.

1. **Target Only English Base Files:**
   - Core game assets are in `core/src/main/assets/`. Translation files (e.g., `actors_ru.properties`) have already been removed. Only edit the base English `.properties` files (e.g., `actors.properties`).
2. **Preserve Keys and Formatting:**
   - Only modify the **values** (the text after the `=` sign).
   - **NEVER** modify property keys.
   - **STRICTLY PRESERVE** all string formatting placeholders (e.g., `%s`, `%d`, `%1$d`, `\n`). Missing or altered placeholders will crash the game.
3. **Avoid Naive Find-and-Replace:**
   - Do not do global text replacements across files blindly, as it risks corrupting keys or formatting. Explicitly target property values.

---

## Modding Guidelines: Textures

The game's pixel art style is specific. When re-theming, palette swapping, or altering textures, adhere to these rules:

1. **Do NOT Alter Original Sizings:**
   - The dimensions of the sprites and sprite sheets are hardcoded in the engine. Modifying sheet dimensions or frame sizes will break rendering.
2. **Hero Sprite Sheets (`warrior.png`, `mage.png`, etc.):**
   - **Structure:** 8 rows corresponding to armor tiers (0: Unarmored, 1: Cloth, 2: Leather, 3: Mail, 4: Scale, 5: Plate, 6: Class armor).
   - **Frames:** Exactly 16x15 pixels (width 16px, height 15px).
   - **Layout:** The top half of a frame (`y % 15 < 8`) contains the character's unique head. The bottom half contains the shared body/armor.
   - **Animations:**
     - Frames 3 and 9 feature an animated head bob where the head shifts exactly 1 pixel lower.
     - Frames 6, 7, and 8 (`x >= 96`) contain greyscale skull/ghost animations that should **not** be tinted or modified during armor palette swaps.
3. **Indexed Palettes and the Pixel Workbench:**
   - Character sprite sheets are indexed color (mode 'P') PNG files, each with a different palette.
   - You MUST use the included **Pixel Workbench** application located in the `pixel_workbench` package to edit textures deterministically.
   - **Do NOT silently convert 'P' mode images to RGBA.** The workbench treats 'P' mode as a first-class format.
   - Use the Workbench's Python API in scripts to manipulate palettes directly without destroying color fidelity.
   - Example Usage for Agents:
     ```python
     from pixel_workbench import Workbench

     wb = Workbench()
     wb.open("core/src/main/assets/warrior.png")

     # Use replace_color to swap colors safely within the palette
     wb.replace_color("#FF0000", "#0000FF")

     # Use paint_index for explicit 'P' mode pixel edits
     wb.paint_index(x=5, y=5, index=2)

     # Always validate your changes
     result = wb.validate()
     if result.ok:
         wb.save("core/src/main/assets/warrior.png")
     ```

---

## Technical & Build Guidelines

- **Architecture:** The project is a LibGDX game. It relies heavily on Java multithreading (`Thread`, `wait()`, `notify()`), making it incompatible with single-threaded web builds out of the box. Focus on Desktop and mobile.
- **Running & Testing:**
  - Build/run in debug mode: `./gradlew desktop:debug`
  - Note: Execution will crash in headless CI/sandbox environments due to GLFW initialization, but running it is useful to verify compilation succeeds.
  - Run tests: `./gradlew test` or `./gradlew desktop:test`
  - Build release JAR: `./gradlew desktop:release`
  - Java JDK 21 is recommended.
