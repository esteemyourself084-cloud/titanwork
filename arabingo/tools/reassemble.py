#!/usr/bin/env python3
"""Put the corrected lessons back into the original course layout.

restructure.py splits every original unit into small units so that the content
fixes in tools/fixes can address one lesson at a time. This script joins the
corrected small units back into the original units: Stage 1, Levels 1-7, ten
units per level, with the Introduction first and the level review last.

usage: python3 tools/reassemble.py ORIGINAL.json SPLIT.json FIXED.json OUT.json
  ORIGINAL.json  the original SEED array
  SPLIT.json     restructure.py output before the fixes (for its id map)
  FIXED.json     the same after tools/apply_fixes.py
Output: {"units": [...], "oldmap": {small unit id: [original id]}, "lvmap": {...}}
so that progress saved on the small units carries over.
"""
import json
import re
import sys

ORD_AR = ['الأَوَّلِ', 'الثَّانِي', 'الثَّالِثِ', 'الرَّابِعِ', 'الخَامِسِ', 'السَّادِسِ', 'السَّابِعِ']


def strings(o, out):
    if isinstance(o, str):
        out.add(o)
    elif isinstance(o, dict):
        for v in o.values():
            strings(v, out)
    elif isinstance(o, list):
        for v in o:
            strings(v, out)
    return out


def main(orig_path, split_path, fixed_path, out_path):
    orig = json.load(open(orig_path, encoding='utf-8'))
    split = json.load(open(split_path, encoding='utf-8'))
    fixed = {u['id']: u for u in json.load(open(fixed_path, encoding='utf-8'))['units']}
    parts_of = split['oldmap']
    # level of each small unit -> original level, for "Level N" in corrected text
    lv_of = {}
    for oid, ids in parts_of.items():
        for nid in ids:
            lv_of[int(nid.split('-')[1])] = int(oid.split('-')[1])
    untouched = strings(split['units'], set())

    def relevel(s):
        # Only corrected text uses the split numbering; original text already uses the old one.
        if s in untouched:
            return s
        s = re.sub(r'Levels (\d+) and (\d+)', lambda m: 'Level %d' % lv_of[int(m.group(1))]
                   if lv_of[int(m.group(1))] == lv_of[int(m.group(2))]
                   else 'Levels %d and %d' % (lv_of[int(m.group(1))], lv_of[int(m.group(2))]), s)
        return re.sub(r'\bLevel (\d+)\b', lambda m: 'Level %d' % lv_of.get(int(m.group(1)), int(m.group(1))), s)

    def walk(o):
        if isinstance(o, str):
            return relevel(o)
        if isinstance(o, dict):
            return {k: walk(v) for k, v in o.items()}
        if isinstance(o, list):
            return [walk(v) for v in o]
        return o

    units, back, lvmap = [], {}, {}
    for ou in sorted(orig, key=lambda u: (u['level'], u['order'])):
        parts = [walk(fixed[i]) for i in parts_of[ou['id']]]
        u = {k: ou[k] for k in ('stage', 'level', 'order', 'id', 'titleAr', 'titleEn')}
        u['about'] = parts[0]['about'] if not parts[0].get('review') else ou['about']
        u['rules'] = [r for p in parts for r in p['rules']]
        seen, u['words'] = set(), []
        for p in parts:
            for w in p['words']:
                if w['ar'] not in seen:
                    seen.add(w['ar'])
                    u['words'].append(w)
        u['qs'] = [q for p in parts for q in p['qs']]
        conv = [p['conv'] for p in parts if p.get('conv')]
        if conv:
            u['conv'] = conv[-1]
        if any(p.get('review') for p in parts):
            u['review'] = True
        units.append(u)
        for i in parts_of[ou['id']]:
            back[i] = [ou['id']]
    for k, v in split['lvmap'].items():
        for lt in v:
            lvmap[lt] = [k]
    units += [review_for(units, lv) for lv in (2,)]
    json.dump({'units': units, 'oldmap': back, 'lvmap': lvmap}, open(out_path, 'w', encoding='utf-8'),
              ensure_ascii=False, separators=(',', ':'))
    print('%d units in %d levels' % (len(units), len({u['level'] for u in units})))


def review_for(units, lv):
    """A review unit for a level that had none: one reminder and two questions per unit."""
    us = [u for u in units if u['level'] == lv]
    half = (len(us) + 1) // 2
    rules = []
    for chunk, (a, b) in ((us[:half], (1, half)), (us[half:], (half + 1, len(us)))):
        names = [u['titleEn'].split(': ')[-1].lower() for u in chunk]
        rules.append({
            'title': 'Reminders: ' + ', '.join(names[:-1]) + ' and ' + names[-1],
            'body': 'These are the key patterns from Units %d to %d. Read each one aloud.' % (a, b),
            'ex': [dict(u['rules'][0]['ex'][0]) for u in chunk if u['rules'] and u['rules'][0]['ex']],
        })
    qs = [q for u in us for q in u['qs'][:2]]
    return {
        'stage': 1, 'level': lv, 'order': len(us) + 1, 'id': '1-%d-%d' % (lv, len(us) + 1),
        'titleAr': 'مُرَاجَعَةُ المُسْتَوَى ' + ORD_AR[lv - 1], 'titleEn': 'Level %d Review' % lv,
        'about': 'A review of everything in Level %d. Read the reminders, then practise: %s.'
                 % (lv, ', '.join(u['titleEn'].split(': ')[-1].lower() for u in us)),
        'review': True, 'rules': rules, 'words': [], 'qs': qs,
    }


if __name__ == '__main__':
    main(*sys.argv[1:5])
