# Stage 1 · Level 11 (was Stage 2 · Level 2) — content corrections and improvements.
FIXES = [
    {"u": "1-11-1", "r": 1, "was": "Countries and capitals", "set": {"body": B("""
        بَلَدٌ is a country or a town (plural بِلَادٌ). عَاصِمَةٌ is a capital, and شَعْبٌ is a people. The Islamic world stretches over many countries.
        Some country names have اَلْ, like السُّعُودِيَّةُ and المَغْرِبُ, and some do not, like مِصْرُ and تُرْكِيَا. Names without اَلْ, like مِصْرُ, take no tanween.
    """)}},
    {"u": "1-11-1", "r": 1, "e": 3, "was": "عَاصِمَةُ السُّعُودِيَّةِ الرِّيَاضُ", "set": {"note": "عَاصِمَةُ السُّعُودِيَّةِ is an إِضَافَةٌ: \"the capital of Saudi Arabia\"."}},
    {"u": "1-11-1", "r": 1, "e": 6, "was": "عَاصِمَةُ إِنْدُونِيسِيَا جَاكَرْتَا", "set": {"note": "Indonesia has more Muslims than any other country."}},
    {"u": "1-11-1", "r": 2, "was": "Directions and nationality", "set": {"body": B("""
        شَرْقٌ is east, غَرْبٌ is west, شِمَالٌ is north and جَنُوبٌ is south. After فِي they end with ـِ: فِي شِمَالِ السُّعُودِيَّةِ.
        You made nationality words with ـِيٌّ in Level 2: مِصْرُ gives مِصْرِيٌّ, and تُرْكِيَا drops its final ا to give تُرْكِيٌّ. A woman is مِصْرِيَّةٌ, and the plural is مِصْرِيُّونَ.
    """)}},
    # Ankara is in central Turkey, so "north" now uses Tabuk.
    {"u": "1-11-1", "r": 2, "e": 1, "was": "أَنْقَرَةُ فِي شِمَالِ تُرْكِيَا", "set": {"ar": "تَبُوكُ فِي شِمَالِ السُّعُودِيَّةِ", "tr": "tabūku fī shimāli s-suʿūdiyyati", "en": "Tabuk is in the north of Saudi Arabia", "note": "شِمَالٌ becomes شِمَالِ after فِي."}},
    {"u": "1-11-1", "r": 2, "e": 2, "was": "جَدَّةُ فِي غَرْبِ السُّعُودِيَّةِ", "set": {"ar": "جُدَّةُ فِي غَرْبِ السُّعُودِيَّةِ", "tr": "juddatu fī gharbi s-suʿūdiyyati"}},
    {"u": "1-11-1", "r": 2, "e": 6, "was": "هِيَ تُرْكِيَّةٌ", "set": {"note": "تُرْكِيَا drops its final ا before ـِيٌّ, and a woman takes ـِيَّةٌ: تُرْكِيَّةٌ."}},
    {"u": "1-11-1", "q": 10, "was": "How do you say \"Ankara is in the north of Turkey\"?", "set": {"q": "How do you say \"Tabuk is in the north of Saudi Arabia\"?", "a": "تَبُوكُ فِي شِمَالِ السُّعُودِيَّةِ", "w": ["تَبُوكُ فِي جَنُوبِ السُّعُودِيَّةِ", "تَبُوكُ شِمَالٌ السُّعُودِيَّةَ"]}},
    {"u": "1-11-1", "q": 11, "was": "How do you say \"Jeddah is in the west of Saudi Arabia\"?", "set": {"a": "جُدَّةُ فِي غَرْبِ السُّعُودِيَّةِ", "w": ["جُدَّةُ فِي شَرْقِ السُّعُودِيَّةِ", "جُدَّةُ غَرْبُ السُّعُودِيَّةِ"]}},

    {"u": "1-11-2", "r": 1, "was": "History and civilisation", "set": {"body": B("""
        تَارِيخٌ is history, and it also means "date". حَضَارَةٌ is civilisation, and عِلْمٌ is knowledge or science. Islamic civilisation gave much to the world.
        To say "from... to...", use مِنْ and إِلَى: مِنَ الشَّرْقِ إِلَى الغَرْبِ. To say "the oldest" or "the largest", put أَفْعَلُ before a singular noun ending in ـٍ, as you learned in Level 9: أَكْبَرُ بَلَدٍ.
    """)}},
    {"u": "1-11-2", "r": 1, "e": 3, "was": "اِنْتَشَرَ الإِسْلَامُ مِنَ الجَزِيرَةِ", "set": {"note": "جَزِيرَةٌ is a peninsula or an island. Here الجَزِيرَةُ is the Arabian Peninsula."}},
    # Al-Azhar is one of the oldest universities, not the oldest (al-Qarawiyyin is older).
    {"u": "1-11-2", "r": 1, "e": 5, "was": "الأَزْهَرُ أَقْدَمُ جَامِعَةٍ", "set": {"ar": "الأَزْهَرُ مِنْ أَقْدَمِ الجَامِعَاتِ", "tr": "al-azharu min aqdami l-jāmiʿāti", "en": "Al-Azhar is one of the oldest universities", "note": "مِنْ أَقْدَمِ الجَامِعَاتِ means \"one of the oldest universities\": مِنْ, then أَفْعَلُ before a plural with اَلْ."}},
    {"u": "1-11-2", "r": 1, "e": 6, "was": "أَكْبَرُ بَلَدٍ مُسْلِمٍ إِنْدُونِيسِيَا", "set": {"note": "أَكْبَرُ before a singular noun ending in ـٍ means \"the largest\". Indonesia has the most Muslims of any country."}},
    {"u": "1-11-2", "q": 6, "was": "How do you say \"Al-Azhar is the oldest university\"?", "set": {"q": "How do you say \"Al-Azhar is one of the oldest universities\"?", "a": "الأَزْهَرُ مِنْ أَقْدَمِ الجَامِعَاتِ", "w": ["الأَزْهَرُ مِنْ أَقْدَمُ الجَامِعَاتِ", "الأَزْهَرُ أَقْدَمُ مِنَ الجَامِعَاتِ"]}},
    {"u": "1-11-2", "r": 2, "was": "Languages of the Islamic world", "set": {"body": B("""
        Many Muslim peoples speak their own language and use Arabic for prayer and the Quran.
        The name of a language is the feminine form of the nationality, with اَلْ: التُّرْكِيَّةُ (Turkish), العَرَبِيَّةُ (Arabic). تَكَلَّمَ takes the language as its object: يَتَكَلَّمُونَ التُّرْكِيَّةَ (they speak Turkish).
    """)}},
    {"u": "1-11-2", "r": 2, "e": 3, "was": "مَاذَا يَتَكَلَّمُونَ فِي إِنْدُونِيسِيَا؟", "set": {"note": "They speak Indonesian, الإِنْدُونِيسِيَّةُ."}},
    # The old reply said Indonesians speak Arabic.
    {"u": "1-11-2", "r": 2, "e": 5, "was": "يَتَكَلَّمُونَ العَرَبِيَّةَ", "set": {"ar": "نَعَمْ، وَيُصَلُّونَ بِالعَرَبِيَّةِ", "tr": "naʿam, wa-yuṣallūna bi-l-ʿarabiyyati", "en": "yes, and they pray in Arabic", "note": "يُصَلُّونَ is \"they pray\"."}},
    {"u": "1-11-2", "l": 4, "was": "نَعَمْ، وَهِيَ فِي شِمَالِ تُرْكِيَا", "set": {"ar": "نَعَمْ، وَهِيَ فِي وَسَطِ تُرْكِيَا."}},
    {"u": "1-11-2", "cq": 3, "was": "Where is the capital?", "set": {"a": "فِي وَسَطِ تُرْكِيَا", "w": ["فِي جَنُوبِ تُرْكِيَا", "فِي غَرْبِ تُرْكِيَا"]}},
    {"u": "1-11-2", "cq": 4, "was": "What language do they speak?", "set": {"w": ["العَرَبِيَّةَ", "الإِنْدُونِيسِيَّةَ"]}},

    {"u": "1-11-3", "r": 1, "was": "Safety words", "set": {"body": B("""
        أَمْنٌ is security and أَمَانٌ is safety. خَطَرٌ is danger and خَطِيرٌ means "dangerous"; the opposite is آمِنٌ, "safe". أَمْنٌ, أَمَانٌ and آمِنٌ share the root أ م ن with إِيمَانٌ (faith).
        Learn these words and the people who keep us safe.
    """)}},
    {"u": "1-11-3", "r": 2, "e": 1, "was": "حَدَثَ حَادِثٌ فِي الشَّارِعِ", "set": {"note": "حَدَثَ stays masculine with حَادِثٌ. The two words share the root ح د ث."}},
    # طَرِيقٌ can be masculine or feminine, so هَذِهِ الطَّرِيقُ خَطِيرَةٌ is also correct.
    {"u": "1-11-3", "q": 13, "was": "How do you say \"this road is dangerous\"?", "set": {"w": ["هَذَا الطَّرِيقُ خَطِيرَةٌ", "هَذَا الطَّرِيقُ آمِنٌ"]}},

    {"u": "1-11-4", "r": 2, "was": "Warnings and rules", "set": {"body": B("""
        اِحْذَرْ means "watch out!", اِنْتَبِهْ means "pay attention!" and قِفْ means "stop!". قِفْ is short: from تَقِفُ, drop تَـ and end with a sukoon. For a woman, the command ends with ـِي.
        حَتَّى means "until". A present verb after it ends with ـَ: اِنْتَظِرْ حَتَّى تَصِلَ الشُّرْطَةُ (wait until the police arrive).
    """)}},
    {"u": "1-11-4", "r": 2, "e": 5, "was": "لَا تَدْخُلْ مِنْ هُنَا", "set": {"note": "For \"do not\", use لَا with the \"you\" verb ending in a sukoon, as after لَمْ."}},
    {"u": "1-11-4", "cq": 5, "was": "Whom should he call?", "set": {"q": "What number should he call?", "a": "رَقْمَ الطَّوَارِئِ", "w": ["رَقْمَ الأُسْتَاذِ", "رَقْمَ المُدِيرِ"]}},

    {"u": "1-11-5", "r": 1, "e": 5, "was": "هَذِهِ نُفَايَاتٌ", "set": {"en": "this is waste", "note": "نُفَايَاتٌ means waste or rubbish, like قُمَامَةٌ. It is a plural of things, so it takes هَذِهِ."}},
    {"u": "1-11-5", "r": 2, "was": "Because of", "set": {"body": B("""
        سَبَبٌ is a reason and نَتِيجَةٌ is a result.
        - بِسَبَبِ means "because of". A noun follows it and ends with ـِ: بِسَبَبِ التَّلَوُّثِ. Compare لِأَنَّ (because), which is followed by a whole sentence.
        - لِذَلِكَ means "therefore". It starts the result: لِذَلِكَ لَا أَخْرُجُ.
        - أَدَّى إِلَى means "it led to": أَدَّى التَّلَوُّثُ إِلَى المَرَضِ.
    """)}},
    {"u": "1-11-5", "r": 2, "e": 3, "was": "الجَوُّ مُلَوَّثٌ، لِذَلِكَ", "set": {"ar": "الهَوَاءُ مُلَوَّثٌ، لِذَلِكَ لَا أَخْرُجُ", "tr": "al-hawāʾu mulawwathun, li-dhālika lā akhruju"}},
    {"u": "1-11-5", "r": 2, "e": 5, "was": "مَا سَبَبُ هَذَا الدُّخَانِ؟", "set": {"note": "سَبَبُ هَذَا الدُّخَانِ is an إِضَافَةٌ: \"the reason for this smoke\"."}},
    {"u": "1-11-5", "q": 15, "was": "How do you say \"the air is polluted, therefore I don't go out\"?", "set": {"a": "الهَوَاءُ مُلَوَّثٌ، لِذَلِكَ لَا أَخْرُجُ", "w": ["الهَوَاءُ مُلَوَّثٌ، بِسَبَبِ لَا أَخْرُجُ", "الهَوَاءُ مُلَوَّثٌ، لَنْ أَخْرُجُ لِذَلِكَ"]}},

    {"u": "1-11-6", "r": 1, "was": "Protecting the environment", "set": {"body": B("""
        حَافَظَ عَلَى means "he protected" or "he took care of". Its present is يُحَافِظُ عَلَى, and the command is حَافِظْ عَلَى.
        زَرَعَ means "he planted". أَعَادَ تَدْوِيرَ means "he recycled": أَعَادَ is "he brought back" and تَدْوِيرٌ is "turning round".
    """)}},
    {"u": "1-11-6", "r": 1, "e": 2, "was": "حَافِظْ عَلَى نَظَافَةِ الشَّارِعِ", "set": {"note": "You learned نَظَافَةٌ (cleanliness) in Level 10."}},
    {"u": "1-11-6", "r": 1, "e": 3, "was": "لَا تَرْمِ النُّفَايَاتِ", "set": {"note": "For \"do not\", use لَا with تَرْمِي, which loses its long ي."}},
    {"u": "1-11-6", "r": 2, "was": "Cause and effect", "set": {"body": B("""
        Link a cause and its effect with these words.
        - لِأَنَّ (because) is followed by a noun ending in ـَ, or by a pronoun ending: لِأَنَّ الهَوَاءَ مُلَوَّثٌ, لِأَنَّهُ مُلَوَّثٌ.
        - بِسَبَبِ (because of) is followed by a noun ending in ـِ: بِسَبَبِ التَّلَوُّثِ.
        - لِذَلِكَ (therefore) starts a new sentence, which does not change.
    """)}},
    {"u": "1-11-6", "r": 2, "e": 3, "was": "كُلُّ النَّاسِ يَحْتَاجُونَ", "set": {"note": "النَّاسُ means \"people\". It is plural, so the verb is يَحْتَاجُونَ."}},
    {"u": "1-11-6", "l": 3, "was": "الهَوَاءُ مُلَوَّثٌ، لِذَلِكَ", "set": {"ar": "الهَوَاءُ مُلَوَّثٌ، لِذَلِكَ انْتَشَرَ المَرَضُ."}},

    {"u": "1-11-7", "r": 1, "e": 2, "was": "الكَهْرَبَاءُ مُهِمَّةٌ", "set": {"note": "الكَهْرَبَاءُ is feminine, so مُهِمٌّ becomes مُهِمَّةٌ. Like صَحْرَاءُ, it takes no tanween."}},
    {"u": "1-11-7", "r": 1, "e": 3, "was": "السُّعُودِيَّةُ غَنِيَّةٌ بِالنَّفْطِ", "set": {"tr": "as-suʿūdiyyatu ghaniyyatun bi-n-nafṭi"}},
    {"u": "1-11-7", "r": 1, "e": 4, "was": "هَذَا وَقُودٌ", "set": {"note": "وَقُودٌ is any fuel, such as petrol or wood."}},
    {"u": "1-11-7", "r": 2, "was": "Using and consuming", "set": {"body": B("""
        Many verbs start with اِسْتَـ. This pattern, اِسْتَفْعَلَ, is often called Form X. اِسْتَخْدَمَ means "he used", اِسْتَهْلَكَ means "he consumed" and اِسْتَطَاعَ means "he was able"; you know أَسْتَطِيعُ (I can) from Level 9.
        Their present forms start with يَسْتَـ: يَسْتَخْدِمُ, يَسْتَهْلِكُ, يَسْتَطِيعُ.
    """)}},

    {"u": "1-11-8", "r": 1, "was": "Saving energy", "set": {"body": B("""
        وَفَّرَ means "he saved" and تَوْفِيرٌ is saving. أَطْفَأَ means "he turned off" and أَشْعَلَ means "he turned on" (a light or a fire). For taps and doors, use فَتَحَ and أَغْلَقَ.
        Verbs like أَطْفَأَ and أَشْعَلَ start their command with أَ, which is always pronounced: أَطْفِئْ, أَشْعِلْ. The command of وَفَّرَ is وَفِّرْ.
    """)}},
    {"u": "1-11-8", "r": 1, "e": 3, "was": "نُوَفِّرُ الطَّاقَةَ فِي البَيْتِ", "set": {"note": "نُوَفِّرُ is \"we save\". The و is doubled, as in وَفَّرَ."}},
    {"u": "1-11-8", "r": 2, "e": 2, "was": "النَّفْطُ مَصْدَرٌ مَحْدُودٌ", "set": {"tr": "an-nafṭu maṣdarun maḥdūdun"}},
    {"u": "1-11-8", "r": 2, "e": 3, "was": "سَوْفَ يَنْفَدُ النَّفْطُ يَوْمًا", "set": {"tr": "sawfa yanfadu n-nafṭu yawman"}},
    # A lamp is "lit", not "open".
    {"u": "1-11-8", "l": 1, "was": "السَّلَامُ عَلَيْكُمْ. لِمَاذَا المِصْبَاحُ مَفْتُوحٌ", "set": {"ar": "السَّلَامُ عَلَيْكُمْ. لِمَاذَا المِصْبَاحُ مُضَاءٌ فِي النَّهَارِ؟"}},
    {"u": "1-11-8", "l": 8, "was": "هَلْ الطَّاقَةُ الشَّمْسِيَّةُ", "set": {"ar": "هَلِ الطَّاقَةُ الشَّمْسِيَّةُ نَظِيفَةٌ؟"}},
    {"u": "1-11-8", "cq": 1, "was": "What does the father ask?", "set": {"a": "لِمَاذَا المِصْبَاحُ مُضَاءٌ"}},

    {"u": "1-11-9", "q": 2, "was": "How do you say \"Ankara is in the north of Turkey\"?", "set": {"q": "How do you say \"Tabuk is in the north of Saudi Arabia\"?", "a": "تَبُوكُ فِي شِمَالِ السُّعُودِيَّةِ", "w": ["تَبُوكُ فِي جَنُوبِ السُّعُودِيَّةِ", "تَبُوكُ شِمَالٌ السُّعُودِيَّةَ"]}},
    {"u": "1-11-9", "l": 8, "was": "لَنْ تَخْسَرَ", "set": {"ar": "لَنْ يَحْدُثَ شَيْءٌ، إِنْ شَاءَ اللَّهُ."}},
]
