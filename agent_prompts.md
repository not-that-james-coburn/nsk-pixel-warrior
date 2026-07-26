# Shattered Pixel Dungeon Sci-Fi Mod - Agent Prompts (Stage 1: Text)

To accomplish the first stage of transforming the game's text into our specific setting, we will divide the work among **5 agents**. Each agent will handle a distinct category of files, ensuring no overlap in their work.

---

## Global Context & Lore (READ FIRST)
All agents must adhere to the following master lore and tone for their text replacements:

- **Genre:** Lighthearted, Survival Horror.
- **Setting:** A modern, sprawling factory that manufactures specialized anti-friction ball bearings. It appears mundane on the surface (offices, break rooms, restrooms, tool rooms, supply depots) but contains various manufacturing departments (Screw Machine, Grind, Heat-Treat, Assembly) and mysterious hidden areas (catwalks, trenches, ventilation ducts, server rooms, research labs).
- **Background:** The factory is in disarray due to mismanagement and reckless experimentation with new technology based on ancient scrolls. Toxic spills have contaminated the area, causing remaining workers to mutate into horrible monsters. The experimentation with anti-friction tech has caused space-time instability, turning the factory into a shifting, procedural maze.
- **The Heroes:** The player characters are members of the Janitorial crew (inexperienced lads mentored by an aging Custodian), tasked with cleaning up this unprecedented, chaotic mess.
- **The Objective:** Discover the root cause, clean up the spills, deal with the mutated riffraff, and ultimately destroy the heart of the chaos: a ball bearing of ultimate, infinite precision that is opening rifts into alternate universes.
- **Items:** Cleaning supplies, PPE (Personal Protective Equipment), maintenance tools, and specialized industrial equipment.

---

## Agent 1: Translation Cleanup
**Objective:** Prepare the codebase for extensive text changes by removing all non-English translation files and disabling the language selection UI, as recommended by the Shattered Pixel Dungeon documentation.

**Prompt for the Agent:**
```
You are an expert Java developer tasked with modifying a LibGDX game (Shattered Pixel Dungeon). Your goal is to remove all non-English translations from the game to prepare it for a complete text rewrite in English.

Please follow these exact steps, as outlined in `docs/recommended-changes.md`:
1. Navigate to the directories inside `core/src/main/assets/messages/` (actors, items, journal, levels, misc, plants, scenes, ui, windows).
2. Delete all `.properties` files that have an underscore and language code (e.g., delete `actors_ru.properties`, `actors_es.properties`, etc., but DO NOT delete `actors.properties`).
3. Open `core/src/main/java/com/shatteredpixel/shatteredpixeldungeon/messages/Languages.java` and remove all enum constants except for `ENGLISH`.
4. Open `core/src/main/java/com/shatteredpixel/shatteredpixeldungeon/windows/WndSettings.java` and remove or comment out the lines that add the language picker UI components (specifically `add( langs );` and `add( langsTab );`).

Verify that your changes compile and run without errors. Do not make any changes to the English `.properties` files.
```

---

## Agent 2: Items & Plants (Equipment & Consumables)
**Objective:** Rewrite all in-game text related to items and plants to fit the new Janitorial/Factory aesthetic.

