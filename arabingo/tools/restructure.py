#!/usr/bin/env python3
"""Rebuild the Arabingo course so that every unit teaches at most two topics
and every level holds 15-20 topics.

Input : a JSON array of the original units (the SEED array from index.html).
Output: a JSON object {"units": [...], "oldmap": {...}, "lvmap": {...}}
        - units  : the new SEED array
        - oldmap : old unit id -> list of new unit ids (for progress migration)
        - lvmap  : old level-test id -> list of new level-test ids

Each original unit becomes a *theme*. Its lessons are split into small units of
one or two lessons. Words and questions go to the small unit that teaches them,
and the theme's conversation goes to its last small unit. Review units are split
so that every new level made from an original level ends with its own review.
"""
import json
import re
import sys

# ---------------------------------------------------------------- the plan
# Original levels -> new levels, as lists of original unit numbers (themes).
PLAN = [
    (1, [[1, 2], [3, 4, 5], [6, 7], [8, 9, 10]]),
    (2, [[1, 2, 3], [4, 5, 6], [7, 8, 9]]),
    (3, [[1, 2, 3, 4], [5, 6, 7, 8, 9]]),
    (4, [[1, 2, 3, 4, 5], [6, 7, 8, 9]]),
    (5, [[1, 2, 3, 4, 5], [6, 7, 8, 9]]),
    (6, [[1, 2, 3, 4, 5], [6, 7, 8, 9]]),
    (7, [[1, 2, 3, 4, 5], [6, 7, 8, 9]]),
]
# Original levels 1-3 are beginner work; 4-7 open with the passive, verbal
# nouns and participles, which is intermediate grammar.
STAGE_OF = {1: 1, 2: 1, 3: 1, 4: 2, 5: 2, 6: 2, 7: 2}
REVIEW_UNIT = 10  # in original levels 3-7, unit 10 is the level review

# Lessons are paired in order unless a better pairing is given here.
GROUPS = {
    '1-1-5': [[0, 1], [2, 5], [3, 4]],  # jobs | more jobs + workplaces | nationalities + where from
    '1-3-5': [[0, 3], [1, 2]],          # places + traffic | bigger + biggest
}

