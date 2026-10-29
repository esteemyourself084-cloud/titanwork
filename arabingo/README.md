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

- **Learn**: the original layout, with levels, unit tiles and progress. On a topic page the explanation sits in its
  own panel and the examples are cards in a grid; a question and its reply show as a two-card dialogue.
- **Tests** mix multiple choice with drag-to-box questions: drag four Arabic words into the boxes with their
  meanings, or four meanings into the boxes with the Arabic (tap a card and then a box also works).
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
- **3D**: the fight, the shop's champion and the arena lobby are drawn in 3D with Three.js r128 (loaded from
  cdnjs): a lit arena with shadows, a cheering crowd, torches, banners and props for each battlefield; a 3D
  champion built from the equipped character, armour, weapon and mount; 3D creatures; sword trails, sparks,
  camera shake and hit flashes. Without WebGL, or if the script cannot load, the 2D drawings are used.
- **Arena fight (3D)**: an action fight, best of three rounds of 60 seconds. Move freely around the arena
  (WASD or arrows; or hold the mouse button and point; on a phone, drag on the left of the screen for a
  joystick). The camera follows behind you and keeps the creature in view. The creature chases you, circles and
  winds up attacks marked on the ground: a red cone (swipe; block it or step out), a red circle (pounce; get out),
  a lane (charge) and a long cone (fire breath). Roll through an attack (Space or the Roll button) and it is left
  open for a counter. J or a click attacks (three hits make a combo), K or a right click is a heavy attack that
  breaks a guard and stops a wind-up, L is the special, Shift blocks.
- **Opponents**: 40 creatures and 8 human fighters (the Thief, the Highwayman, the Raider Archer, the Mercenary,
  the Swordswoman, the Black Knight, the Raider Chief and, last, the Arena Champion), dressed in the shop's gear.
- **Fight moves**: attacks home in on the target; light attacks chain into a four-hit combo with a finisher;
  every hit has a short freeze-frame and makes the enemy flinch; block just before a blow to parry it; a roll at the
  last moment is a perfect dodge with slow motion; tougher enemies chain attacks and answer button-mashing with a
  shockwave; archers keep their distance and shoot along a marked lane.
  - **Sword control on touch screens**: drag on the left half to move; on the right half the sword follows your
    finger, and a swipe swings it that way: across for a cut, down for a chop (breaks a guard, interrupts and lands
    criticals on a staggered enemy) or up for an uppercut. A faster swipe hits harder, changing direction from one
    swipe to the next builds a combo, and the fourth is a finisher. A tap is a quick attack. With a mouse, flick it
    while holding the button to slash.
  - **Stamina** (the green bar under Special): rolls and blocked blows use it, and it refills when you rest.
    Run out and you can't roll ("Tired!"), and a blocked blow breaks your guard.
  - **Charged heavy**: hold K, right-click or the Heavy button; the longer you hold (up to about a second),
    the harder it hits and the further it knocks the enemy back.
  - **Roll-cancel and dash**: a roll cancels an attack once its blow has landed; attack right after a roll for
    a dash strike.
  - **Poise** (the yellow bar under the enemy's health): every hit wears it down, parries a lot. When it breaks
    the enemy is staggered, and a heavy blow or a combo finisher then lands a critical (2.6× damage).
  - **Enraged**: from the third opponent on, an enemy below 40% health roars once and fights faster. It chains
    more attacks, shrugs off light hits and uses a shockwave.
  - **Feints**: from the fifth opponent on, some wind-ups stop halfway and restart, to catch early rolls.
  - **Knockdowns**: slams and charges knock you down (you can't be hit while down); press roll to get up
    sooner. Enemies punish a long block with a slam, and a slow charge with a quick attack. The fight can go full screen.
- **Graphics quality** (the button next to full screen): **Epic** draws up to about 3.7 million pixels (1440p level)
  with 4096 shadows, glow (bloom), sky reflections on metal and cloth, 4x anti-aliasing and colour grading;
  **High** is the same at up to about 2.1 million pixels with 2048 shadows; **Fast** has no glow or reflections
  and up to about 1 million pixels. On a phone, Epic and High use every pixel of the screen. Until you pick one, a
  slow device steps down by itself after the first few seconds. The choice is kept on the device. Models use
  smoother shapes, and the arena floor and walls use sharper, bump-mapped textures.
- **Arena fight (2D)**: without WebGL the earlier fight is used: dodge left or right at the last moment, block,
  light, heavy and special, with the buttons under the fight.

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

Another chat also edits the published page, so `index.html` is merged with each newly published version
(a three-way merge from the version both started from). The scripts below rebuilt an earlier stage of the page: `tools/build/build_fight.py`
(new swords, items, the fight and the skin, from the other files in `tools/build`), then `rearfix.py` (the champion
seen from behind), `learnfix.py` (lesson cards and drag-to-box questions) and `g3fix.py` (adds `arena3d.js`).

Other tools: `tools/dump_level.py` prints a level for review, and `tools/audit_content.py` runs automatic
checks on the Arabic.

## Versions

- **1.0**: `versions/arabingo-1.0.html` (git tag `arabingo-v1.0`) is the app as it was before the move to Full HD
  level 3D (up to about 1.6 million pixels). It opens on its own, like `index.html`.