**Prompt for the Agent:**
```

### QA Feedback / Adjustments
- **Inconsistencies Found:** There are hundreds of lingering references to `wands`, `rings`, `armor`, `weapon`, `scroll`, `potion`, `sword`, `gold`, and `coins` across item properties.
- **Action Required:** Ensure *all* classic RPG terms are completely replaced with factory/janitorial equivalents (e.g., `wand` -> `tool`, `ring` -> `badge`, `scroll` -> `form/manual`, `potion` -> `spray/drink`, `armor` -> `PPE/coveralls`, `gold` -> `company scrip/overtime pay`).
You are a creative writer and expert software engineer tasked with modding the text of a game (Shattered Pixel Dungeon). The goal is to change the game's aesthetic to a lighthearted survival horror set in a chaotic ball bearing factory.

Please read the "Global Context & Lore" carefully before starting.

Your specific domain is **Items and Plants**.
Target Directories:
- `core/src/main/assets/messages/items/`
- `core/src/main/assets/messages/plants/`

Instructions:
1. Open the base English `.properties` files in these directories (e.g., `items.properties`, `plants.properties`). Do NOT touch files with language codes.
2. Rewrite the names and descriptions of all entries to fit the factory janitorial setting.
   - Example 1: Change "Sword" or "Dagger" to "Heavy-Duty Mop" or "Pipe Wrench".
   - Example 2: Change "Health Potion" to "First-Aid Spray" or "Energy Drink".
   - Example 3: Change "Scroll of Upgrade" to "Equipment Requisition Form" or "Maintenance Manual".
   - Example 4: Change plants/seeds to various chemical spills, molds, or specialized cleaning compounds.
3. Maintain the original formatting, placeholders (like `%s` or `%d`), and keys within the `.properties` files. Only change the values (the text after the `=` sign).
4. Keep the descriptions engaging, cohesive with the janitorial lore, and ensure they accurately reflect what the item does mechanically.

Make sure you do not alter files outside of your target directories.
```

---

## Agent 3: Actors (Characters, Enemies, & NPCs)
**Objective:** Rewrite all in-game text related to the player characters, enemies, and NPCs to fit the mutated factory worker and janitorial crew theme.

**Prompt for the Agent:**
```

### QA Feedback / Adjustments
- **Inconsistencies Found:** There are over 700 lingering references to `hero` and dozens of references to `warrior`, `mage`, `rogue`, `huntress`, `duelist`, and `cleric`. The names were partially changed (e.g. 'Heavy-Duty Janitor' is used sometimes, but 'Warrior' is still used elsewhere). There are also remaining references to `magic`.
- **Action Required:** Do a rigorous find-and-replace to ensure *every single instance* of `hero` is changed to something like `janitor` or `worker`, and *every instance* of the classic class names (Warrior, Mage, Rogue, Huntress, Duelist, Cleric) is replaced with your chosen factory equivalents (e.g. Heavy-Duty Janitor, Hazmat Technician, Aging Custodian, etc.). Eliminate all mentions of `magic` (replace with `anti-friction tech`, `chemical`, etc.).
You are a creative writer and expert software engineer tasked with modding the text of a game (Shattered Pixel Dungeon). The goal is to change the game's aesthetic to a lighthearted survival horror set in a chaotic ball bearing factory.

Please read the "Global Context & Lore" carefully before starting.

Your specific domain is **Actors** (Enemies, NPCs, and Player Classes).
Target Directory:
- `core/src/main/assets/messages/actors/`

Instructions:
1. Open the base English `.properties` files in this directory. Do NOT touch files with language codes.
2. Rewrite the names and descriptions of all entities to fit the factory setting.
   - Example 1: Change basic enemies like "Rat" to "Mutated Lab Rat" or "Rogue Roomba".
   - Example 2: Change mid-tier enemies like "Gnoll" or "Skeleton" to "Toxic Shift Worker" or "Corrupted Foreman".
   - Example 3: Change "Shopkeeper" to "Vending Machine Dispenser" or "Cynical Union Rep".
   - Example 4: Change Player Classes (Warrior, Mage, Rogue, Huntress) to variations of the Janitorial Crew (e.g., "Rookie Sweeper", "Bio-Hazard Tech", "Aging Custodian").
3. Maintain the original formatting, placeholders (like `%s` or `%d`), and keys within the `.properties` files. Only change the values.
4. Keep the descriptions engaging, slightly humorous but creepy, and build a consistent factory universe.

Make sure you do not alter files outside of your target directory.
```

---

## Agent 4: Environment & Lore (Levels, Journal, & Scenes)
**Objective:** Rewrite the setting descriptions, lore notes, story scenes, and level names to establish the shifting factory environments and the backstory of the infinite precision ball bearing.