# Arabic names for lessons whose titles were English only.
AR_LABEL = {
    ('1-1-1', 7): 'المُذَكَّرُ وَالمُؤَنَّثُ',
    ('1-1-2', 5): 'نَعَمْ وَلَا وَمِنْ أَيْنَ',
    ('1-1-2', 7): 'عِبَارَاتٌ مُفِيدَةٌ',
    ('1-3-4', 2): 'التَّهْنِئَةُ وَالدُّعَاءُ',
    ('1-3-5', 0): 'أَمَاكِنُ فِي المَدِينَةِ',
    ('1-3-5', 3): 'الازْدِحَامُ وَالانْتِظَارُ',
    ('1-3-6', 0): 'كَلِمَاتُ الجَامِعَةِ',
    ('1-3-6', 1): 'التَّعَلُّمُ وَالتَّعْلِيمُ',
    ('1-3-7', 2): 'المُقَابَلَةُ وَالرَّاتِبُ',
    ('1-3-8', 0): 'كَلِمَاتُ اللُّغَةِ',
    ('1-3-8', 1): 'كَلِمَاتُ النَّحْوِ',
    ('1-3-9', 0): 'الجَوَائِزُ وَالمُسَابَقَاتُ',
    ('1-4-1', 0): 'المَبْنِيُّ لِلْمَجْهُولِ',
    ('1-4-1', 1): 'المُضَارِعُ المَبْنِيُّ لِلْمَجْهُولِ',
    ('1-4-2', 0): 'كَلِمَاتُ التِّقْنِيَّةِ',
    ('1-4-2', 1): 'الاتِّصَالُ وَاللِّقَاءُ',
    ('1-4-3', 0): 'كَلِمَاتُ النَّظَافَةِ',
    ('1-4-3', 1): 'أَفْعَالُ التَّنْظِيفِ',
    ('1-4-4', 0): 'الإِسْلَامُ وَالإِيمَانُ',
    ('1-4-4', 1): 'أَرْكَانُ الإِسْلَامِ',
    ('1-4-4', 2): 'العَدَدُ مِنْ ثَلَاثَةٍ إِلَى عَشَرَةٍ',
    ('1-4-4', 3): 'القُرْآنُ وَالنَّبِيُّ ﷺ',
    ('1-4-5', 0): 'الشَّبَابُ',
    ('1-4-5', 1): 'الأَحْلَامُ وَالآمَالُ',
    ('1-4-5', 3): 'التَّطَوُّعُ',
    ('1-4-6', 0): 'الدُّوَلُ وَالعَوَاصِمُ',
    ('1-4-6', 1): 'الجِهَاتُ وَالجِنْسِيَّةُ',
    ('1-4-6', 2): 'التَّارِيخُ وَالحَضَارَةُ',
    ('1-4-6', 3): 'لُغَاتُ العَالَمِ الإِسْلَامِيِّ',
    ('1-4-7', 0): 'كَلِمَاتُ السَّلَامَةِ',
    ('1-4-7', 1): 'حَالَاتُ الطَّوَارِئِ',
    ('1-4-7', 3): 'التَّحْذِيرَاتُ وَالقَوَاعِدُ',
    ('1-4-8', 0): 'كَلِمَاتُ البِيئَةِ',
    ('1-4-8', 2): 'حِمَايَةُ البِيئَةِ',
    ('1-4-8', 3): 'السَّبَبُ وَالنَّتِيجَةُ',
    ('1-4-9', 0): 'كَلِمَاتُ الطَّاقَةِ',
    ('1-4-9', 1): 'الاسْتِخْدَامُ وَالاسْتِهْلَاكُ',
    ('1-4-9', 2): 'تَوْفِيرُ الطَّاقَةِ',
    ('1-4-9', 3): 'المَصَادِرُ المُتَجَدِّدَةُ وَالمَحْدُودَةُ',
    ('1-5-1', 3): 'بَعْضُنَا بَعْضًا',
    ('1-5-2', 1): 'المُثَنَّى',
    ('1-5-2', 2): 'أَفْعَالُ الحَيَوَانَاتِ',
    ('1-5-2', 3): 'النَّبَاتَاتُ وَالمَنَاظِرُ',
    ('1-5-3', 0): 'كَلِمَاتُ المَشَاعِرِ',
    ('1-5-3', 2): 'أَفْعَالٌ مَعَ حُرُوفِ الجَرِّ',
    ('1-5-3', 3): 'لِمَاذَا تَشْعُرُ بِذَلِكَ؟',
    ('1-5-4', 0): 'الأَخْلَاقُ الحَسَنَةُ',
    ('1-5-4', 1): 'الأَخْلَاقُ السَّيِّئَةُ',
    ('1-5-5', 0): 'الرَّأْسُ',
    ('1-5-5', 1): 'الجِسْمُ',
    ('1-5-5', 2): 'المُثَنَّى فِي الجِسْمِ',
    ('1-5-5', 3): 'الحَوَاسُّ وَالأَلَمُ',
    ('1-5-6', 0): 'كَلِمَاتُ رَمَضَانَ',
    ('1-5-6', 1): 'قَبْلَ وَبَعْدَ',
    ('1-5-6', 2): 'الجَائِزُ وَغَيْرُ الجَائِزِ',
    ('1-5-6', 3): 'اللَّيَالِي وَالأَعْمَالُ المُبَارَكَةُ',
    ('1-5-7', 0): 'مَنْ يُعْطِي وَمَنْ يَأْخُذُ',
    ('1-5-7', 1): 'أَفْعَالُ العَطَاءِ',
    ('1-5-7', 3): 'الصَّدَقَةُ الجَارِيَةُ',
    ('1-5-8', 0): 'كَلِمَاتُ التَّوْبَةِ',
    ('1-5-8', 1): 'شُرُوطُ التَّوْبَةِ',
    ('1-5-8', 3): 'الاعْتِذَارُ وَالعَفْوُ',
    ('1-5-9', 0): 'كَلِمَاتُ الدُّعَاءِ',
    ('1-5-9', 1): 'آدَابُ الدُّعَاءِ',
    ('1-5-9', 2): 'أَدْعِيَةٌ يَوْمِيَّةٌ',
    ('1-5-9', 3): 'أَدْعِيَةٌ مِنَ القُرْآنِ',
    ('1-6-1', 1): 'مَصَادِرُ الأَوْزَانِ الأُخْرَى',
    ('1-6-2', 0): 'مَلَابِسُ الرِّجَالِ وَالنِّسَاءِ',
    ('1-6-2', 2): 'الأَقْمِشَةُ وَوَصْفُ المَلَابِسِ',
    ('1-6-2', 3): 'الحِشْمَةُ وَاخْتِيَارُ المَلَابِسِ',
    ('1-6-3', 0): 'أَسْمَاءُ الرِّيَاضَاتِ',
    ('1-6-3', 1): 'اللَّاعِبُونَ وَالفِرَقُ وَالمُبَارَيَاتُ',
    ('1-6-3', 2): 'اللِّيَاقَةُ وَالصِّحَّةُ',
    ('1-6-4', 0): 'المَرْكَبَاتُ',
    ('1-6-4', 1): 'فِي المَحَطَّةِ وَالمَطَارِ',
    ('1-6-4', 2): 'عَلَى الطَّرِيقِ',
    ('1-6-4', 3): 'السَّلَامَةُ وَدُعَاءُ السَّفَرِ',
    ('1-6-5', 0): 'مَعْرِفَةُ الوَقْتِ',
    ('1-6-5', 1): 'أَوْقَاتُ اليَوْمِ وَالصَّلَوَاتُ',
    ('1-6-5', 2): 'الشُّهُورُ المِيلَادِيَّةُ',
    ('1-6-5', 3): 'المَوَاعِيدُ وَقِيمَةُ الوَقْتِ',
    ('1-6-6', 0): 'التَّقْوِيمُ الهِجْرِيُّ',
    ('1-6-6', 1): 'الشُّهُورُ الاثْنَا عَشَرَ',
    ('1-6-6', 2): 'الأَشْهُرُ الحُرُمُ',
    ('1-6-6', 3): 'رُؤْيَةُ الهِلَالِ',
    ('1-6-7', 0): 'الأَسْمَاءُ الحُسْنَى',
    ('1-6-7', 1): 'الرَّحْمَةُ وَالمَغْفِرَةُ',
    ('1-6-7', 2): 'العِلْمُ وَالقُدْرَةُ',
    ('1-6-7', 3): 'الرِّزْقُ وَالقُرْبُ',
    ('1-6-8', 0): 'المَلَائِكَةُ',
    ('1-6-8', 1): 'أَعْمَالُ المَلَائِكَةِ',
    ('1-6-8', 2): 'الجِنُّ',
    ('1-6-8', 3): 'الاسْتِعَاذَةُ وَالأَذْكَارُ',
    ('1-6-9', 0): 'المَوْتُ وَالقَبْرُ',
    ('1-6-9', 1): 'يَوْمُ القِيَامَةِ',
    ('1-6-9', 2): 'الجَنَّةُ وَالنَّارُ',
    ('1-6-9', 3): 'الاسْتِعْدَادُ لِلْآخِرَةِ',
    ('1-7-2', 0): 'الأَجْهِزَةُ',
    ('1-7-2', 1): 'اسْتِخْدَامُ الإِنْتَرْنِتِ',
    ('1-7-2', 2): 'وَسَائِلُ التَّوَاصُلِ',
    ('1-7-2', 3): 'الاسْتِخْدَامُ الحَسَنُ وَالسَّيِّئُ',
    ('1-7-3', 0): 'المَزْرَعَةُ وَالمُزَارِعُ',
    ('1-7-3', 1): 'البُذُورُ وَالنَّبَاتَاتُ وَالمَحَاصِيلُ',
    ('1-7-3', 2): 'الرَّيُّ وَالحَصَادُ',
    ('1-7-3', 3): 'الزِّرَاعَةُ صَدَقَةٌ',
    ('1-7-4', 0): 'البَحْرُ وَالشَّاطِئُ',
    ('1-7-4', 1): 'الصَّيْدُ وَالإِبْحَارُ',
    ('1-7-4', 2): 'المَاءُ فِي الإِسْلَامِ',
    ('1-7-4', 3): 'قِصَصُ البَحْرِ',
    ('1-7-5', 0): 'أَرْضُ الصَّحْرَاءِ',
    ('1-7-5', 1): 'الإِبِلُ وَالبَدْوُ',
    ('1-7-5', 2): 'الكَرَمُ فِي الصَّحْرَاءِ',
    ('1-7-5', 3): 'الضَّيَاعُ فِي الصَّحْرَاءِ وَالتَّيَمُّمُ',
    ('1-7-6', 0): 'الأَمَانَةُ وَالعَدْلُ وَالإِحْسَانُ',
    ('1-7-6', 1): 'التَّوَاضُعُ وَالحَيَاءُ',
    ('1-7-6', 2): 'الإِحْسَانُ إِلَى النَّاسِ',
    ('1-7-6', 3): 'الإِخْلَاصُ وَالتَّوَكُّلُ',
    ('1-7-7', 0): 'المَوْلِدُ وَالطُّفُولَةُ',
    ('1-7-7', 1): 'الوَحْيُ وَالدَّعْوَةُ',
    ('1-7-7', 2): 'الهِجْرَةُ وَالمَدِينَةُ',
    ('1-7-7', 3): 'الغَزَوَاتُ وَالصُّلْحُ وَالفَتْحُ',
    ('1-7-8', 0): 'الأَحْكَامُ الخَمْسَةُ',
    ('1-7-8', 1): 'الشُّرُوطُ وَالأَرْكَانُ وَالصِّحَّةُ',
    ('1-7-8', 2): 'الطَّهَارَةُ وَالنَّجَاسَةُ',
    ('1-7-8', 3): 'مَصَادِرُ التَّشْرِيعِ وَالعُلَمَاءُ',
    ('1-7-9', 0): 'أَجْزَاءُ القُرْآنِ',
    ('1-7-9', 1): 'التَّعَامُلُ مَعَ القُرْآنِ',
    ('1-7-9', 2): 'صِفَاتُ القُرْآنِ',
    ('1-7-9', 3): 'كَلِمَاتٌ وَأَوَامِرُ شَائِعَةٌ',
}
# English titles that carried an English aside in brackets.
EN_RENAME = {
    ('1-4-1', 0): 'The passive: what was done',
    ('1-5-2', 1): 'The dual: two of them',
}
ORD_AR = ['الأَوَّلِ', 'الثَّانِي', 'الثَّالِثِ', 'الرَّابِعِ', 'الخَامِسِ', 'السَّادِسِ',
          'السَّابِعِ', 'الثَّامِنِ', 'التَّاسِعِ', 'العَاشِرِ']

