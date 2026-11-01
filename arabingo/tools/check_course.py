#!/usr/bin/env python3
"""Check the course layout inside index.html.

Every lesson is in Stage 1, a stage has at most 10 levels, and a level has 10 units:
the Introduction first and, from Level 2 on, the level review last.
usage: python3 tools/check_course.py index.html
"""
import json
import re
import sys
from collections import OrderedDict

src = open(sys.argv[1], encoding='utf-8').read()
units = json.loads(re.search(r'^var SEED=(.*);$', src, re.M).group(1))
levels = OrderedDict()
for u in sorted(units, key=lambda u: (u['stage'], u['level'], u['order'])):
    levels.setdefault((u['stage'], u['level']), []).append(u)
errors = []
for (s, l), us in levels.items():
    print('Stage %d Level %d: %2d units, %3d lessons  %s ... %s' % (
        s, l, len(us), sum(len(u['rules']) for u in us), us[0]['titleEn'], us[-1]['titleEn']))
    if s != 1:
        errors.append('stage %d level %d: lessons belong in Stage 1' % (s, l))
    if l > 10:
        errors.append('stage %d has a level %d; a stage has at most 10 levels' % (s, l))
    if len(us) != 10:
        errors.append('stage %d level %d has %d units, not 10' % (s, l, len(us)))
    if not us[0]['titleEn'].startswith('Introduction'):
        errors.append('stage %d level %d does not start with an Introduction' % (s, l))
    if l > 1 and not us[-1].get('review'):
        errors.append('stage %d level %d does not end with a review' % (s, l))
print('%d units, %d lessons' % (len(units), sum(len(u['rules']) for u in units)))
if errors:
    print('\n'.join('ERROR: ' + e for e in errors))
    sys.exit(1)
print('OK: Stage 1 only, 10 units per level, Introduction first and review last')
