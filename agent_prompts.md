# Shattered Pixel Dungeon Sci-Fi Mod - Agent Prompts (Stage 1: Text)

To accomplish the first stage of transforming the game's text into a modern/industrial/sci-fi aesthetic, we will divide the work among **5 agents**. Each agent will handle a distinct category of files, ensuring no overlap in their work.

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
**Objective:** Rewrite all in-game text related to items and plants to fit the new modern/industrial/sci-fi aesthetic.

**Prompt for the Agent:**
```
You are a creative writer and expert software engineer tasked with modding the text of a game (Shattered Pixel Dungeon). The goal is to change the game's aesthetic from magical/fantasy to modern/industrial/sci-fi.

Your specific domain is **Items and Plants**.
Target Directories:
- `core/src/main/assets/messages/items/`
- `core/src/main/assets/messages/plants/`

Instructions:
1. Open the base English `.properties` files in these directories (e.g., `items.properties`, `plants.properties`). Do NOT touch files with language codes (e.g., `_ru`, `_es`).
2. Rewrite the names and descriptions of all entries to fit a sci-fi/industrial setting.
   - Example 1: Change "Sword" to "Plasma Cutter" or "Vibro-blade".
   - Example 2: Change "Health Potion" to "Med-Stim" or "Nanite Injector".
   - Example 3: Change "Scroll of Upgrade" to "Firmware Update" or "Overclock Module".
   - Example 4: Change "Firebloom" to "Incendiary Charge" or "Thermite Trap".
3. Maintain the original formatting, placeholders (like `%s` or `%d`), and keys within the `.properties` files. Only change the values (the text after the `=` sign).
4. Keep the descriptions engaging, cohesive with a unified sci-fi lore, and ensure they accurately reflect what the item does mechanically.

Make sure you do not alter files outside of your target directories.
```

---

## Agent 3: Actors (Characters, Enemies, & NPCs)
**Objective:** Rewrite all in-game text related to the player characters, enemies, and NPCs to fit the new modern/industrial/sci-fi aesthetic.

**Prompt for the Agent:**
```
You are a creative writer and expert software engineer tasked with modding the text of a game (Shattered Pixel Dungeon). The goal is to change the game's aesthetic from magical/fantasy to modern/industrial/sci-fi.

Your specific domain is **Actors** (Enemies, NPCs, and Player Classes).
Target Directory:
- `core/src/main/assets/messages/actors/`

Instructions:
1. Open the base English `.properties` files in this directory (e.g., `actors.properties`). Do NOT touch files with language codes.
2. Rewrite the names and descriptions of all entities to fit a sci-fi/industrial setting.
   - Example 1: Change "Rat" to "Maintenance Drone" or "Scrap-Bot".
   - Example 2: Change "Goblin" to "Mutant Scavenger" or "Rogue Android".
   - Example 3: Change "Shopkeeper" to "Quartermaster" or "Black Market Vendor".
   - Example 4: Change "Mage" (player class) to "Technician" or "Hacker".
3. Maintain the original formatting, placeholders (like `%s` or `%d`), and keys within the `.properties` files. Only change the values.
4. Keep the descriptions engaging and ensure they build a consistent sci-fi universe.

Make sure you do not alter files outside of your target directory.
```

---

## Agent 4: Environment & Lore (Levels, Journal, & Scenes)
**Objective:** Rewrite the setting descriptions, lore notes, story scenes, and level names to establish the modern/industrial/sci-fi world.

**Prompt for the Agent:**
```
You are a creative writer and expert software engineer tasked with modding the text of a game (Shattered Pixel Dungeon). The goal is to change the game's aesthetic from magical/fantasy to modern/industrial/sci-fi.

Your specific domain is **Environment & Lore**.
Target Directories:
- `core/src/main/assets/messages/levels/`
- `core/src/main/assets/messages/journal/`
- `core/src/main/assets/messages/scenes/`

Instructions:
1. Open the base English `.properties` files in these directories. Do NOT touch files with language codes.
2. Rewrite the environment names, scene text, and journal lore to fit a sci-fi/industrial setting.
   - Example 1: Change "The Sewers" to "Lower Maintenance Shafts" or "Coolant Tunnels".
   - Example 2: Change "The Prison" to "Detention Block" or "Quarantine Zone".
   - Example 3: Update journal entries from ancient magical lore to logs from scientists, facility managers, or corrupted AI.
3. Maintain the original formatting, placeholders (like `%s` or `%d`), and keys within the `.properties` files. Only change the values.
4. Ensure the narrative flows logically and builds an immersive sci-fi atmosphere.

Make sure you do not alter files outside of your target directories.
```

---

## Agent 5: UI & Misc (User Interface, Windows, & System Text)
**Objective:** Update the user interface text, system messages, and window prompts to sound like a futuristic OS or heads-up display (HUD).

**Prompt for the Agent:**
```
You are a creative writer and expert software engineer tasked with modding the text of a game (Shattered Pixel Dungeon). The goal is to change the game's aesthetic from magical/fantasy to modern/industrial/sci-fi.

Your specific domain is **UI & Misc**.
Target Directories:
- `core/src/main/assets/messages/ui/`
- `core/src/main/assets/messages/windows/`
- `core/src/main/assets/messages/misc/`

Instructions:
1. Open the base English `.properties` files in these directories. Do NOT touch files with language codes.
2. Rewrite the UI elements, system messages, and window text to fit a sci-fi/industrial HUD or OS interface.
   - Example 1: Change "Magic Mapping" to "Area Scan Complete".
   - Example 2: Change "Cast Spell" to "Deploy Ability" or "Execute Routine".
   - Example 3: Change "Inventory" to "Cargo" or "Storage Matrix".
3. Maintain the original formatting, placeholders (like `%s` or `%d`), and keys within the `.properties` files. Only change the values.
4. Ensure the new terminology is intuitive so the player still understands how to play the game, but clearly reflects a futuristic setting.

Make sure you do not alter files outside of your target directories.
```
