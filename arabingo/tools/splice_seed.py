#!/usr/bin/env python3
"""Write a restructured course (output of restructure.py) into index.html.

Replaces the `var SEED=[...];` line and the `var OLDMAP=...;` line after it.
"""
import json
import sys

html_path, data_path = sys.argv[1], sys.argv[2]
data = json.load(open(data_path, encoding='utf-8'))
lines = open(html_path, encoding='utf-8').read().split('\n')
i = next(k for k, l in enumerate(lines) if l.startswith('var SEED='))
dump = lambda v: json.dumps(v, ensure_ascii=False, separators=(',', ':'))
lines[i] = 'var SEED=' + dump(data['units']) + ';'
maps = 'var OLDMAP=' + dump(data['oldmap']) + ',LVMAP=' + dump(data['lvmap']) + ';'
if lines[i + 1].startswith('var OLDMAP='):
    lines[i + 1] = maps
else:
    lines.insert(i + 1, maps)
open(html_path, 'w', encoding='utf-8').write('\n'.join(lines))
print('SEED: %d units written to line %d' % (len(data['units']), i + 1))
