# Stage 1 · Level 9 — content corrections and improvements.
FIXES = [
    {"u": "1-9-1", "r": 1, "was": "Places in the city", "set": {"body": B("""
        You know مَدِينَةٌ (city), شَارِعٌ (street), مَطَارٌ (airport) and مَحَطَّةٌ (station). Learn more words for city life: قَرْيَةٌ (village), مَيْدَانٌ (square) and جِسْرٌ (bridge), and the words for its crowds and noise.
    """)}},
    {"u": "1-9-1", "r": 2, "was": "Traffic and waiting", "set": {"body": B("""
        Learn the verbs for getting around. رَكِبَ means "he rode" or "he got on", and اِنْتَظَرَ means "he waited". وَقَفَ, which you know as "he stood", also means "he stopped". Their present forms are يَرْكَبُ, يَنْتَظِرُ and يَقِفُ.
        The thing you ride and the person you wait for come straight after the verb: أَرْكَبُ الحَافِلَةَ (I ride the bus), أَنْتَظِرُ صَدِيقِي (I wait for my friend).
    """)}},
    {"u": "1-9-1", "r": 2, "e": 2, "was": "وَقَفَتِ السَّيَّارَةُ", "set": {"note": "The verb takes ـتْ because السَّيَّارَةُ is feminine. Before اَلْ the تْ becomes تِ: وَقَفَتِ."}},
    {"u": "1-9-1", "r": 2, "e": 3, "was": "نَنْتَظِرُ فِي المَحَطَّةِ", "set": {"note": "نَنْتَظِرُ is \"we wait\". There is no word for \"for\": نَنْتَظِرُ أَخِي is \"we wait for my brother\"."}},

    # Comparatives were introduced in Level 8; this lesson shows how to make them.
    {"u": "1-9-2", "r": 1, "was": "Bigger, better", "set": {"body": B("""
        You learned أَفْضَلُ مِنْ in Level 8. You can make this form from most describing words: put their three root letters in the pattern أَفْعَلُ.
        - كَبِيرٌ (big) gives أَكْبَرُ (bigger).
        - جَمِيلٌ (beautiful) gives أَجْمَلُ (more beautiful).
        - سَرِيعٌ (fast) gives أَسْرَعُ (faster).
        - رَخِيصٌ (cheap) gives أَرْخَصُ (cheaper).
        These words do not change for masculine or feminine, and they take no tanween.
    """)}},
    # Jeddah is written جُدَّةُ everywhere else in the course; جَدَّةٌ is "grandmother".
    {"u": "1-9-2", "r": 1, "e": 1, "was": "الرِّيَاضُ أَكْبَرُ مِنْ جَدَّةَ", "set": {"ar": "الرِّيَاضُ أَكْبَرُ مِنْ جُدَّةَ", "tr": "ar-riyāḍu akbaru min juddata", "note": "Like most city names, جُدَّةُ takes no tanween, so after مِنْ it ends with ـَ."}},
    {"u": "1-9-2", "r": 1, "e": 5, "was": "أَيُّ مَدِينَةٍ أَجْمَلُ؟", "set": {"note": "أَيُّ means \"which\". The noun after it is singular and ends with ـٍ: أَيُّ مَدِينَةٍ."}},
    {"u": "1-9-2", "r": 1, "e": 6, "was": "مَكَّةُ أَجْمَلُ مَدِينَةٍ", "set": {"note": "أَجْمَلُ before a singular noun ending in ـٍ means \"the most beautiful\". The next lesson shows how."}},
    {"u": "1-9-2", "r": 2, "was": "The most", "set": {"body": B("""
        To say "the biggest", put أَكْبَرُ before a singular noun ending with ـٍ: أَكْبَرُ مَدِينَةٍ (the biggest city). The two words make an إِضَافَةٌ.
        You can also use اَلْ: الأَكْبَرُ means "the biggest one". هَذَا الشَّارِعُ هُوَ الأَطْوَلُ means "this street is the longest".
    """)}},
    {"u": "1-9-2", "q": 4, "was": "How do you say \"Riyadh is bigger than Jeddah\"?", "set": {"a": "الرِّيَاضُ أَكْبَرُ مِنْ جُدَّةَ", "w": ["الرِّيَاضُ كَبِيرٌ مِنْ جُدَّةَ", "جُدَّةُ أَكْبَرُ مِنَ الرِّيَاضِ"]}},
    {"u": "1-9-2", "cq": 2, "was": "Where is Ali from?", "set": {"a": "مِنْ قَرْيَةٍ صَغِيرَةٍ", "w": ["مِنْ مَدِينَةٍ كَبِيرَةٍ", "مِنْ مَدِينَةٍ جَمِيلَةٍ"]}},

    {"u": "1-9-3", "r": 1, "was": "University words", "set": {"body": B("""
        You know مَدْرَسَةٌ (school), جَامِعَةٌ (university) and مَكْتَبَةٌ (library). Learn the words of university life. Many of them are feminine with ـَةٌ, so point at them with هَذِهِ.
    """)}},
    {"u": "1-9-3", "r": 1, "e": 4, "was": "هَذَا طَالِبٌ جَامِعِيٌّ", "set": {"note": "جَامِعِيٌّ means \"of the university\". Like صِحِّيٌّ, it is made with ـِيٌّ."}},
    {"u": "1-9-3", "r": 2, "was": "Learning and teaching", "set": {"body": B("""
        Three verbs come from the root ع ل م, like عِلْمٌ (knowledge) and مُعَلِّمٌ (teacher).
        - عَلِمَ means "he knew": أَعْلَمُ (I know).
        - عَلَّمَ, with a doubled ل, means "he taught": أُعَلِّمُ (I teach).
        - تَعَلَّمَ means "he learned": أَتَعَلَّمُ (I learn).
        To say what you know, use أَنَّ ("that"). The noun after أَنَّ ends with ـَ: أَعْلَمُ أَنَّ الامْتِحَانَ صَعْبٌ.
    """)}},
    {"u": "1-9-3", "r": 2, "e": 6, "was": "دَرَسْتُ فِي الجَامِعَةِ", "set": {"note": "You know دَرَسْتُ (I studied) from Level 5."}},

    {"u": "1-9-4", "r": 1, "was": "Who, which", "set": {"body": B("""
        الَّذِي means "who" or "which" for a masculine singular noun, and الَّتِي is for a feminine singular noun. Use them only after a noun with اَلْ, to add more information: الطَّالِبُ نَجَحَ (the student passed), الطَّالِبُ الَّذِي نَجَحَ (the student who passed).
        If the noun is the object in the new part, the verb gets an ending that points back to it: الكِتَابُ الَّذِي قَرَأْتُهُ, literally "the book which I read it".
    """)}},

    {"u": "1-9-5", "r": 1, "was": "Professions", "set": {"body": B("""
        A profession is مِهْنَةٌ, and its plural is مِهَنٌ. You know طَبِيبٌ and مُعَلِّمٌ from Level 2. Now learn more.
        Some words end with ـٍ when they have no اَلْ, like مُحَامٍ (lawyer). With اَلْ the ي comes back: المُحَامِي. You saw the same with غَالٍ and نَادٍ.
    """)}},
    {"u": "1-9-5", "r": 1, "e": 4, "was": "هَذَا صَيْدَلِيٌّ", "set": {"note": "A صَيْدَلِيٌّ works in a صَيْدَلِيَّةٌ (pharmacy). The plural is صَيَادِلَةٌ."}},
    # شُرْطَةٌ is the police force, not the plural of شُرْطِيٌّ.
    {"u": "1-9-5", "r": 1, "e": 6, "was": "هَذَا شُرْطِيٌّ", "set": {"note": "شُرْطِيٌّ is one police officer, and the plural is شُرْطِيُّونَ. The police force is الشُّرْطَةُ."}},
    {"u": "1-9-5", "r": 1, "e": 8, "was": "هَذَا مُدِيرٌ", "set": {"note": "The plural is مُدِيرُونَ; you will also hear مُدَرَاءُ. A woman manager is مُدِيرَةٌ."}},
    {"u": "1-9-5", "r": 1, "e": 9, "was": "هَذَا صَحَفِيٌّ", "set": {"note": "It comes from صَحِيفَةٌ, \"newspaper\"."}},
    {"u": "1-9-5", "w": 6, "was": "مُدِيرٌ", "set": {"pl": "مُدِيرُونَ"}},
    {"u": "1-9-5", "r": 2, "was": "Working as", "set": {"body": B("""
        أَعْمَلُ means "I work". To say what job you do, put كَـ ("as") before the job: أَعْمَلُ كَمُهَنْدِسٍ. The job ends with ـٍ. You can also simply say أَنَا مُهَنْدِسٌ. The place of work comes after فِي.
        Ask مَاذَا تَعْمَلُ؟ (what do you do?) and أَيْنَ تَعْمَلُ؟ (where do you work?).
    """)}},
    {"u": "1-9-5", "r": 2, "e": 6, "was": "أُرِيدُ أَنْ أَكُونَ طَبِيبًا", "set": {"note": "أَكُونُ becomes أَكُونَ after أَنْ, and the job after it ends with ـًا, just as after كَانَ."}},

    # "A person's age and experience use خِبْرَةٌ" was wrong.
    {"u": "1-9-6", "r": 1, "was": "Interview and salary", "set": {"body": B("""
        وَظِيفَةٌ is a job or post. To look for one, say أَبْحَثُ عَنْ وَظِيفَةٍ. When you apply (قَدَّمْتُ عَلَى وَظِيفَةٍ, "I applied for a job"), you may have an interview, مُقَابَلَةٌ.
        Employers ask about your خِبْرَةٌ (experience), and a job pays a رَاتِبٌ (salary).
    """)}},
    {"u": "1-9-6", "r": 2, "was": "Describing a state", "set": {"body": B("""
        To say what state someone is in while they do something, add a describing word ending in ـًا. This is called الحَالُ: دَخَلَ مُبْتَسِمًا (he came in smiling).
        - The word has no اَلْ and ends with ـًا, or ـَةً for a woman: جَاءَتْ مُسْرِعَةً (she came hurrying).
        - Compare: خَرَجَ المُهَنْدِسُ الغَاضِبُ is "the angry engineer went out", but خَرَجَ المُهَنْدِسُ غَاضِبًا is "the engineer went out angry".
    """)}},
    {"u": "1-9-6", "r": 2, "e": 4, "was": "عَادَ الطَّيَّارُ مُتْعَبًا", "set": {"note": "عَادَ means \"he came back\". Like زَارَ, it drops its ا with \"I\": عُدْتُ."}},
    # The manager asked about experience Sami had just mentioned; ask about his degree instead.
    {"u": "1-9-6", "l": 7, "was": "هَلْ عِنْدَكَ خِبْرَةٌ؟", "set": {"ar": "مَا شَاءَ اللَّهُ. هَلْ عِنْدَكَ شَهَادَةٌ جَامِعِيَّةٌ؟"}},
    {"u": "1-9-6", "l": 8, "was": "نَعَمْ، عِنْدِي خِبْرَةٌ", "set": {"ar": "نَعَمْ، دَرَسْتُ فِي الجَامِعَةِ أَرْبَعَ سَنَوَاتٍ."}},

    {"u": "1-9-7", "r": 2, "was": "Grammar words", "set": {"body": B("""
        You met these ideas in Level 1. Arabic words are of three types: اِسْمٌ (a noun), فِعْلٌ (a verb) and حَرْفٌ (a particle). A sentence that starts with a verb is a جُمْلَةٌ فِعْلِيَّةٌ, and one that starts with a noun is a جُمْلَةٌ اسْمِيَّةٌ.
        The endings of a noun have names too: مَرْفُوعٌ (ending in ـُ), مَنْصُوبٌ (ending in ـَ) and مَجْرُورٌ (ending in ـِ).
    """)}},
    # A doer (فَاعِلٌ) belongs to a verb sentence, not a noun sentence.
    {"u": "1-9-8", "l": 6, "was": "هَلْ هَذِهِ جُمْلَةٌ اسْمِيَّةٌ؟", "set": {"ar": "هَلْ هَذِهِ جُمْلَةٌ فِعْلِيَّةٌ؟"}},
    {"u": "1-9-8", "cq": 7, "was": "What kind of sentence is it?", "set": {"a": "جُمْلَةٌ فِعْلِيَّةٌ", "w": ["جُمْلَةٌ اسْمِيَّةٌ", "جُمْلَةٌ قَصِيرَةٌ"]}},

    {"u": "1-9-8", "r": 1, "was": "I can", "set": {"body": B("""
        أَسْتَطِيعُ أَنْ means "I can". The verb after أَنْ ends with ـَ, as you learned with يَجِبُ أَنْ. تَسْتَطِيعُ is "you can" and يَسْتَطِيعُ is "he can". Put لَا before it for "cannot": لَا أَسْتَطِيعُ.
    """)}},
    {"u": "1-9-8", "r": 1, "e": 5, "was": "لَمْ أَفْهَمْ هَذِهِ الجُمْلَةَ", "set": {"note": "فَهِمَ means \"he understood\". After لَمْ the present form ends with a sukoon and means the past, as in لَمْ أُسَافِرْ."}},
    {"u": "1-9-8", "w": 0, "add": {"ar": "فَهِمَ", "pl": "يَفْهَمُ", "en": "to understand", "type": "verb"}},
    {"u": "1-9-8", "r": 2, "was": "How?", "set": {"body": B("""
        To say how something is done, put بِـ ("with") before a noun that ends with ـٍ: بِسُرْعَةٍ, "with speed", means "quickly". The phrase usually comes at the end of the sentence.
        Learn بِسُرْعَةٍ (quickly), بِبُطْءٍ (slowly), بِوُضُوحٍ (clearly) and بِطَلَاقَةٍ (fluently).
    """)}},
    {"u": "1-9-8", "r": 2, "e": 2, "was": "يَتَكَلَّمُ العَرَبِيَّةَ بِطَلَاقَةٍ", "set": {"note": "The بِـ phrase comes at the end."}},

    {"u": "1-9-9", "r": 1, "e": 1, "was": "هَذِهِ جَائِزَةٌ كَبِيرَةٌ", "set": {"note": "The hamza sits on a seat shaped like ي: ئ. The plural is جَوَائِزُ."}},
    {"u": "1-9-9", "r": 1, "e": 5, "was": "هَذِهِ مِيدَالِيَّةٌ ذَهَبِيَّةٌ", "set": {"note": "ذَهَبِيٌّ means \"gold\", from ذَهَبٌ. فِضِّيٌّ means \"silver\", from فِضَّةٌ."}},
    {"u": "1-9-9", "r": 2, "was": "Winning", "set": {"body": B("""
        فَازَ means "he won" and يَفُوزُ is "he wins". What you win comes after بِـ: فَازَ بِجَائِزَةٍ. Like زَارَ, it drops its ا with "I": فُزْتُ (I won).
        خَسِرَ means "he lost" (يَخْسَرُ, "he loses"). شَارَكَ means "he took part" (يُشَارِكُ), and it takes فِي: شَارَكْتُ فِي المُسَابَقَةِ.
    """)}},
    {"u": "1-9-9", "r": 2, "e": 6, "was": "لَمْ أَفُزْ", "set": {"note": "After لَمْ the verb ends with a sukoon, and the long و drops: أَفُزْ, not أَفُوزُ."}},

    {"u": "1-9-10", "r": 1, "was": "First, second, third", "set": {"body": B("""
        You met the feminine ordinals with the time in Level 6: السَّاعَةُ الثَّالِثَةُ. Here are both forms. Like any describing word, they come after the noun and agree with it.
        - الأَوَّلُ and الأُولَى (first)
        - الثَّانِي and الثَّانِيَةُ (second)
        - الثَّالِثُ and الثَّالِثَةُ (third)
        - الرَّابِعُ and الرَّابِعَةُ (fourth)
        - الخَامِسُ and الخَامِسَةُ (fifth)
    """)}},
    {"u": "1-9-10", "r": 1, "e": 4, "was": "المَرْكَزُ الثَّالِثُ", "set": {"note": "مَرْكَزٌ is masculine, so use الثَّالِثُ."}},
    {"u": "1-9-10", "r": 2, "was": "Congratulating", "set": {"body": B("""
        هَنَّأَ means "he congratulated". أُهَنِّئُكَ is "I congratulate you" to a man, and أُهَنِّئُكِ is to a woman. After it, say عَلَى and the reason: أُهَنِّئُكَ عَلَى الفَوْزِ. تَهْنِئَةٌ means "congratulation", and you can always simply say مَبْرُوكٌ.
    """)}},
    {"u": "1-9-10", "r": 2, "e": 3, "was": "تَهَانِينَا", "set": {"note": "تَهَانِي is the plural of تَهْنِئَةٌ, and ـنَا means \"our\"."}},
    {"u": "1-9-10", "l": 6, "was": "فِي المَرْكَزِ الأَوَّلِ", "set": {"ar": "فِي المَرْكَزِ الأَوَّلِ. وَأَنْتَ، هَلْ شَارَكْتَ فِي المُسَابَقَةِ؟"}},

    {"u": "1-9-11", "r": 1, "e": 1, "was": "الرِّيَاضُ أَكْبَرُ مِنْ جَدَّةَ", "set": {"ar": "الرِّيَاضُ أَكْبَرُ مِنْ جُدَّةَ", "tr": "ar-riyāḍu akbaru min juddata"}},
    {"u": "1-9-11", "q": 1, "was": "How do you say \"Riyadh is bigger than Jeddah\"?", "set": {"a": "الرِّيَاضُ أَكْبَرُ مِنْ جُدَّةَ", "w": ["الرِّيَاضُ كَبِيرٌ مِنْ جُدَّةَ", "جُدَّةُ أَكْبَرُ مِنَ الرِّيَاضِ"]}},
]
