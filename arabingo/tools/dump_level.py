#!/usr/bin/env python3
"""Print one level of the course in a compact, reviewable text form.

usage: python3 tools/dump_level.py index.html STAGE LEVEL [--no-qs]
Labels (R1, E3, W2, Q5, L4, CQ2) match the indexes used in tools/fixes/*.json (counted from 1 here).
"""
import json
import re
import sys

src = open(sys.argv[1], encoding='utf-8').read()
units = json.loads(re.search(r'^var SEED=(.*);$', src, re.M).group(1))
stage, level = int(sys.argv[2]), int(sys.argv[3])
no_qs = '--no-qs' in sys.argv
for u in sorted(units, key=lambda u: u['order']):
    if u['stage'] != stage or u['level'] != level:
        continue
    print('=' * 8, u['id'], '|', u['titleEn'], '|', u['titleAr'])
    print('ABOUT:', u['about'])
    for ri, r in enumerate(u['rules'], 1):
        print('--- R%d %s' % (ri, r['title']))
        print(r['body'])
        for ei, e in enumerate(r['ex'], 1):
            print('  E%d%s %s | %s | %s' % (ei, ' (reply)' if e.get('re') else '', e['ar'], e.get('tr', ''), e.get('en', '')))
            if e.get('note'):
                print('      note: ' + e['note'])
    if u['words']:
        print('WORDS: ' + ' ; '.join('W%d %s|%s|%s|%s' % (i, w['ar'], w.get('pl', ''), w['en'], w.get('type', '')) for i, w in enumerate(u['words'], 1)))
    if not no_qs:
        for qi, q in enumerate(u['qs'], 1):
            print('  Q%d %s -> %s  [x %s]' % (qi, q['q'], q['a'], ' / '.join(q['w'])))
        if u.get('conv'):
            c = u['conv']
            print('CONV: ' + c['title'])
            for li, l in enumerate(c['lines'], 1):
                print('  L%d %s %s: %s' % (li, l['w'], l['n'], l['ar']))
            for qi, q in enumerate(c['qs'], 1):
                print('  CQ%d %s -> %s  [x %s]' % (qi, q['q'], q['a'], ' / '.join(q['w'])))
    print()
