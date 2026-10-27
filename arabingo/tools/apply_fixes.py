#!/usr/bin/env python3
"""Apply the content corrections in tools/fixes/*.py (or .json) to a restructured course.

usage: python3 tools/apply_fixes.py new.json tools/fixes fixed.json

Each fixes file is a JSON list of operations. Indexes count from 1, as printed by dump_level.py,
and refer to the course as restructure.py produces it (before any fix).
  {"u": "1-2-5", "set": {"about": "..."}}                      unit fields
  {"u": "1-2-5", "r": 1, "set": {"title": "...", "body": "..."}}  lesson fields
  {"u": "1-2-5", "r": 1, "e": 3, "was": "هَذَا أَبٌ", "set": {"en": "..."}}   example fields
  {"u": "1-2-5", "r": 1, "e": 3, "del": true, "was": "..."}       remove an example
  {"u": "1-2-5", "r": 1, "add": {"ar": "...", "tr": "...", "en": "...", "note": "..."}}  new example
  {"u": "1-2-5", "w": 2, "was": "أَبٌ", "set": {"pl": "..."}}       word fields (was = Arabic)
  {"u": "1-2-5", "w": 0, "add": {"ar": "...", "pl": "", "en": "...", "type": "noun"}}
  {"u": "1-2-5", "q": 4, "was": "question text", "set": {"a": "...", "w": ["...", "..."]}}
  {"u": "1-2-5", "q": 4, "del": true, "was": "question text"}
  {"u": "1-2-5", "q": 0, "add": {"q": "...", "a": "...", "w": ["...", "..."]}}
  {"u": "1-2-5", "l": 3, "was": "...", "set": {"ar": "..."}}        conversation line
  {"u": "1-2-5", "cq": 2, "was": "question text", "set": {...}}     conversation question
"was" must equal the current text or be its start; a mismatch stops the run.
A .py file may also define POST(units), which runs after its FIXES for changes across the whole course.
"""
import json
import os
import sys
import textwrap


def fail(op, msg):
    sys.exit('fix failed: %s\n  %s' % (msg, json.dumps(op, ensure_ascii=False)))


def check_was(op, cur):
    w = op.get('was')
    if w is not None and not (cur == w or cur.startswith(w)):
        fail(op, 'expected "%s" but found "%s"' % (w, cur))


def target(units, op):
    u = units.get(op['u']) or fail(op, 'no unit ' + op['u'])
    if 'e' in op or ('r' in op and 'add' in op):
        r = u['rules'][op['r'] - 1]
        if 'add' in op:
            return r['ex'], None, 'ar'
        return r['ex'], op['e'] - 1, 'ar'
    if 'r' in op:
        return u['rules'], op['r'] - 1, 'title'
    if 'w' in op:
        return u['words'], op['w'] - 1, 'ar'
    if 'q' in op:
        return u['qs'], op['q'] - 1, 'q'
    if 'l' in op:
        return u['conv']['lines'], op['l'] - 1, 'ar'
    if 'cq' in op:
        return u['conv']['qs'], op['cq'] - 1, 'q'
    return None, None, None


def apply(units, ops):
    # Edits first, then removals from the back, then additions, so indexes keep their meaning.
    edits = [o for o in ops if 'set' in o]
    dels = [o for o in ops if o.get('del')]
    adds = [o for o in ops if 'add' in o]
    for op in edits:
        lst, i, key = target(units, op)
        if lst is None:
            units[op['u']].update(op['set'])
            continue
        if i >= len(lst):
            fail(op, 'index out of range')
        check_was(op, lst[i].get(key, ''))
        for k, v in op['set'].items():
            if v is None:
                lst[i].pop(k, None)
            else:
                lst[i][k] = v
    for op in sorted(dels, key=lambda o: -max(o.get(k, 0) for k in ('e', 'w', 'q', 'l', 'cq'))):
        lst, i, key = target(units, op)
        check_was(op, lst[i].get(key, ''))
        lst.pop(i)
    for op in adds:
        lst, i, key = target(units, op)
        lst.append(op['add'])


if __name__ == '__main__':
    src, fixdir, dst = sys.argv[1:4]
    data = json.load(open(src, encoding='utf-8'))
    units = {u['id']: u for u in data['units']}
    n = 0
    for name in sorted(os.listdir(fixdir)):
        path = os.path.join(fixdir, name)
        if name.endswith('.json'):
            ops = json.load(open(path, encoding='utf-8'))
        elif name.endswith('.py') and not name.startswith('_'):
            # Python files hold FIXES = [...]; B() tidies multi-line lesson text.
            env = {'B': lambda t: textwrap.dedent(t).strip('\n')}
            exec(compile(open(path, encoding='utf-8').read(), path, 'exec'), env)
            ops = env.get('FIXES', [])
        else:
            continue
        apply(units, ops)
        if name.endswith('.py') and 'POST' in env:
            env['POST'](units)
        n += len(ops)
        print('%-14s %4d fixes' % (name, len(ops)))
    json.dump(data, open(dst, 'w', encoding='utf-8'), ensure_ascii=False, separators=(',', ':'))
    print('applied %d fixes' % n)