# ---------------------------------------------------------------- matching
HARAKAT = re.compile('[ً-ٰٟـۖ-ۭ]')
ARABIC = re.compile('[؀-ۿ]')
STOP = set('هذا هذه ذلك تلك في من الى على عن هو هي انا انت نحن هم ما لا نعم مع ثم او قد كل'.split())
PREFIXES = ['وال', 'فال', 'بال', 'كال', 'لل', 'ال', 'و', 'ف', 'ب', 'ل', 'ك', 'س']


def nar(s):
    s = HARAKAT.sub('', s or '')
    s = re.sub('[أإآٱ]', 'ا', s)
    s = s.replace('ى', 'ي').replace('ة', 'ه').replace('ؤ', 'و').replace('ئ', 'ي')
    s = re.sub(r'[^ء-ي\s]', ' ', s)
    return re.sub(r'\s+', ' ', s).strip()


def variants(tok):
    out = {tok}
    for p in PREFIXES:
        if tok.startswith(p) and len(tok) - len(p) >= 2:
            out.add(tok[len(p):])
    return out


def stems(word):
    w = nar(word)
    s = {w}
    if w.startswith('ال') and len(w) > 4:
        s.add(w[2:])
    if w.endswith('ه') and len(w) >= 3:
        s.add(w[:-1] + 'ت')
    return s


