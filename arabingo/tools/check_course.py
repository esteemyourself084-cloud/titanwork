#!/usr/bin/env python3
"""Check the course inside index.html: at most 2 topics per unit, 15-20 topics per level.

Review units hold recap pages, not new topics, so they are not counted.
usage: python3 tools/check_course.py index.html
"""
import json
import re
import sys
from collections import OrderedDict

src = open(sys.argv[1], encoding='utf-8').read()
units = json.loads(re.search(r'^var SEED=(.*);$', src, re.M).group(1))
levels = OrderedDict()
errors = []
for u in sorted(units, key=lambda u: (u['stage'], u['level'], u['order'])):
    key = (u['stage'], u['level'])
    lv = levels.setdefault(key, {'topics': 0, 'units': 0})
    lv['units'] += 1
    if len(u['rules']) > 2:
        errors.append('%s has %d %s' % (u['id'], len(u['rules']), 'recap pages' if u.get('review') else 'topics'))
    if not u.get('review'):
        lv['topics'] += len(u['rules'])
for (s, l), lv in levels.items():
    ok = 15 <= lv['topics'] <= 20
    print('Stage %d Level %d: %2d topics in %2d units %s' % (s, l, lv['topics'], lv['units'], '' if ok else '  <-- out of range'))
    if not ok:
        errors.append('stage %d level %d has %d topics' % (s, l, lv['topics']))
print('%d units, %d topics' % (len(units), sum(v['topics'] for v in levels.values())))
if errors:
    print('\n'.join('ERROR: ' + e for e in errors))
    sys.exit(1)
print('OK: every unit has at most 2 topics and every level has 15-20 topics')
