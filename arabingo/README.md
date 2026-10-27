# Arabingo

Arabic-learning app: stages → levels → themes → small units, with lessons, quick checks, unit tests,
level and stage tests, conversations, a reading room, a word bank with flashcards, a shop and an arena.

Published artifact: https://claude.ai/artifact/T3ehfd5MLocuet6CnFHqYh

## Course structure

- Every unit teaches **at most 2 topics** (lessons). Each level holds **15–20 topics**.
- The original 69 large units were split into **165 small units across 17 levels**:
  - **Stage 1 · Beginner** (levels 1–9): the original levels 1–3.
  - **Stage 2 · Intermediate** (levels 1–8): the original levels 4–7. These levels open with the passive,
    verbal nouns and participles.
- Each original unit became a **theme**. Its small units stay together on the Learn page, and the theme's
  conversation is the test at the end of its last unit.
- Levels made from the original levels 3–7 end with a **review unit**. A review unit holds recap pages, not
  new topics.
- Words and questions were moved to the small unit that teaches them. No lessons, words (1,417) or
  questions (1,963) were dropped.

## Pages

- **Learn**: levels grouped by theme, with topic and unit counts, progress and a "next up" card. Each unit
  runs Intro → Topic 1 → Topic 2 → Words → Test, and every topic ends with a quick check.
- **Reading**: all 68 conversations as reading passages. Tap any word to look it up in the word bank. You
  can turn the vowel marks on or off, change the text size, listen to the whole dialogue, and answer
  comprehension questions for XP.
- **Quiz**: "Practise your mistakes" (wrong answers are saved), "Quick review", and the level road with
  level and stage tests. Longer answers get 15–20 seconds instead of 10.
- **Shop**: shaded SVG art for every weapon, armour, mount and character, rarity tiers, stat bars, and a
  showcase of your fighter on a pedestal.
- **Arena**: an illustrated arena, drawn enemies, an HP display, hit effects (slash, claws, sting, fire),
  knock-outs, and enemies that unlock in order.

`REVIEW = true` in the script unlocks every unit and stage and shows the "+1000 XP" button for testing.

## Data and progress

- Progress is stored in `localStorage` (`arabingo.progress.v3`), and synced to `data/users/{uid}/progress3`
  when the app runs as an artifact. Progress saved before the split (`progress.v2` / `progress2`) is moved
  onto the new units automatically, using `OLDMAP` and `LVMAP` in the page.
- Runtime capabilities when hosted as an artifact: `db`, `downloads`, `sample`, `user`.

## Tools

```sh
# rebuild the course from the original SEED (taken from the commit before the restructure)
git show a5fad0d:arabingo/index.html | sed -n 's/^var SEED=//p' | sed 's/;$//' > /tmp/seed-original.json
python3 tools/restructure.py /tmp/seed-original.json /tmp/new.json
python3 tools/splice_seed.py index.html /tmp/new.json

# check the course rules (≤2 topics per unit, 15–20 topics per level)
python3 tools/check_course.py index.html

# end-to-end browser checks (needs Playwright)
node tools/e2e.js "$PWD/index.html"
```
