# Stage 1 · Level 12 (was Stage 2 · Level 3) — content corrections and improvements.
INTRO_ABOUT = "Learn new verb patterns. You will learn verbs that show \"it happened by itself\" (like اِنْفَتَحَ), verbs for doing something to each other (like تَقَابَلَ), how to say \"each other\" with بَعْضُنَا بَعْضًا, and how to exclaim with مَا أَجْمَلَ!"
FIXES = [
    # This theme used to open "Level 5".
    {"u": "1-12-1", "set": {"about": INTRO_ABOUT}},
    {"u": "1-12-2", "set": {"about": INTRO_ABOUT}},

    {"u": "1-12-1", "r": 1, "was": "It happened by itself", "set": {"body": B("""
        Some verbs start with اِنْـ and show that something happened to a thing on its own, with nobody named. This pattern is اِنْفَعَلَ.
        - فَتَحَ is "he opened", and اِنْفَتَحَ is "it opened".
        - كَسَرَ is "he broke", and اِنْكَسَرَ is "it broke".
        Their present forms are يَنْفَتِحُ and يَنْكَسِرُ. Compare the passive فُتِحَ, which means someone opened it.
    """)}},
    # الكَهْرَبَاءُ is feminine (as taught in Level 2), so the verb takes ـتْ.
    {"u": "1-12-1", "r": 1, "e": 3, "was": "اِنْقَطَعَ الكَهْرَبَاءُ", "set": {"ar": "اِنْقَطَعَتِ الكَهْرَبَاءُ", "tr": "inqaṭaʿati l-kahrabāʾu", "en": "the electricity went off", "note": "قَطَعَ means \"he cut\". الكَهْرَبَاءُ is feminine, so the verb takes ـتْ, which becomes ـتِ before اَلْ."}},
    {"u": "1-12-1", "q": 8, "was": "How do you say \"the electricity cut off\"?", "set": {"q": "How do you say \"the electricity went off\"?", "a": "اِنْقَطَعَتِ الكَهْرَبَاءُ", "w": ["اِنْقَطَعَتِ الكَهْرَبَاءَ", "قَطَعَتِ الكَهْرَبَاءُ"]}},
    {"u": "1-12-1", "r": 2, "was": "Doing it to each other", "set": {"body": B("""
        Verbs that start with تَـ and have a long ا after the first root letter often show two or more people doing something to each other. This pattern is تَفَاعَلَ.
        - قَابَلَ is "he met", and تَقَابَلَ is "they met each other".
        - تَبَادَلَ means "they exchanged", and تَعَاوَنَ means "they cooperated".
        Use them with a plural or dual doer, or with نَا: تَقَابَلْنَا (we met).
    """)}},
    {"u": "1-12-1", "r": 2, "e": 3, "was": "تَعَاوَنَ الطُّلَّابُ", "set": {"note": "You saw نَتَعَاوَنُ (we cooperate) in Level 8."}},
    {"u": "1-12-1", "r": 2, "e": 4, "was": "تَسَاءَلَ النَّاسُ", "set": {"note": "سَأَلَ is \"he asked\"; تَسَاءَلَ, \"they asked each other\", means \"they wondered\"."}},
    {"u": "1-12-1", "r": 2, "e": 5, "was": "نَتَحَدَّثُ مَعًا", "set": {"note": "تَحَدَّثَ means \"he talked\". It has a doubled letter instead of a long ا, a different pattern; مَعًا adds \"together\"."}},
    # A verb-first broken plural of people may also take a feminine verb, so that is not a safe wrong answer.
    {"u": "1-12-1", "q": 14, "was": "How do you say \"the students cooperated\"?", "set": {"w": ["تَعَاوَنُوا الطُّلَّابُ", "يَتَعَاوَنُ الطُّلَّابُ"]}},

    {"u": "1-12-2", "r": 1, "was": "How!", "set": {"body": B("""
        To exclaim "how beautiful!", say مَا, then the describing word on the pattern أَفْعَلَ, then the thing. Both end with ـَ: مَا أَجْمَلَ الطَّبِيعَةَ! (how beautiful nature is!).
        It looks like the comparing word أَجْمَلُ, but here it ends with ـَ. With a pronoun ending, say مَا أَجْمَلَهَا! (how beautiful it is!).
    """)}},
    # "Each other": بَعْضُنَا is the subject, so the verb is the singular يُحِبُّ.
    {"u": "1-12-2", "r": 2, "was": "Each other and one another", "set": {"body": B("""
        To say "each other", use بَعْضٌ twice: بَعْضُنَا بَعْضًا (we... each other), بَعْضُهُمْ بَعْضًا (they... each other).
        The first بَعْضُ is the subject, so the verb before it is singular, like يُحِبُّ. The second is the object and ends with ـًا: يُحِبُّ بَعْضُنَا بَعْضًا (we love each other), literally "some of us love others".
    """)}},
    {"u": "1-12-2", "r": 2, "e": 1, "was": "نُحِبُّ بَعْضُنَا بَعْضًا", "set": {"ar": "يُحِبُّ بَعْضُنَا بَعْضًا", "tr": "yuḥibbu baʿḍunā baʿḍan", "note": "The verb is يُحِبُّ because its subject is بَعْضُنَا. In everyday Arabic you will also hear نُحِبُّ بَعْضَنَا."}},
    {"u": "1-12-2", "r": 2, "e": 3, "was": "يَحْتَرِمُ الطُّلَّابُ بَعْضَهُمْ", "set": {"ar": "يَحْتَرِمُ الطُّلَّابُ بَعْضُهُمْ بَعْضًا", "tr": "yaḥtarimu ṭ-ṭullābu baʿḍuhum baʿḍan", "note": "Literally \"the students, some of them respect others\"."}},
    {"u": "1-12-2", "q": 6, "was": "How do you say \"we love each other\"?", "set": {"a": "يُحِبُّ بَعْضُنَا بَعْضًا", "w": ["يُحِبُّ بَعْضًا بَعْضُنَا", "أُحِبُّ بَعْضُنَا بَعْضًا"]}},
    {"u": "1-12-2", "q": 8, "was": "How do you say \"the students respect one another\"?", "set": {"a": "يَحْتَرِمُ الطُّلَّابُ بَعْضُهُمْ بَعْضًا", "w": ["يَحْتَرِمُ الطُّلَّابُ بَعْضَهُمْ بَعْضٌ", "يَحْتَرِمُ الطُّلَّابَ بَعْضُهُمْ بَعْضًا"]}},
    {"u": "1-12-2", "l": 5, "was": "ثُمَّ اِنْطَفَأَ المِصْبَاحُ", "set": {"ar": "ثُمَّ انْطَفَأَ المِصْبَاحُ."}},
    {"u": "1-12-2", "l": 6, "was": "وَاِنْقَطَعَ الكَهْرَبَاءُ؟", "set": {"ar": "وَانْقَطَعَتِ الكَهْرَبَاءُ؟"}},
    {"u": "1-12-2", "l": 8, "was": "نُسَاعِدُ بَعْضُنَا بَعْضًا", "set": {"ar": "يُسَاعِدُ بَعْضُنَا بَعْضًا، وَنَتَحَدَّثُ مَعًا."}},

    {"u": "1-12-3", "r": 1, "e": 3, "was": "هَذَا حِصَانٌ", "set": {"note": "The plural is أَحْصِنَةٌ. For horses in general, Arabic also says خَيْلٌ or خُيُولٌ."}},
    {"u": "1-12-3", "w": 4, "was": "حِصَانٌ", "set": {"pl": "أَحْصِنَةٌ"}},
    {"u": "1-12-3", "w": 13, "was": "يَعِيشُ", "set": {"ar": "عَاشَ", "pl": "يَعِيشُ"}},
    {"u": "1-12-3", "r": 2, "was": "The dual: two of them", "set": {"body": B("""
        To say "two" of something, add ـَانِ to the noun: كِتَابٌ becomes كِتَابَانِ. A noun ending in ـَةٌ takes ـَتَانِ: قِطَّةٌ becomes قِطَّتَانِ.
        After a verb or a small word like فِي, the ending is ـَيْنِ (or ـَتَيْنِ): رَأَيْتُ أَسَدَيْنِ. A describing word takes the dual too: حِصَانَانِ كَبِيرَانِ. "These two" is هَذَانِ, or هَاتَانِ for feminine nouns.
    """)}},

    {"u": "1-12-4", "r": 1, "was": "What animals do", "set": {"body": B("""
        Animals do many things: يَعِيشُ (it lives), يَأْكُلُ (it eats), يَطِيرُ (it flies) and يَسْبَحُ (it swims). A plural of animals takes a feminine singular verb: تَطِيرُ الطُّيُورُ.
        Their food: لَحْمٌ (meat), عُشْبٌ (grass) and حَبٌّ (grain).
    """)}},
    {"u": "1-12-4", "r": 2, "e": 2, "was": "تَنْمُو النَّبَاتَاتُ بِالمَاءِ", "set": {"note": "نَمَا means \"it grew\" (يَنْمُو). نَبَاتَاتٌ is a plural of things, so the verb is feminine: تَنْمُو."}},
    {"u": "1-12-4", "cq": 10, "was": "Who is the teacher?", "set": {"q": "Who suggests sitting on the beach?", "a": "المُعَلِّمُ", "w": ["الطَّالِبُ", "الأَبُ"]}},

    {"u": "1-12-5", "r": 1, "e": 4, "was": "أَبِي قَلِقٌ", "set": {"note": "قَلِقٌ (worried) describes a person; قَلَقٌ is the noun \"worry\". Only the vowel on the ل is different."}},
    {"u": "1-12-5", "r": 1, "e": 7, "was": "أَنَا مُرْتَاحٌ", "set": {"tr": "anā murtāḥuni l-yawma", "note": "مُرْتَاحٌ comes from اِرْتَاحَ (he rested), like أَرْتَاحُ in Level 8."}},

    {"u": "1-12-6", "r": 1, "e": 3, "was": "أَشْتَاقُ إِلَى أُخْتِي", "set": {"note": "اِشْتَاقَ follows the pattern اِفْتَعَلَ, like اِتَّصَلَ. It always takes إِلَى."}},
    # لَا تَخَفْ is the "do not" form of تَخَافُ, not a command made from خَافَ.
    {"u": "1-12-6", "r": 1, "e": 10, "was": "لَا تَخَفْ", "set": {"note": "After لَا, تَخَافُ ends with a sukoon and its long ا drops: لَا تَخَفْ."}},
    {"u": "1-12-6", "r": 1, "e": 11, "was": "لَا تَقْلَقْ", "set": {"note": "For \"do not\", use لَا with the \"you\" verb ending in a sukoon."}},
    {"u": "1-12-6", "r": 2, "e": 2, "was": "أَنَا حَزِينٌ لِأَنَّ صَدِيقِي سَافَرَ", "set": {"note": "لِأَنَّ is followed by a noun or by a pronoun ending: لِأَنِّي (because I), لِأَنَّهُ (because he)."}},
    {"u": "1-12-6", "cq": 5, "was": "How does Ali feel about him?", "set": {"a": "يَشْعُرُ بِالفَخْرِ", "w": ["يَشْعُرُ بِالحُزْنِ", "يَشْعُرُ بِالغَضَبِ"]}},

    {"u": "1-12-7", "r": 1, "was": "Good character", "set": {"body": B("""
        شَخْصِيَّةٌ is a personality, and خُلُقٌ is a trait of character; the plural أَخْلَاقٌ means "character" or "manners". Good character is praised in Islam.
        Each describing word has a noun for the quality: صَادِقٌ (honest) and صِدْقٌ (honesty). For a woman, add ـَةٌ to the describing word.
    """)}},
    {"u": "1-12-7", "r": 2, "was": "Bad character", "set": {"body": B("""
        Some traits are bad: جَبَانٌ (cowardly), كَاذِبٌ (lying), عَنِيدٌ (stubborn), مُتَكَبِّرٌ (arrogant) and كَسُولٌ (lazy). Muslims try to avoid them.
        Learn them with their opposites: صَادِقٌ and كَاذِبٌ, شُجَاعٌ and جَبَانٌ, مُتَوَاضِعٌ and مُتَكَبِّرٌ, مُجْتَهِدٌ and كَسُولٌ.
    """)}},
    {"u": "1-12-7", "r": 2, "e": 1, "was": "لَا تَكُنْ كَاذِبًا", "set": {"note": "After لَا, تَكُونُ ends with a sukoon and loses its و: لَا تَكُنْ, \"do not be\". The word after it ends with ـًا, as after كَانَ."}},
    {"u": "1-12-7", "r": 2, "e": 7, "was": "أَنَا أَكْرَهُ الكَذِبَ", "set": {"tr": "anā akrahu l-kadhiba wa-anta ayḍan"}},

    {"u": "1-12-8", "r": 1, "was": "Owner of", "set": {"body": B("""
        ذُو means "having" or "a man of", and ذَاتُ is the feminine. The noun after them ends with ـٍ: رَجُلٌ ذُو أَخْلَاقٍ (a man of good character). They work a little like "-ful" in English.
        ذُو changes with the noun before it: ذَا where that noun ends in ـَ (رَأَيْتُ رَجُلًا ذَا خُلُقٍ), and ذِي where it ends in ـِ (عَلَى رَجُلٍ ذِي حِكْمَةٍ).
    """)}},
    {"u": "1-12-8", "r": 2, "was": "More than", "set": {"body": B("""
        To compare a quality, use أَكْثَرُ ("more") or أَقَلُّ ("less") with the noun for the quality ending in ـًا, then مِنْ: أَكْثَرُ صَبْرًا مِنْ عَلِيٍّ (more patient than Ali), literally "more in patience".
        This is useful when a describing word has no أَفْعَلُ form of its own.
    """)}},

    # This repeats the body lesson of Level 7, so build on it.
    {"u": "1-12-9", "r": 1, "was": "The head", "set": {"body": B("""
        You learned the main parts of the head in Level 7: رَأْسٌ, عَيْنٌ, أُذُنٌ, أَنْفٌ and فَمٌ. Here they are again with new ones: لِسَانٌ (tongue), شَعْرٌ (hair) and رَقَبَةٌ (neck).
        Parts that come in pairs, like عَيْنٌ and أُذُنٌ, are feminine, so point at one with هَذِهِ.
    """)}},
    {"u": "1-12-9", "r": 1, "e": 4, "was": "هَذَا فَمٌ", "set": {"note": "The plural is أَفْوَاهٌ. \"My mouth\" is فَمِي."}},
    # شُعُورٌ is also the word for "feeling"; leave the plural of hair out.
    {"u": "1-12-9", "w": 2, "was": "شَعْرٌ", "set": {"pl": ""}},
    {"u": "1-12-9", "r": 2, "was": "The body", "set": {"body": B("""
        Learn the parts of the body. Some you know from Level 7.
        صَدْرٌ is the chest, بَطْنٌ the stomach, ظَهْرٌ the back, كَتِفٌ the shoulder, ذِرَاعٌ the arm, إِصْبَعٌ a finger, رِجْلٌ the leg and رُكْبَةٌ the knee. Inside are the قَلْبٌ (heart) and the دَمٌ (blood), and the جِلْدٌ (skin) covers it all. عَقْلٌ is the mind.
    """)}},

    {"u": "1-12-10", "r": 1, "was": "Pairs of body parts", "set": {"body": B("""
        Most body parts that come in pairs are feminine, and two of them take the dual: عَيْنَانِ (two eyes), أُذُنَانِ (two ears), يَدَانِ (two hands), رِجْلَانِ (two legs), قَدَمَانِ (two feet). A describing word for them is dual too.
        With "my", the dual drops its نِ: عَيْنَايَ (my eyes) as a subject, and عَيْنَيَّ after a verb or a small word like بِـ: أَرَى بِعَيْنَيَّ.
    """)}},
    # In English "two black eyes" means bruised eyes.
    {"u": "1-12-10", "r": 1, "e": 1, "was": "لِي عَيْنَانِ سَوْدَاوَانِ", "set": {"en": "I have dark eyes", "note": "Literally \"I have two black eyes\". أَسْوَدُ is black; the feminine is سَوْدَاءُ and its dual is سَوْدَاوَانِ."}},
    {"u": "1-12-10", "q": 2, "was": "How do you say \"I have two black eyes\"?", "set": {"q": "How do you say \"I have dark eyes\" (two black eyes)?"}},
    {"u": "1-12-10", "r": 2, "was": "Senses and pain", "set": {"body": B("""
        The five senses are البَصَرُ (sight), السَّمْعُ (hearing), الشَّمُّ (smell), الذَّوْقُ (taste) and اللَّمْسُ (touch).
        To say where it hurts, use عِنْدِي أَلَمٌ فِي and the body part with "my": عِنْدِي أَلَمٌ فِي رَأْسِي. Or use يُؤْلِمُنِي, "it hurts me": يُؤْلِمُنِي بَطْنِي. For a feminine part, say تُؤْلِمُنِي: تُؤْلِمُنِي رِجْلِي.
    """)}},
    {"u": "1-12-10", "l": 1, "was": "السَّلَامُ عَلَيْكُمْ. مَاذَا بِكَ؟", "set": {"ar": "السَّلَامُ عَلَيْكُمْ. مَا بِكَ؟"}},
    {"u": "1-12-10", "l": 8, "was": "الحَمْدُ لِلَّهِ. هَلْ هَذَا مُهِمٌّ؟", "set": {"ar": "الحَمْدُ لِلَّهِ. هَلْ هَذَا خَطِيرٌ؟"}},

    {"u": "1-12-11", "q": 15, "was": "How do you say \"we love each other\"?", "set": {"a": "يُحِبُّ بَعْضُنَا بَعْضًا", "w": ["يُحِبُّ بَعْضًا بَعْضُنَا", "أُحِبُّ بَعْضُنَا بَعْضًا"]}},
]