def tok_hit(stem, tokset):
    for t in tokset:
        for v in variants(t):
            if v == stem:
                return True
            if len(stem) >= 3 and v.startswith(stem) and len(v) - len(stem) <= 3:
                return True
    return False


def phrase_in(a, text):
    return bool(a) and (' ' + a + ' ') in (' ' + text + ' ')


class Bag:
    """Normalised text of a group of lessons, kept by source."""

    def __init__(self, rules):
        self.ex = [nar(e['ar']) for r in rules for e in r['ex']]
        self.en = [(e.get('en') or '').lower() for r in rules for e in r['ex']]
        self.body = nar(' '.join(r['body'] + ' ' + ' '.join(e.get('note', '') for e in r['ex']) for r in rules))
        self.title = nar(' '.join(r['title'] for r in rules))
        self.ex_toks = set(' '.join(self.ex).split())
        self.body_toks = set(self.body.split()) | set(self.title.split())
        self.all_toks = self.ex_toks | self.body_toks

    def word_where(self, w):
        """3 = taught in an example, 1 = mentioned in the explanation, 0 = absent."""
        cands = [w['ar']] + ([w['pl']] if w.get('pl') else [])
        best = 0
        for c in cands:
            n = nar(c)
            if not n:
                continue
            if ' ' in n:
                if any(phrase_in(n, x) for x in self.ex):
                    return 3
                if phrase_in(n, self.body):
                    best = max(best, 1)
                continue
            for s in stems(c):
                if tok_hit(s, self.ex_toks):
                    return 3
                if tok_hit(s, self.body_toks):
                    best = max(best, 1)
        return best

    def q_score(self, q, words_here):
        a = nar(q['a'])
        sc = 0.0
        if a:
            if any(phrase_in(a, x) for x in self.ex):
                sc += 10
            elif phrase_in(a, self.body):
                sc += 5
            toks = [t for t in a.split() if len(t) > 2 and t not in STOP]
            if toks:
                sc += 3 * sum(1 for t in toks if tok_hit(t, self.all_toks)) / len(toks)
        for t in nar(q['q']).split():
            if len(t) > 2 and t not in STOP and tok_hit(t, self.all_toks):
                sc += 2
        for ph in re.findall(r'[“"]([^”"]{2,})[”"]', q['q']):
            ph = ph.lower().strip(' ?.!')
            if ph and any(re.search(r'\b' + re.escape(ph) + r'\b', e) for e in self.en):
                sc += 6
        if any(nar(w['ar']) == a for w in words_here):
            sc += 8
        return sc


