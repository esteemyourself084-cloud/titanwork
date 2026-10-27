# Stage 1 · Level 8 — content corrections and improvements.
GROUPS_ABOUT = "So far you have mostly talked about one person at a time. Now you will talk about groups and pairs. You will learn the words for \"they\", \"you all\" and \"the two of them\", how verbs change for each, and how plural nouns and describing words behave."
MARRIAGE_ABOUT = "Talk about marriage and family life. You will learn marriage words, how to say who married whom with تَزَوَّجَ, how to congratulate and bless a couple, and how to say who must do something with يَجِبُ عَلَى."
FIXES = [
    # This theme used to open Level 3.
    {"u": "1-8-1", "set": {"about": GROUPS_ABOUT}},
    {"u": "1-8-2", "set": {"about": GROUPS_ABOUT}},
    {"u": "1-8-3", "set": {"about": GROUPS_ABOUT}},

    {"u": "1-8-1", "r": 1, "was": "They", "set": {"body": B("""
        هُمْ means "they" for men, or for a mixed group. هُنَّ means "they" for women only.
        In the present, both start with يَـ like the "he" form. For هُمْ the verb ends with ـُونَ, and for هُنَّ it ends with ـْنَ: يَذْهَبُ (he goes), يَذْهَبُونَ (they go), يَذْهَبْنَ (they, women, go).
        When the people are named before the verb, the verb shows the plural: الطُّلَّابُ يَذْهَبُونَ. When the verb comes first, it stays singular: يَذْهَبُ الطُّلَّابُ (the students go).
    """)}},
    {"u": "1-8-1", "r": 1, "e": 3, "was": "هُمْ يَشْرَبُونَ القَهْوَةَ", "set": {"note": "يَشْرَبُ ends with ـُونَ instead of ـُ."}},
    {"u": "1-8-1", "r": 1, "e": 4, "was": "هُنَّ يَشْرَبْنَ الشَّايَ", "set": {"note": "يَشْرَبُ loses its ـُ, and the ب takes a sukoon before ـنَ."}},

    {"u": "1-8-2", "r": 1, "was": "The two of them", "set": {"body": B("""
        Arabic also has a special form for exactly two. The pronoun is هُمَا, for two men, two women or one of each.
        - In the present, the verb ends with ـَانِ: يَذْهَبَانِ. For two women it starts with تَـ: تَذْهَبَانِ.
        - In the past, two men take ـَا and two women take ـَتَا: ذَهَبَا, ذَهَبَتَا.
    """)}},
    {"u": "1-8-2", "r": 2, "was": "You all", "set": {"body": B("""
        أَنْتُمْ means "you" for a group of men or a mixed group, and أَنْتُنَّ is for a group of women.
        - For أَنْتُمْ, the present starts with تَـ and ends with ـُونَ: تَذْهَبُونَ. The past ends with ـْتُمْ: ذَهَبْتُمْ.
        - For أَنْتُنَّ, the verbs are تَذْهَبْنَ and ذَهَبْتُنَّ.
        نَحْنُ (we) is the same for men and women: نَذْهَبُ, ذَهَبْنَا.
    """)}},

    {"u": "1-8-3", "r": 1, "was": "Plural nouns and describing words", "set": {"body": B("""
        A describing word must match its noun.
        - For a plural of people, use a plural describing word: مُعَلِّمُونَ مُجْتَهِدُونَ (hard-working teachers), طَالِبَاتٌ مُجْتَهِدَاتٌ.
        - For a plural of things or animals, use the feminine singular: كُتُبٌ جَدِيدَةٌ (new books), بُيُوتٌ كَبِيرَةٌ (big houses).
        The rule works in sentences too: الكُتُبُ جَدِيدَةٌ (the books are new). It is one of the most used rules in Arabic.
    """)}},
    # جُدُدٌ can describe things in classical Arabic, so it is not a safe wrong answer.
    {"u": "1-8-3", "q": 2, "was": "How do you say \"new books\"?", "set": {"w": ["كُتُبٌ جَدِيدٌ", "كُتُبٌ جَدِيدُونَ"]}},
    {"u": "1-8-3", "q": 4, "was": "How do you say \"the books are new\"?", "set": {"w": ["الكُتُبُ جَدِيدُونَ", "الكُتُبُ جَدِيدٌ"]}},
    # Rashid asked Layla what he himself had done; let them each tell their own day.
    {"u": "1-8-3", "l": 9, "was": "وَنَحْنُ، مَاذَا فَعَلْنَا أَمْسِ؟", "set": {"ar": "وَأَنْتِ، مَاذَا فَعَلْتِ أَمْسِ؟"}},
    {"u": "1-8-3", "l": 10, "was": "أَنْتُمْ ذَهَبْتُمْ", "set": {"ar": "دَرَسْتُ فِي البَيْتِ. وَأَنْتُمْ، مَاذَا فَعَلْتُمْ؟"}},
    {"u": "1-8-3", "l": 11, "was": "شُكْرًا", "set": {"ar": "نَحْنُ ذَهَبْنَا إِلَى السُّوقِ. مَعَ السَّلَامَةِ."}},
    {"u": "1-8-3", "l": 12, "was": "عَفْوًا", "set": {"ar": "مَعَ السَّلَامَةِ."}},

    {"u": "1-8-4", "r": 1, "was": "Healthy habits", "set": {"body": B("""
        عَادَةٌ means "habit". Learn the words of a healthy life.
        صِحِّيٌّ means "healthy". It comes from صِحَّةٌ (health): adding ـِيٌّ makes a describing word, just as with the nationalities in Level 2. For a feminine noun, say صِحِّيَّةٌ.
    """)}},
    {"u": "1-8-4", "r": 1, "e": 4, "was": "نَوْمٌ كَافٍ", "set": {"note": "نَوْمٌ means \"sleep\" and كَافٍ means \"enough\". Like غَالٍ, كَافٍ ends with ـٍ."}},
    {"u": "1-8-4", "r": 2, "was": "You must", "set": {"body": B("""
        يَجِبُ means "it is necessary". Put أَنْ ("that") after it, then a present verb. After أَنْ, the last ـُ of the verb becomes ـَ: تَنَامُ (you sleep), يَجِبُ أَنْ تَنَامَ (you must sleep).
        Verbs that end with ـُونَ or ـِينَ drop their ن after أَنْ: يَدْرُسُونَ becomes أَنْ يَدْرُسُوا, and تَشْرَبِينَ becomes أَنْ تَشْرَبِي.
    """)}},

    {"u": "1-8-5", "r": 1, "was": "You must not", "set": {"body": B("""
        To say "must not", put أَلَّا after يَجِبُ. أَلَّا is أَنْ and لَا joined together, and the verb after it ends with ـَ: يَجِبُ أَلَّا تُدَخِّنَ (you must not smoke).
        Be careful with لَا يَجِبُ. It means "it is not necessary": لَا يَجِبُ أَنْ تَخَافَ is "you do not have to be afraid".
    """)}},
    {"u": "1-8-5", "r": 1, "e": 5, "was": "يَجِبُ أَنْ تَشْرَبَ المَاءَ وَلَا", "set": {"note": "تَشْرَبَ after وَلَا still depends on أَنْ, so it ends with ـَ too."}},
    {"u": "1-8-5", "r": 2, "was": "Better than", "set": {"body": B("""
        To compare two things, use a word on the pattern أَفْعَلُ: كَبِيرٌ gives أَكْبَرُ (bigger), صَغِيرٌ gives أَصْغَرُ (smaller) and كَثِيرٌ gives أَكْثَرُ (more). أَفْضَلُ means "better". Put مِنْ ("than") after it, and the next word ends with ـِ.
        This word does not change for a feminine noun, and it takes no tanween: الفَاكِهَةُ أَفْضَلُ مِنَ الحَلْوَى.
    """)}},
    {"u": "1-8-5", "r": 2, "e": 5, "was": "الرِّيَاضَةُ أَحْسَنُ لِلصِّحَّةِ", "set": {"en": "exercise is better for health"}},
    {"u": "1-8-5", "r": 2, "e": 6, "was": "هَذَا الغِذَاءُ أَكْثَرُ فَائِدَةً", "set": {"note": "أَكْثَرُ فَائِدَةً means \"more useful\", literally \"more in benefit\". The noun after أَكْثَرُ ends with ـًا. فَائِدَةٌ means \"benefit\"."}},

    {"u": "1-8-6", "r": 1, "was": "A check-up", "set": {"body": B("""
        فَحْصٌ means "examination", and فَحْصٌ طِبِّيٌّ is a medical check-up. Many people have one every year. تَطْعِيمٌ means "vaccination", and تَحْلِيلٌ is a lab test, such as a blood test.
    """)}},
    {"u": "1-8-6", "r": 1, "e": 2, "was": "هَلْ أَخَذْتَ التَّطْعِيمَ؟", "set": {"en": "did you get the vaccination? (to a man)"}},
    {"u": "1-8-6", "w": 2, "was": "تَطْعِيمٌ", "set": {"en": "vaccination"}},
    {"u": "1-8-6", "q": 1, "was": "Which word means \"vaccine\"?", "set": {"q": "Which word means \"vaccination\"?"}},
    {"u": "1-8-6", "q": 3, "was": "How do you say \"did you take the vaccine?\" to a man?", "set": {"q": "How do you ask a man \"Did you get the vaccination?\""}},
    # The course negates the present with لَا.
    {"u": "1-8-6", "l": 4, "was": "لَا، مَا أُمَارِسُ", "set": {"ar": "لَا، لَا أُمَارِسُ الرِّيَاضَةَ. أَنَا مَشْغُولٌ."}},

    # "Free time" was already a topic in Level 6; this lesson is about places to relax.
    {"u": "1-8-7", "set": {"titleEn": "Places to relax · In order to", "titleAr": "أَمَاكِنُ الرَّاحَةِ · لِـ"}},
    {"u": "1-8-7", "r": 1, "was": "Free time and places to relax", "set": {"title": "Places to relax (أَمَاكِنُ الرَّاحَةِ)", "body": B("""
        You know وَقْتُ الفَرَاغِ (free time) from Level 6. رَاحَةٌ means "rest". Learn some places people go to relax.
        Many of them start with مَـ, "the place of": مَلْعَبٌ (sports ground) comes from لَعِبَ (he played), and مَقْهًى (café) comes from قَهْوَةٌ (coffee).
    """)}},
    {"u": "1-8-7", "r": 1, "e": 1, "was": "وَقْتُ الفَرَاغِ", "set": {"note": "You learned this in Level 6. It is an إِضَافَةٌ: two nouns side by side."}},
    {"u": "1-8-7", "r": 1, "e": 7, "was": "هَذَا نَادٍ", "set": {"note": "Its plural is نَوَادٍ. Like غَالٍ it ends with ـٍ, and with اَلْ it is النَّادِي."}},
    {"u": "1-8-7", "r": 2, "was": "In order to", "set": {"body": B("""
        لِـ before a present verb means "in order to". The verb's last ـُ becomes ـَ, as after أَنْ: أَذْهَبُ إِلَى الحَدِيقَةِ لِأَرْتَاحَ (I go to the park to relax).
        Before a noun, لِـ means "for", as in لِلْعُمْرَةِ (for Umrah).
    """)}},
    # رَاحَ means "he went"; rest is رَاحَةٌ.
    {"u": "1-8-7", "r": 2, "e": 1, "was": "أَذْهَبُ إِلَى الحَدِيقَةِ لِأَرْتَاحَ", "set": {"note": "لِـ joins to أَرْتَاحَ. أَرْتَاحُ means \"I rest\", from the same root as رَاحَةٌ (rest)."}},
    {"u": "1-8-7", "r": 2, "e": 7, "was": "لِأَقْضِيَ وَقْتًا", "set": {"note": "After لِـ, the final ي of أَقْضِي takes ـَ: لِأَقْضِيَ. أَصْدِقَائِي is \"my friends\"."}},

    {"u": "1-8-8", "r": 1, "was": "When", "set": {"body": B("""
        عِنْدَمَا means "when" in a statement. To ask "when?", use مَتَى.
        - After عِنْدَمَا, use the past for something that happened: عِنْدَمَا وَصَلْنَا (when we arrived).
        - Use the present for something that usually happens: عِنْدَمَا أَكُونُ مُتْعَبًا، أَنَامُ (when I am tired, I sleep). أَكُونُ is the present of كَانَ.
        إِذَا means "if". The verb after it is usually in the past form, but the meaning is present or future: إِذَا ذَهَبْتَ (if you go).
    """)}},
    {"u": "1-8-8", "r": 1, "e": 3, "was": "عِنْدَمَا أَكُونُ مُتْعَبًا", "set": {"note": "أَكُونُ (I am) is the present of كَانَ, so مُتْعَبٌ becomes مُتْعَبًا after it."}},
    {"u": "1-8-8", "r": 1, "e": 4, "was": "إِذَا ذَهَبْتَ إِلَى النَّادِي", "set": {"note": "ذَهَبْتَ looks past, but after إِذَا it means \"you go\". مَعَكَ means \"with you\"."}},
    {"u": "1-8-8", "r": 1, "e": 7, "was": "أَذْهَبُ عِنْدَمَا أَكُونُ فَارِغًا", "set": {"note": "فَارِغٌ means \"free\" or \"empty\". After أَكُونُ it becomes فَارِغًا."}},
    {"u": "1-8-8", "r": 2, "was": "I used to", "set": {"body": B("""
        To say what you used to do, put كَانَ before a present verb: أَلْعَبُ (I play), كُنْتُ أَلْعَبُ (I used to play).
        Both verbs change for the person: كُنْتُ أَلْعَبُ (I), كَانَ يَلْعَبُ (he), كَانَتْ تَلْعَبُ (she), كُنَّا نَلْعَبُ (we). Like زَارَ, كَانَ drops its long ا with "I", "you" and "we": كُنْتُ, كُنْتَ, كُنَّا.
    """)}},
    {"u": "1-8-8", "r": 2, "e": 1, "was": "كُنْتُ أَلْعَبُ كُرَةَ القَدَمِ", "set": {"note": "كُنْتُ is \"I was\". With أَلْعَبُ after it, it means \"I used to play\"."}},

    {"u": "1-8-9", "set": {"about": MARRIAGE_ABOUT}},
    {"u": "1-8-10", "set": {"about": MARRIAGE_ABOUT}},
    {"u": "1-8-9", "r": 1, "was": "Marriage words", "set": {"body": B("""
        زَوَاجٌ means "marriage". You met زَوْجٌ (husband) and زَوْجَةٌ (wife) in Level 2.
        On the wedding day the man is called عَرِيسٌ (groom) and the woman عَرُوسٌ (bride). عَرُوسٌ is feminine even without ـَةٌ, so point at her with هَذِهِ.
    """)}},
    {"u": "1-8-9", "r": 1, "e": 6, "was": "هَذِهِ حَفْلَةُ الزَّوَاجِ", "set": {"note": "This is an إِضَافَةٌ: \"the party of the marriage\". حَفْلَةٌ means \"party\"."}},
    # A mahr is given by the husband to the wife, which "dowry" does not convey.
    {"u": "1-8-9", "r": 1, "e": 7, "was": "هَذَا مَهْرٌ", "set": {"en": "this is a mahr (bridal gift)", "note": "The مَهْرٌ is the gift that the husband must give his wife at marriage."}},
    {"u": "1-8-9", "r": 1, "e": 8, "was": "هَذِهِ خِطْبَةٌ", "set": {"note": "خِطْبَةٌ is the promise to marry. Do not mix it up with خُطْبَةٌ, a sermon."}},
    {"u": "1-8-9", "w": 5, "was": "مَهْرٌ", "set": {"en": "mahr, bridal gift"}},
    # The old text said "no extra word" and then used مِنْ; both ways are correct.
    {"u": "1-8-9", "r": 2, "was": "Getting married", "set": {"body": B("""
        تَزَوَّجَ means "he married", and its present is يَتَزَوَّجُ. To say whom, put the person straight after the verb, or add مِنْ: تَزَوَّجَ فَاطِمَةَ and تَزَوَّجَ مِنْ فَاطِمَةَ are both correct.
        خَطَبَ means "he got engaged to". It takes the person directly, with no مِنْ: خَطَبَ فَاطِمَةَ.
    """)}},
    {"u": "1-8-9", "r": 2, "e": 3, "was": "تَزَوَّجَ أَخِي مِنْ فَاطِمَةَ", "set": {"tr": "tazawwaja akhī min fāṭimata", "note": "Names like فَاطِمَةُ take no tanween. After مِنْ they end with ـَ, not ـِ, just like مَكَّةَ."}},
    {"u": "1-8-9", "r": 2, "e": 4, "was": "خَطَبَ أَخِي فَاطِمَةَ", "set": {"tr": "khaṭaba akhī fāṭimata"}},
    {"u": "1-8-9", "r": 2, "e": 7, "was": "سَأَتَزَوَّجُ بَعْدَ سَنَةٍ", "set": {"tr": "saʾatazawwaju baʿda sanatin, in shāʾa llāhu", "en": "I will get married in a year, if Allah wills", "note": "سَأَتَزَوَّجُ is سَـ with أَتَزَوَّجُ: \"I will get married\"."}},

    # "Must" was taught twice in this level; the second lesson now covers who must, with عَلَى.
    {"u": "1-8-10", "set": {"titleEn": "Congratulations and blessings · Who must?", "titleAr": "التَّهْنِئَةُ وَالدُّعَاءُ · يَجِبُ عَلَى"}},
    {"u": "1-8-10", "r": 1, "was": "Congratulations and blessings", "set": {"body": B("""
        مَبْرُوكٌ means "congratulations", literally "blessed". At a wedding people bless the couple, so they speak to two people. The ending for "you two" is ـكُمَا: لَكُمَا (for you two), بَيْنَكُمَا (between you two). For a group it is ـكُمْ: فِيكُمْ.
    """)}},
    {"u": "1-8-10", "r": 1, "e": 1, "was": "مَبْرُوكٌ!", "set": {"note": "People say it for a wedding, a new baby, a new home or a success."}},
    {"u": "1-8-10", "r": 1, "e": 2, "was": "بَارَكَ اللَّهُ لَكُمَا", "set": {"note": "بَارَكَ means \"he blessed\". The verb looks past, but the phrase is a wish. لَكُمَا means \"for you two\"."}},
    {"u": "1-8-10", "r": 1, "e": 3, "was": "جَمَعَ اللَّهُ بَيْنَكُمَا", "set": {"note": "The Prophet ﷺ used to say to a man who had just married: بَارَكَ اللَّهُ لَكَ، وَبَارَكَ عَلَيْكَ، وَجَمَعَ بَيْنَكُمَا فِي خَيْرٍ."}},
    {"u": "1-8-10", "r": 1, "e": 4, "was": "أَلْفُ مَبْرُوكٍ", "set": {"note": "أَلْفٌ (a thousand) joins مَبْرُوكٍ in an إِضَافَةٌ, like أَلْفُ رِيَالٍ."}},
    {"u": "1-8-10", "r": 2, "was": "Must", "set": {"title": "Who must? (يَجِبُ عَلَى)", "body": B("""
        You know يَجِبُ أَنْ from the health lessons. To say who must, add عَلَى with an ending for the person.
        - عَلَيَّ (on me): يَجِبُ عَلَيَّ أَنْ أَعْمَلَ means "I must work", literally "it is necessary on me that I work".
        - عَلَيْكَ (on you), عَلَيْهِ (on him), عَلَيْهَا (on her), عَلَيْنَا (on us).
        The verb after أَنْ still ends with ـَ, and it matches the person.
    """)}},
    # لَا يَجِبُ means "do not have to"; "must not" is يَجِبُ أَلَّا.
    {"u": "1-8-10", "r": 2, "e": 5, "was": "لَا يَجِبُ أَنْ نَغْضَبَ", "set": {"ar": "يَجِبُ أَلَّا نَغْضَبَ", "tr": "yajibu allā naghḍaba", "note": "غَضِبَ means \"he got angry\". For \"must not\" use أَلَّا; لَا يَجِبُ would mean \"we do not have to\"."}},
    {"u": "1-8-10", "q": 9, "was": "How do you say \"we must not get angry\"?", "set": {"a": "يَجِبُ أَلَّا نَغْضَبَ", "w": ["لَا يَجِبُ أَنْ نَغْضَبَ", "يَجِبُ أَنْ نَغْضَبَ"]}},
    {"u": "1-8-10", "l": 4, "was": "تَزَوَّجْتُ الْيَوْمَ", "set": {"ar": "تَزَوَّجْتُ اليَوْمَ. هَذِهِ حَفْلَةُ الزَّوَاجِ."}},
    {"u": "1-8-10", "l": 5, "was": "مَنْ العَرُوسُ؟", "set": {"ar": "مَنِ العَرُوسُ؟"}},
    {"u": "1-8-10", "cq": 2, "was": "When did Majid get married?", "set": {"a": "اليَوْمَ"}},
    {"u": "1-8-10", "cq": 5, "was": "When did Majid get engaged to her?", "set": {"w": ["بَعْدَ سَنَةٍ", "اليَوْمَ"]}},

    {"u": "1-8-11", "r": 1, "e": 4, "was": "تَزَوَّجَ أَخِي مِنْ فَاطِمَةَ", "set": {"tr": "tazawwaja akhī min fāṭimata"}},
    {"u": "1-8-11", "r": 1, "e": 6, "was": "يَجِبُ عَلَيَّ أَنْ أَعْمَلَ", "set": {"note": "يَجِبُ عَلَيَّ أَنْ means \"I must\"."}},
]
