# Course-wide style: runs after every level's fixes.
import re


def _allah(s):
    # Most lessons say "Allah"; a few said "God". Keep "God-fearing" and the lower-case "god".
    s = re.sub(r"\bGod's\b", "Allah's", s)
    return re.sub(r"\bGod\b(?!-)", "Allah", s)


def _english(s):
    return re.sub(r"\btanwin\b", "tanween", _allah(s))


def _arabic(s):
    # The course writes the article اَلْ without a sukoon: اليَوْمَ, not الْيَوْمَ.
    return re.sub(r"(?<![\u0621-\u064A\u064B-\u0652])الْ", "ال", s)


def _each_text(u):
    yield u, 'about'
    for r in u['rules']:
        yield r, 'title'
        yield r, 'body'
        for e in r['ex']:
            yield e, 'en'
            yield e, 'note'
    for w in u['words']:
        yield w, 'en'
    for q in u['qs'] + u.get('conv', {}).get('qs', []):
        yield q, 'q'


def _each_arabic(u):
    for r in u['rules']:
        for e in r['ex']:
            yield e, 'ar'
    for q in u['qs'] + u.get('conv', {}).get('qs', []):
        yield q, 'a'
    for l in u.get('conv', {}).get('lines', []):
        yield l, 'ar'


# In connected speech the first ا of a word like اغْفِرْ or امْرَأَةٌ is silent.
TR_WASL = {
    "ʿindahu ibnun": "ʿindahu bnun",
    "hiya imraʾatun laṭīfatun": "hiya mraʾatun laṭīfatun",
    "jumlatun ismiyyatun": "jumlatuni smiyyatun",
    "kāna hunāka izdiḥāmun": "kāna hunāka zdiḥāmun",
    "hiya imraʾatun dhātu ʿilmin": "hiya mraʾatun dhātu ʿilmin",
    "hiya aktharu ijtihādan min ukhtihā": "hiya aktharu jtihādan min ukhtihā",
    "yā rabbi ighfir lī": "yā rabbi ghfir lī",
    "allāhumma ighfir lī": "allāhumma ghfir lī",
    "allāhumma iftaḥ lī abwāba raḥmatika": "allāhumma ftaḥ lī abwāba raḥmatika",
    "rabbi ishraḥ lī ṣadrī": "rabbi shraḥ lī ṣadrī",
    "allāhumma isqinā": "allāhumma sqinā",
    "allāhumma irzuqnā tilāwatahu": "allāhumma rzuqnā tilāwatahu",
    "mā ismuka": "mā smuka",
    "mā ismuki": "mā smuki",
    "mā ismuhu": "mā smuhu",
    "mā ismuhā": "mā smuhā",
    "hādhā izdiḥāmun": "hādhā zdiḥāmun",
    "hādhā imtiḥānun": "hādhā mtiḥānun",
    "baʿda fī yaʾtī ismun majrūrun": "baʿda fī yaʾtī smun majrūrun",
    "as-sanatu fīhā ithnā ʿashara shahran": "as-sanatu fīhā thnā ʿashara shahran",
    "at-tiqniyyatu niʿmatun idhā istakhdamnāhā fi l-khayri": "at-tiqniyyatu niʿmatun idhā stakhdamnāhā fi l-khayri",
}


def POST(units):
    for u in units.values():
        for obj, key in _each_text(u):
            if obj.get(key):
                obj[key] = _english(obj[key])
        for obj, key in _each_arabic(u):
            obj[key] = _arabic(obj[key])
        for q in u['qs'] + u.get('conv', {}).get('qs', []):
            q['w'] = [_arabic(w) for w in q['w']]
        for r in u['rules']:
            for e in r['ex']:
                # Transliterations are lower case throughout, names included.
                e['tr'] = TR_WASL.get(e['tr'].lower(), e['tr'].lower())
