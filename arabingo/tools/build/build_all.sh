#!/bin/sh
# Rebuild index.html from a published page: the new items, the fight and the skin, the back view,
# the lesson cards and drag questions, then the 3D. usage: tools/build/build_all.sh BASE.html
set -e
D=$(dirname "$0")
python3 "$D/build_fight.py" "$D" "$1"
python3 "$D/rearfix.py" index.html
python3 "$D/learnfix.py" index.html
python3 "$D/g3fix.py" index.html
