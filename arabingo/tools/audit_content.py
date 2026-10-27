#!/usr/bin/env python3
"""Find likely mistakes in the course content inside index.html.

usage: python3 tools/audit_content.py index.html [--all]
Prints one line per finding: CHECK | unit id | where | text
"""
import json
import re
import sys
from collections import Counter, defaultdict

HARAKA = 'ًٌٍَُِّْ'
TANWEEN = 'ًٌٍ'
SUN = 'تثدذرزسشصضطظلن'
AR_WORD = re.compile('[ء-يً-ْٰـ]+')

src = open(sys.argv[1], encoding='utf-8').read()
units = json.loads(re.search(r'^var SEED=(.*);$', src, re.M).group(1))
show_all = '--all' in sys.argv
out = []


def add(check, uid, where, text):
    out.append((check, uid, where, text))


def letters(w):
    return re.sub('[^ء-ي]', '', w)


def strip_prefix(w):
    """Remove a leading wa/fa/bi/li/ka so the article check sees the noun."""
    for p in ('وَ', 'فَ', 'بِ', 'لِ', 'كَ', 'وَبِ', 'وَلِ'):
        if w.startswith(p) and len(letters(w[len(p):])) >= 3:
            return w[len(p):]
    return w


def check_arabic(uid, where, text, vocalised=True):
    for w in AR_WORD.findall(text or ''):
        bare = letters(w)
        if len(bare) < 2:
            continue
        core = strip_prefix(w)
        # the definite article never takes tanween
        if re.match('^ال', core) and core[-1:] in TANWEEN and len(letters(core)) > 3:
            add('AL+TANWEEN', uid, where, w)
        # a sun letter after al- is doubled: الشَّمْسُ
        m = re.match('^ال([' + SUN + '])([' + HARAKA + ']*)', core)
        if vocalised and m and m.group(1) != 'ل' and 'ّ' not in m.group(2) and re.search('[' + HARAKA + ']', core):
            add('SUN-NO-SHADDA', uid, where, w)
        # fathatan is written on the letter before alif (ـًا), as everywhere else in the course
        if 'اً' in w:
            add('TANWEEN-ON-ALIF', uid, where, w)
        # a vocalised text with a long word that has no vowel marks at all
        if vocalised and len(bare) >= 3 and not re.search('[' + HARAKA + ']', w) and bare not in ('الله', 'اللهم'):
            add('NO-HARAKAT', uid, where, w)
        # two vowels on one letter
        if re.search('[َُِ][َُِ]', w):
            add('DOUBLE-VOWEL', uid, where, w)


TR_MAP = {'ب': 'b', 'ت': 't', 'ث': 'th', 'ج': 'j', 'ح': 'ḥ', 'خ': 'kh', 'د': 'd', 'ذ': 'dh', 'ر': 'r', 'ز': 'z',
          'س': 's', 'ش': 'sh', 'ص': 'ṣ', 'ض': 'ḍ', 'ط': 'ṭ', 'ظ': 'ẓ', 'ع': 'ʿ', 'غ': 'gh', 'ف': 'f', 'ق': 'q',
          'ك': 'k', 'ل': 'l', 'م': 'm', 'ن': 'n', 'ه': 'h'}


def consonants_ar(text):
    return ''.join(TR_MAP.get(c, '') for c in text if c in TR_MAP)


def consonants_tr(tr):
    t = tr.lower()
    for a, b in (('th', 'θ'), ('dh', 'δ'), ('kh', 'χ'), ('sh', 'ʃ'), ('gh', 'ɣ')):
        t = t.replace(a, b)
    keep = 'btθjḥχdδrzsʃṣḍṭẓʿɣfqklmnh'
    out = ''.join(c for c in t if c in keep)
    for a, b in (('θ', 'th'), ('δ', 'dh'), ('χ', 'kh'), ('ʃ', 'sh'), ('ɣ', 'gh')):
        out = out.replace(a, b)
    return out


def tr_mismatch(ar, tr):
    """Rough check that a transliteration spells the same consonants as the Arabic."""
    a = re.sub(r'(.)\1+', r'\1', consonants_ar(ar))
    t = re.sub(r'(.)\1+', r'\1', consonants_tr(tr))
    if not a or not t:
        return False
    # allow for the article assimilating (ash-shams) and other small differences
    from difflib import SequenceMatcher
    return SequenceMatcher(None, a, t).ratio() < 0.6


stats = Counter()
seen_ex = defaultdict(list)
for u in units:
    uid = u['id']
    for ri, r in enumerate(u['rules']):
        check_arabic(uid, 'rule%d.body' % (ri + 1), r['body'], vocalised=True)
        for ei, e in enumerate(r['ex']):
            where = 'rule%d.ex%d' % (ri + 1, ei + 1)
            stats['examples'] += 1
            check_arabic(uid, where, e['ar'])
            if e.get('note'):
                check_arabic(uid, where + '.note', e['note'])
            if not e.get('tr'):
                stats['no_tr'] += 1
                if show_all:
                    add('NO-TRANSLIT', uid, where, e['ar'])
            elif tr_mismatch(e['ar'], e['tr']):
                add('TRANSLIT?', uid, where, e['ar'] + '  ~  ' + e['tr'])
            if not e.get('en'):
                add('NO-MEANING', uid, where, e['ar'])
            if not e.get('note'):
                stats['no_note'] += 1
            seen_ex[(uid, ri, e['ar'])].append(ei)
    for wi, w in enumerate(u['words']):
        check_arabic(uid, 'word%d' % (wi + 1), w['ar'])
        if w.get('pl'):
            check_arabic(uid, 'word%d.pl' % (wi + 1), w['pl'])
        if not w.get('type'):
            add('NO-TYPE', uid, 'word%d' % (wi + 1), w['ar'] + ' = ' + w['en'])
    for qi, q in enumerate(u['qs'] + (u.get('conv') or {}).get('qs', [])):
        where = 'q%d' % (qi + 1)
        check_arabic(uid, where + '.a', q['a'])
        bare = lambda s: re.sub('[' + HARAKA + 'ٰ]', '', s).strip(' ؟?.!،,')
        if q['a'] in q['w']:
            add('ANSWER-IN-WRONG', uid, where, q['q'] + ' -> ' + q['a'])
        elif bare(q['a']) in [bare(x) for x in q['w']] and not any(c in q['q'] for c in 'ـ'):
            add('SAME-LETTERS', uid, where, q['q'] + ' -> ' + q['a'] + ' | ' + ' / '.join(q['w']))
        if len(set(q['w'])) < len(q['w']):
            add('DUP-WRONG', uid, where, q['q'])
        if len(q['w']) < 2:
            add('FEW-OPTIONS', uid, where, q['q'])
    if u.get('conv'):
        for li, l in enumerate(u['conv']['lines']):
            check_arabic(uid, 'line%d' % (li + 1), l['ar'])
for k, v in seen_ex.items():
    if len(v) > 1:
        add('DUP-EXAMPLE', k[0], 'rule%d' % (k[1] + 1), k[2])

counts = Counter(c for c, *_ in out)
for c, uid, where, text in out:
    print('%-15s | %-7s | %-16s | %s' % (c, uid, where, text))
print('\nexamples: %(examples)d, without transliteration: %(no_tr)d, without note: %(no_note)d' % stats)
print('findings:', dict(counts))
