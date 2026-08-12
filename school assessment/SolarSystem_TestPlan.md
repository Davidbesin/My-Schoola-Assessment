# Test Plan — Solar System Explorer (Tkinter App)

## 1. Overview

**Application:** `GUI.py` + supporting modules `Planets.py`, `Lists.py`, `Query.py`
**Purpose:** A Tkinter desktop app that lets a user browse planet name/mass/distance/moon data via menu buttons, and ask free-text questions about planets via a query box based on keywords.

**Modules:**
| Module | Responsibility |
|---|---|
| `Planets.py` | Static data (`Planet` class + `planets` list) |
| `Lists.py` | Keyword lists used for free-text query matching--Asked ai to generate the list of possible |
| `Query.py` | Parses a free-text query into a `QueryInfo` object and builds an answer string |
| `GUI.py` | Tkinter UI: menu navigation + query box wiring |

## 2. Scope

**In scope:**

- Unit-level correctness of `Query.py` parsing/answer logic
- Data integrity of `Planets.py`
- Manual/exploratory UI testing of `GUI.py` (menu navigation, back buttons, query box and answer box)

## 3. Test Environment

- Python 3.x, standard library only (`tkinter`, `os`) — no extra dependencies to install
- Requires `SolarSystem.png` present alongside `GUI.py` (app calls `PhotoImage` on a hardcoded relative path

### 4.1 `get_planet_name(query)`

| #   | Input                          | Expected         | Notes                                                                                                                                             |
| --- | ------------------------------ | ---------------- | ------------------------------------------------------------------------------------------------------------------------------------------------- |
| 1   | `"what is the mass of earth"`  | `"Earth"`        | case-insensitive match                                                                                                                            |
| 2   | `"MERCURY mass"`               | `"Mercury"`      | all-caps input                                                                                                                                    |
| 3   | `"tell me about earth's moon"` | `"Earth"`        | trailing punctuation (`'s`) stripped                                                                                                              |
| 4   | `"asdkjasd"`                   | `None`           | no planet found                                                                                                                                   |
| 5   | `"Earth Mars distance"`        | `"Earth"` (only) | **defect/limitation**: only the first matching planet in the sentence is returned; a two-planet comparison query silently drops the second planet |
| 6   | `"Earth Earth distance"`       | `"Earth"` (only) | **defect/limitation**: only the first matching planet in the sentence is returned; a two-planet comparison query silently drops the second planet |
| 7   | `""` (empty string)            | `None`           | empty query                                                                                                                                       |



### 4.2 `get_mass(query)`

| #   | Input                    | Expected                  |
| --- | ------------------------ | ------------------------- |
| 1   | `"how heavy is jupiter"` | `True`                    |
| 2   | `"how far is mars"`      | `False`                   |
| 3   | `"MASS of Venus"`        | `True` (case-insensitive) |

### 4.3 `get_distance(query)`

| #   | Input                            | Expected |
| --- | -------------------------------- | -------- |
| 1   | `"how far is mars from the sun"` | `True`   |
| 2   | `"what is Saturn's mass"`        | `False`  |

### 4.4 `get_moons(query)`

| #   | Input                               | Expected | Notes |
| --- | ----------------------------------- | -------- | ----- |
| 1   | `"how many moons does Saturn have"` | `True`   |       |
| 2   | `"does venus have any moons"`       | `True`   |       |

### 4.5 `get_every_info(query)`

| #   | Input                                | Expected |
| --- | ------------------------------------ | -------- |
| 1   | `"tell me everything about Jupiter"` | `True`   |
| 2   | `"mass of Mars"`                     | `False`  |

### 4.6 `QueryInfo.get_answer()` — integration of the above

| #   | Input                                          | Expected behavior                                                                                                                     |
| --- | ---------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------- |
| 1   | `"tell me everything about Jupiter"`           | Returns mass + distance + moons, all in one string                                                                                    |
| 2   | `"asdkjasd"`                                   | `"I couldn't figure out which planet you're asking about."`                                                                           |
| 3   | `"Pluto mass"`                                 | Same "couldn't figure out" message (Pluto not in `planets`) — confirms graceful handling of non-modeled planets                       |
| 4   | `"Earth"` (planet named, no attribute keyword) | `"I found Earth, but I'm not sure what you want to know about it."`                                                                   |
| 5   | `"how many rings does Saturn have"`            | Currently falls into the "not sure what you want" branch — flag against expected UX (user probably expects a moon-count-style answer) |



## 5. Data Validation — `Planets.py`

| #   | Check                                                       | Expected                                        |
| --- | ----------------------------------------------------------- | ----------------------------------------------- |
| 1   | All 8 planets present, correct order (Mercury → Neptune)    | Pass                                            |
| 2   | `mass` and `distance` are positive numbers for every planet | Pass                                            |
| 3   | `moons` is a list (possibly empty) for every planet         | Pass                                            |
| 4   | Mercury and Venus have empty moons` lists                   | Pass (matches GUI's hardcoded "0 moons" labels) |

## 6. Manual/Exploratory Test Cases — `GUI.py`

### 6.1 Startup

| #   | Steps                                                             | Expected                                                                                  |
| --- | ----------------------------------------------------------------- | ----------------------------------------------------------------------------------------- |
| 1   | Launch `GUI.py` with `SolarSystem.png` present in the same folder | Window opens maximized, background image and credit label visible, 4 menu buttons visible |
| 2   | Launch with `SolarSystem.png` missing/renamed                     | With try and except, it can run wiithout background image                                 |

### 6.2 Menu navigation (repeat for each of the 4 submenus: Name / Mass / Distance / Moons)

| #   | Steps                                                                    | Expected                                                           |
| --- | ------------------------------------------------------------------------ | ------------------------------------------------------------------ |
| 1   | Click submenu button from main menu                                      | Main menu buttons disappear; 8 planet rows + back arrow appear     |
| 2   | Click back arrow (`<-`)                                                  | Submenu widgets disappear; main menu buttons reappear              |
| 3   | Navigate into each of the 4 submenus and back at least once, in sequence | No leftover/duplicate widgets, no overlap                          |
| 4   | Resize window / check on different screen resolutions                    | Layout (relx/rely percentages) still readable, no overlapping text |

### 6.3 Moons submenu specifics

| #   | Steps              | Expected                                                                                 | Notes |
| --- | ------------------ | ---------------------------------------------------------------------------------------- | ----- |
| 1   | Open Moons submenu | Mercury and Venus rows read "has 0 moons"; Earth onward read "The Moons of X is/are ..." |       |

### 6.4 Query box

| #   | Steps                                                    | Expected                                                                                                                                        |
| --- | -------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------- |
| 1   | Type `"mass of earth"`, click Enter                      | Output label shows Earth's mass string                                                                                                          |
| 2   | Type `""` (empty) and click Enter                        | Output label shows "I couldn't figure out..." — verify no crash on empty input                                                                  |
| 3   | Type a query, click Enter, verify the input field clears | Entry field is emptied after submit                                                                                                             |
| 4   | Type a very long query (200+ chars)                      | Output label displays without breaking layout (label has fixed relwidth — check for text overflow/clipping)                                     |
| 5   | Submit multiple queries in a row                         | Output label correctly replaces previous answer each time, no stacking/duplication                                                              |
| 6   | Query while a submenu (not main menu) is open            | Query box is always visible/enabled regardless of submenu state — confirm this is intended, since it's placed independently of the button lists |