# ---------------------------------------------------------------- helpers
def split_title(title, uid, i):
    """Return (english, arabic) names for a lesson title."""
    m = re.match(r'^(.*?)\s*\(([^()]*)\)\s*$', title)
    if m and ARABIC.search(m.group(2)):
        return m.group(1).strip(), m.group(2).strip()
    en = EN_RENAME.get((uid, i), title)
    ar = AR_LABEL.get((uid, i))
    if not ar:
        raise SystemExit('missing Arabic label for %s lesson %d: %s' % (uid, i + 1, title))
    return en, ar


def groups_for(u):
    if u['id'] in GROUPS:
        g = GROUPS[u['id']]
        assert sorted(i for x in g for i in x) == list(range(len(u['rules']))), u['id']
        return g
    n = len(u['rules'])
    return [list(range(i, min(i + 2, n))) for i in range(0, n, 2)]


def reminder_names(title):
    m = re.match(r'^Reminders:\s*(.*)$', title)
    body = m.group(1) if m else title
    parts = re.split(r',\s*|\s+and\s+', body)
    return [p.strip() for p in parts if p.strip()]


def join_names(names):
    if len(names) <= 1:
        return ''.join(names)
    return ', '.join(names[:-1]) + ' and ' + names[-1]


def plain_theme(name):
    """Drop the "Introduction: " prefix the old levels used for their grammar theme."""
    for pre in ('Introduction: ', 'المُقَدِّمَةُ: '):
        if name.startswith(pre):
            return name[len(pre):]
    return name


def best(scores):
    """Index of the highest score, earliest on ties; None if all zero."""
    top = max(scores)
    if top <= 0:
        return None
    return scores.index(top)