**Prompt for the Agent:**
```

### QA Feedback / Adjustments
- **Inconsistencies Found:** The lore still heavily relies on words like `dungeon`, `descend` (violates horizontal spatial layout lore), `amulet of yendor`, and classic level names like `sewer`, `prison`, `cave`, and `city`.
- **Action Required:** Remove all references to `dungeon` (use `factory` or `facility`), `descend`/`go down` (use `proceed to the next sector`, `move laterally`), and `amulet of yendor` (use `ultimate ball bearing` or `infinite precision ball bearing`). Ensure all level lore and journal entries strictly adhere to the factory departments (Offices, Screw Machine Dept, Grind Dept, etc.) and lateral progression.
You are a creative writer and expert software engineer tasked with modding the text of a game (Shattered Pixel Dungeon). The goal is to change the game's aesthetic to a lighthearted survival horror set in a chaotic ball bearing factory.

Please read the "Global Context & Lore" carefully before starting.

Your specific domain is **Environment & Lore**.
Target Directories:
- `core/src/main/assets/messages/levels/`
- `core/src/main/assets/messages/journal/`
- `core/src/main/assets/messages/scenes/`

Instructions:
1. Open the base English `.properties` files in these directories. Do NOT touch files with language codes.
2. Rewrite the environment names, scene text, and journal lore to fit the factory setting.
   - Example 1: Change "The Sewers" to "Break Rooms & Offices" or "Supply Depots".
   - Example 2: Change deeper levels like "The Prison" or "The City" to "Screw Machine Dept", "Grind Dept", "Heat-Treat", or "Assembly".
   - Example 3: Update journal entries from ancient magical lore to misplaced memos, warning labels, shift logs, and frantic notes from scientists discovering the space-time rifts caused by the "ultimate ball bearing".
3. Maintain the original formatting, placeholders (like `%s` or `%d`), and keys within the `.properties` files. Only change the values.
4. Ensure the narrative flows logically, capturing the mundane surface transitioning into the bizarre, dimension-shifting depths of the factory.

Make sure you do not alter files outside of your target directories.
```

---

## Agent 5: UI & Misc (User Interface, Windows, & System Text)
**Objective:** Update the user interface text, system messages, and window prompts to sound like a janitor's logbook, a factory PA system, or an employee handbook.

**Prompt for the Agent:**
```

### QA Feedback / Adjustments
- **Inconsistencies Found:** UI and windows still contain references to `hero`, `gold`, `scroll`, `armor`, `weapon`, `magic`, and `dungeon`.
- **Action Required:** Standardize the UI text to match the new terminology from Agents 2, 3, and 4. `Hero` must become `Janitor`, `Gold` must become `Company Scrip` or `Overtime Pay`, `Dungeon` must become `Factory`, and equipment tabs/prompts must use factory equivalents (`PPE`, `Tools`, `Forms`, `Sprays`).
You are a creative writer and expert software engineer tasked with modding the text of a game (Shattered Pixel Dungeon). The goal is to change the game's aesthetic to a lighthearted survival horror set in a chaotic ball bearing factory.

Please read the "Global Context & Lore" carefully before starting.

Your specific domain is **UI & Misc**.
Target Directories:
- `core/src/main/assets/messages/ui/`
- `core/src/main/assets/messages/windows/`
- `core/src/main/assets/messages/misc/`

Instructions:
1. Open the base English `.properties` files in these directories. Do NOT touch files with language codes.
2. Rewrite the UI elements, system messages, and window text to fit a factory/janitorial interface.
   - Example 1: Change "Magic Mapping" to "Reviewing Facility Blueprint".
   - Example 2: Change "Cast Spell" to "Apply Solvent" or "Use Equipment".
   - Example 3: Change "Inventory" to "Utility Cart" or "Toolbelt".
   - Example 4: Change level-up or resting messages to "Taking a Union-Mandated Break" or "Earning Overtime Pay".
3. Maintain the original formatting, placeholders (like `%s` or `%d`), and keys within the `.properties` files. Only change the values.
4. Ensure the new terminology is intuitive so the player still understands how to play the game, while keeping the lighthearted, bureaucratic factory tone.

Make sure you do not alter files outside of your target directories.
```