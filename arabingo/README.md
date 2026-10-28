# Arabingo

Arabic-learning app: stages → levels → units, with lessons, quick checks, unit tests, level and stage
tests, conversations, a reading room, a word bank with flashcards, a shop and an arena.

Published artifact: https://claude.ai/artifact/T3ehfd5MLocuet6CnFHqYh

## Course layout

- Three stages, ten levels in each stage and ten units in each level, as in the original app.
- All lessons are in **Stage 1 · Beginner**, Levels 1–7. Stages 2 and 3 are empty and show "Coming soon".
- Every level has 10 units. Unit 1 is the Introduction, and from Level 2 on, unit 10 is the level review.
  Level 2 had 9 units, so it gained a review unit built from its own lessons and questions.
- The lesson content has been checked and corrected: grammar errors, wrong translations and facts, stale
  level references, weak quiz options, and thin explanations.

## Pages

- **Learn**: the original layout, with levels, unit tiles and progress.
- **Reading**: the conversations as reading passages. Tap any word to look it up in the word bank, turn the
  vowel marks on or off, listen, and answer questions for XP.
- **Quiz**: "Practise your mistakes", "Quick review", and the level road with level and stage tests.
- **Shop** (the Armory) and **Arena**: a fighting-game look with a dark ember stage, gold metal frames and
  rarity-coloured fighter-select tiles that tilt towards the pointer. All the art is SVG, so it stays sharp at
  any screen resolution.
- **Weapons**: 45, among them the classical sword names, each drawn from its meaning (Dadan, Mishmal, Sadhij,
  Qashib, Dhaliq, Safiha, ʿAdb, Matin, Arqab, Barraq, Lahdham, Batir, Dhakar, Samsam, Rasub, Bariqa, Mufaqqar,
  Daʾir, Dimashqi, Bilarak, Qirdab, Mudharrab, Islit, Husam, Mudajjal and Dhu al-Fiqar), plus the khanjar,
  janbiya, Khatti spear, nabʿ bow, mace, axe and hammer. Some blades have a special effect: fire, poison,
  lightning, gold or a twin strike.
- **Armour** (22), **mounts** (27, including the classic Arabian horse strains and camel breeds) and
  **characters** (30), and 20 battlefields.
- **Arena fight**: real time, best of three rounds of 60 seconds. The creature winds up before it strikes
  (a yellow "!" is a swipe you can block, a red "!!" is a slam you must dodge). Dodge at the last moment and it
  is left open for a counter. Light attacks are quick, heavy attacks break a guard and stop a wind-up, and the
  special fills as you land hits and dodges. Keys: ← → or A D dodge, ↓ or S block, J light, K heavy, L or Space
  special; on a phone, the buttons under the fight.

`REVIEW = true` in the script unlocks every unit and stage and shows the "+1000 XP" button for testing.

## Data and progress

- Progress is stored in `localStorage` (`arabingo.progress.v3`, format version 5) and synced to
  `data/users/{uid}/progress3` when the app runs as an artifact.
- Progress saved while the course was split into small units (format versions 3 and 4) is moved back onto
  the original units with `OLDMAP` and `LVMAP`: a unit counts as done when all its small units were done.
  Progress from the first version of the app keeps its unit ids.

## How the content is built

The corrections in `tools/fixes` address one lesson at a time, so the build splits the original units,
applies the fixes, and joins the units back together:

```sh
SP=/tmp/arabingo; mkdir -p $SP/style
# the original SEED, from the commit before any restructure
git show a5fad0d:arabingo/index.html | sed -n 's/^var SEED=//p' | sed 's/;$//' > $SP/seed.json
python3 tools/restructure.py $SP/seed.json $SP/split.json > /dev/null
python3 tools/apply_fixes.py $SP/split.json tools/fixes $SP/fixed.json
cp tools/fixes/zz_style.py $SP/style/ && python3 tools/apply_fixes.py $SP/split.json $SP/style $SP/styled.json
python3 tools/reassemble.py $SP/seed.json $SP/styled.json $SP/fixed.json $SP/final.json
python3 tools/splice_seed.py index.html $SP/final.json

# check the layout (Stage 1 only, 10 units per level, Introduction first, review last)
python3 tools/check_course.py index.html

# end-to-end browser checks (needs Playwright)
node tools/e2e.js "$PWD/index.html"
```

Other tools: `tools/dump_level.py` prints a level for review, and `tools/audit_content.py` runs automatic
checks on the Arabic.