# ---------------------------------------------------------------- build
def build(old):
    byid = {u['id']: u for u in old}
    out, oldmap, lvmap = [], {}, {}
    lv_count = {1: 0, 2: 0, 3: 0}
    report = []

    for old_lv, new_levels in PLAN:
        stage = STAGE_OF[old_lv]
        review = byid.get('1-%d-%d' % (old_lv, REVIEW_UNIT)) if old_lv >= 3 else None
        lvmap['lt-1-%d' % old_lv] = []
        # where each original theme lands (for splitting the review)
        theme_level = {}
        new_lv_ids = []
        for k, themes in enumerate(new_levels):
            lv_count[stage] += 1
            new_lv_ids.append((stage, lv_count[stage]))
            for t in themes:
                theme_level[t] = k

        # split the review: reminder examples and questions follow their theme
        review_parts = None
        if review:
            theme_bags = {t: Bag(byid['1-%d-%d' % (old_lv, t)]['rules']) for t in theme_level}
            theme_words = {t: byid['1-%d-%d' % (old_lv, t)]['words'] for t in theme_level}
            review_parts = [{'rules': [], 'qs': []} for _ in new_levels]
            for r in review['rules']:
                rng = re.search(r'Units? (\d+)(?: to | and )(\d+)', r['body'])
                lo, hi = (int(rng.group(1)), int(rng.group(2))) if rng else (1, 9)
                span = list(range(lo, hi + 1))
                names = reminder_names(r['title'])
                name_of = dict(zip(span, names)) if len(names) == len(span) else {}
                by_level = {}
                for j, e in enumerate(r['ex']):
                    cands = [t for t in span if t in theme_bags]
                    sc = [theme_bags[t].q_score({'q': '', 'a': e['ar']}, theme_words[t]) for t in cands]
                    pick = best(sc)
                    # fall back to the reminder's own order: examples run through its units in turn
                    t = cands[pick] if pick is not None else cands[min(len(cands) - 1, j * len(cands) // len(r['ex']))]
                    by_level.setdefault(theme_level[t], []).append((t, e))
                for k, items in sorted(by_level.items()):
                    ts = sorted(set(t for t, _ in items))
                    whole = len(by_level) == 1
                    title = r['title'] if whole or not name_of else 'Reminders: ' + join_names([name_of[t] for t in ts])
                    nm = [name_of[t] for t in ts] if name_of else names
                    review_parts[k]['rules'].append({
                        'title': title,
                        'body': 'These are the key patterns from ' + join_names(nm) + '. Read each one aloud.',
                        'ex': [e for _, e in items],
                    })
            for q in review['qs']:
                sc = [theme_bags[t].q_score(q, theme_words[t]) for t in sorted(theme_bags)]
                pick = best(sc)
                t = sorted(theme_bags)[pick] if pick is not None else max(theme_level)
                review_parts[theme_level[t]]['qs'].append(q)

        for k, themes in enumerate(new_levels):
            stage, lv = new_lv_ids[k]
            lvmap['lt-1-%d' % old_lv].append('lt-%d-%d' % (stage, lv))
            order = 0
            lv_topics, lv_units = 0, 0
            for t in themes:
                u = byid['1-%d-%d' % (old_lv, t)]
                gs = groups_for(u)
                rules = []
                for i, r in enumerate(u['rules']):
                    en, ar = split_title(r['title'], u['id'], i)
                    rules.append(dict(r, title='%s (%s)' % (en, ar), _en=en, _ar=ar))
                bags = [Bag([rules[i] for i in g]) for g in gs]
                words = [[] for _ in gs]
                for w in u['words']:
                    where = [b.word_where(w) for b in bags]
                    pick = best(where)
                    if pick is None:
                        en = (w.get('en') or '').lower().split(',')[0].split('(')[0].strip()
                        hits = [any(en and re.search(r'\b' + re.escape(en) + r'\b', x) for x in b.en) for b in bags]
                        pick = hits.index(True) if any(hits) else min(range(len(gs)), key=lambda i: (len(words[i]), i))
                    words[pick].append(w)
                qs = [[] for _ in gs]
                for q in u['qs']:
                    sc = [b.q_score(q, words[i]) for i, b in enumerate(bags)]
                    pick = best(sc)
                    if pick is None:
                        pick = min(range(len(gs)), key=lambda i: (len(qs[i]), i))
                    qs[pick].append(q)
                ids = []
                for gi, g in enumerate(gs):
                    order += 1
                    rs = [rules[i] for i in g]
                    nu = {
                        'stage': stage, 'level': lv, 'order': order,
                        'titleAr': ' · '.join(r['_ar'] for r in rs),
                        'titleEn': ' · '.join(r['_en'] for r in rs),
                        'about': u['about'],
                        'theme': {'ar': plain_theme(u['titleAr']), 'en': plain_theme(u['titleEn']), 'part': gi + 1, 'parts': len(gs)},
                        'rules': [{k2: v for k2, v in r.items() if not k2.startswith('_')} for r in rs],
                        'words': words[gi],
                        'qs': qs[gi],
                    }
                    if gi == len(gs) - 1 and u.get('conv'):
                        nu['conv'] = u['conv']
                    nu['id'] = '%d-%d-%d' % (stage, lv, order)
                    out.append(nu)
                    ids.append(nu['id'])
                    lv_topics += len(rs)
                    lv_units += 1
                    report.append('    %-8s %-58s topics=%d words=%2d qs=%2d%s' % (
                        nu['id'], nu['titleEn'][:58], len(rs), len(words[gi]), len(qs[gi]), ' +conv' if 'conv' in nu else ''))
                oldmap[u['id']] = ids
            if review_parts:
                part = review_parts[k]
                order += 1
                last = k == len(new_levels) - 1
                theme_names = [plain_theme(byid['1-%d-%d' % (old_lv, t)]['titleEn']) for t in themes]
                nu = {
                    'stage': stage, 'level': lv, 'order': order,
                    'titleAr': 'مُرَاجَعَةُ المُسْتَوَى ' + ORD_AR[lv - 1],
                    'titleEn': 'Level %d Review' % lv,
                    'about': 'A review of Level %d. Read the reminders, then practise the themes of this level: %s.' % (lv, ' · '.join(theme_names)),
                    'review': True,
                    'theme': {'ar': 'المُرَاجَعَةُ', 'en': 'Review', 'part': 1, 'parts': 1},
                    'rules': part['rules'], 'words': [], 'qs': part['qs'],
                }
                if last and review.get('conv'):
                    nu['conv'] = review['conv']
                nu['id'] = '%d-%d-%d' % (stage, lv, order)
                out.append(nu)
                oldmap.setdefault(review['id'], []).append(nu['id'])
                lv_units += 1
                report.append('    %-8s %-58s recap=%d qs=%2d%s' % (
                    nu['id'], nu['titleEn'], len(part['rules']), len(part['qs']), ' +conv' if 'conv' in nu else ''))
            report.insert(len(report) - lv_units, 'Stage %d Level %d (from old level %d): %d topics, %d units' % (
                stage, lv, old_lv, lv_topics, lv_units))
    return out, oldmap, lvmap, report


def check(units):
    errs = []
    lv = {}
    for u in units:
        if not u.get('review') and len(u['rules']) > 2:
            errs.append('%s has %d topics' % (u['id'], len(u['rules'])))
        if u.get('review') and len(u['rules']) > 2:
            errs.append('%s review has %d recap pages' % (u['id'], len(u['rules'])))
        key = (u['stage'], u['level'])
        lv.setdefault(key, [0, 0])
        lv[key][1] += 1
        if not u.get('review'):
            lv[key][0] += len(u['rules'])
    for key, (t, n) in sorted(lv.items()):
        if not 15 <= t <= 20:
            errs.append('stage %d level %d has %d topics' % (key[0], key[1], t))
        if n > 12:
            errs.append('stage %d level %d has %d units' % (key[0], key[1], n))
    return errs


if __name__ == '__main__':
    src, dst = sys.argv[1], sys.argv[2]
    old = json.load(open(src, encoding='utf-8'))
    units, oldmap, lvmap, report = build(old)
    errs = check(units)
    print('\n'.join(report))
    n_old = sum(len(u['qs']) for u in old)
    n_new = sum(len(u['qs']) for u in units)
    w_old = sum(len(u['words']) for u in old)
    w_new = sum(len(u['words']) for u in units)
    print('units %d -> %d, questions %d -> %d, words %d -> %d' % (len(old), len(units), n_old, n_new, w_old, w_new))
    if errs:
        print('\n'.join('ERROR: ' + e for e in errs))
        sys.exit(1)
    json.dump({'units': units, 'oldmap': oldmap, 'lvmap': lvmap}, open(dst, 'w', encoding='utf-8'),
              ensure_ascii=False, separators=(',', ':'))
