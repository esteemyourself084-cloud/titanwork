# Stage 1 · Level 7 — content corrections and improvements.
FIXES = [
    {"u": "1-7-1", "r": 1, "was": "Hajj and Umrah", "set": {"body": B("""
        الحَجُّ (Hajj) is the great pilgrimage to Makkah. It is one of the five pillars of Islam, and every Muslim who is able makes it once in a lifetime, in the month of ذُو الحِجَّةِ. العُمْرَةُ (Umrah) is the lesser pilgrimage, which can be made at any time of the year.
        - A man who makes Hajj is حَاجٌّ, and a woman is حَاجَّةٌ.
        - A man who makes Umrah is مُعْتَمِرٌ, and a woman is مُعْتَمِرَةٌ.
    """)}},
    {"u": "1-7-1", "r": 1, "e": 7, "was": "الحَجُّ فِي ذِي الحِجَّةِ", "set": {"note": "ذُو الحِجَّةِ is the twelfth month of the Islamic year, the month of Hajj. After فِي, ذُو becomes ذِي."}},
    {"u": "1-7-1", "r": 2, "was": "The holy places", "set": {"body": B("""
        Say the names of the places of the pilgrimage. مَكَّةُ المُكَرَّمَةُ and المَدِينَةُ المُنَوَّرَةُ are the two holy cities.
        The describing words follow the city names, as you learned in Level 3. A city name counts as a word with اَلْ, so its describing word takes اَلْ too: مَكَّةُ المُكَرَّمَةُ.
    """)}},
    {"u": "1-7-1", "r": 2, "e": 2, "was": "المَدِينَةُ المُنَوَّرَةُ", "set": {"en": "Madinah, the illuminated", "note": "المُنَوَّرَةُ means \"the illuminated\". It comes from نُورٌ, \"light\"."}},
    {"u": "1-7-1", "r": 2, "e": 3, "was": "المَسْجِدُ الحَرَامُ فِي مَكَّةَ", "set": {"note": "Here الحَرَامُ means \"sacred\", not \"forbidden\". The Kaʿbah is in this mosque."}},
    {"u": "1-7-1", "r": 2, "e": 5, "was": "أَيْنَ عَرَفَةُ؟", "set": {"note": "عَرَفَةُ is the plain where pilgrims stand on the ninth day of ذُو الحِجَّةِ."}},
    {"u": "1-7-1", "r": 2, "e": 6, "was": "عَرَفَةُ بَعِيدَةٌ عَنْ مَكَّةَ", "set": {"note": "عَرَفَةُ is feminine, so بَعِيدٌ becomes بَعِيدَةٌ. You learned بَعِيدٌ عَنْ in Level 6."}},
    {"u": "1-7-1", "r": 2, "e": 7, "was": "مِنًى بِجَانِبِ مَكَّةَ", "set": {"note": "مِنًى is the valley where pilgrims stay during Hajj. You learned بِجَانِبِ in Level 4."}},
    {"u": "1-7-1", "r": 2, "e": 8, "was": "مَاءُ زَمْزَمَ", "set": {"note": "زَمْزَمُ is the blessed well near the Kaʿbah. This is an إِضَافَةٌ: \"the water of Zamzam\"."}},

    {"u": "1-7-2", "r": 1, "was": "The main rites", "set": {"body": B("""
        المَنَاسِكُ are the rites of Hajj and Umrah. Learn their names.
        - الإِحْرَامُ (ihram) is the sacred state a pilgrim enters before the rites.
        - الطَّوَافُ is walking seven times around the Kaʿbah. Each round is a شَوْطٌ.
        - السَّعْيُ is walking seven times between the hills of Safa and Marwa.
        Use حَوْلَ for "around" and بَيْنَ for "between".
    """)}},
    {"u": "1-7-2", "r": 1, "e": 1, "was": "الإِحْرَامُ", "set": {"note": "A pilgrim enters ihram before the rites. A man wears two plain white cloths."}},
    {"u": "1-7-2", "r": 2, "was": "Words for the pilgrim", "set": {"body": B("""
        التَّلْبِيَةُ (the Talbiyah) is what pilgrims say again and again from the moment they enter ihram. Learn it slowly, one part at a time.
        After it come some wishes people say to pilgrims. A wish like حَجًّا مَبْرُورًا ends with ـًا.
    """)}},
    {"u": "1-7-2", "r": 2, "e": 1, "was": "لَبَّيْكَ اللَّهُمَّ لَبَّيْكَ", "set": {"note": "This is how the Talbiyah begins. لَبَّيْكَ means \"here I am, at Your service\", and اللَّهُمَّ means \"O Allah\"."}},

    {"u": "1-7-3", "r": 1, "was": "My journey", "set": {"body": B("""
        Use the past for what you did, and سَـ before the present for what you will do. Some common verbs change a little in the past.
        - Verbs with a long ا in the middle, like طَافَ (he made tawaf) and زَارَ (he visited), drop the ا with "I", and the first letter takes ـُ: طُفْتُ, زُرْتُ.
        - Verbs that end in ى, like سَعَى and صَلَّى, change the ى to ي: سَعَيْتُ, صَلَّيْتُ.
    """)}},
    {"u": "1-7-3", "r": 1, "e": 1, "was": "طُفْتُ حَوْلَ الكَعْبَةِ", "set": {"note": "With \"I\", طَافَ drops its long ا and becomes طُفْتُ."}},
    {"u": "1-7-3", "r": 1, "e": 2, "was": "سَعَيْتُ بَيْنَ الصَّفَا", "set": {"note": "سَعَيْتُ is the \"I\" form of سَعَى. The ى becomes ي."}},
    {"u": "1-7-3", "r": 1, "e": 5, "was": "سَأَحُجُّ هَذِهِ السَّنَةَ", "set": {"note": "أَحُجُّ means \"I make Hajj\", and سَـ makes it future."}},
    {"u": "1-7-3", "r": 1, "e": 6, "was": "زُرْتُ المَدِينَةَ المُنَوَّرَةَ", "set": {"note": "زُرْتُ is the \"I\" form of زَارَ (he visited). The long ا drops, just as in طُفْتُ."}},
    {"u": "1-7-3", "r": 1, "e": 8, "was": "هَلْ سَافَرْتَ إِلَى مَكَّةَ؟", "set": {"note": "You learned سَافَرَ in Level 5."}},
    {"u": "1-7-3", "r": 1, "e": 9, "was": "نَعَمْ، سَافَرْتُ لِلْعُمْرَةِ", "set": {"note": "لِـ means \"for\". Before اَلْ its ا drops, so لِـ and العُمْرَةِ become لِلْعُمْرَةِ."}},

    {"u": "1-7-4", "r": 1, "was": "The body", "set": {"body": B("""
        جِسْمٌ means "body". Learn the main parts. Most parts that come in pairs, such as the eyes, ears, hands and feet, are feminine, so point at one with هَذِهِ.
        For two of them, add ـَانِ. This is the dual (مُثَنَّى) from Level 1: عَيْنٌ becomes عَيْنَانِ (two eyes).
    """)}},
    {"u": "1-7-4", "r": 2, "was": "What is wrong?", "set": {"body": B("""
        Ask a man مَا بِكَ؟ and a woman مَا بِكِ؟. It means "what is wrong with you?".
        Answer with عِنْدِي ("I have") and the problem: عِنْدِي صُدَاعٌ. To say where it hurts, say عِنْدِي أَلَمٌ فِي and the body part with ـِي ("my"): عِنْدِي أَلَمٌ فِي ظَهْرِي. أَلَمٌ means "pain".
    """)}},
    {"u": "1-7-4", "q": 17, "was": "How does a man ask \"What is wrong with you?\"", "set": {"q": "How do you ask a man \"What is wrong with you?\""}},

    {"u": "1-7-5", "r": 1, "was": "At the doctor", "set": {"body": B("""
        A doctor (طَبِيبٌ) works in a clinic (عِيَادَةٌ) or a hospital (مُسْتَشْفًى). You may need an appointment, مَوْعِدٌ.
        The doctor may ask about your temperature (حَرَارَةٌ) and how long you have been ill: مُنْذُ مَتَى؟ ("since when?"). Answer with مُنْذُ and the time.
    """)}},
    {"u": "1-7-5", "r": 1, "e": 5, "was": "نَعَمْ، عِنْدِي حَرَارَةٌ عَالِيَةٌ", "set": {"note": "عَالٍ means \"high\". For a feminine word it becomes عَالِيَةٌ, just like غَالٍ and غَالِيَةٌ."}},
    {"u": "1-7-5", "r": 1, "e": 8, "was": "هَلْ ذَهَبْتَ إِلَى المُسْتَشْفَى؟", "set": {"note": "You learned the past tense in Level 5."}},
    # "Do not" uses لَا with the "you" verb, never with the command form.
    {"u": "1-7-5", "r": 2, "was": "Medicine and advice", "set": {"body": B("""
        دَوَاءٌ is medicine and صَيْدَلِيَّةٌ is a pharmacy. To give advice, use a command, like the اِذْهَبْ you learned in Level 6.
        - For a man, take the "you" verb, drop its تَـ and end it with a sukoon. If it now starts with a sukoon, add اِ in front: تَشْرَبُ becomes اِشْرَبْ (drink).
        - For a woman, the command ends with ـِي: اِشْرَبِي.
        - To say "do not", do not use the command. Put لَا before the "you" verb and end it with a sukoon: لَا تَأْكُلْ (do not eat). For a woman, say لَا تَأْكُلِي.
    """)}},
    {"u": "1-7-5", "r": 2, "e": 1, "was": "خُذْ هَذَا الدَّوَاءَ", "set": {"note": "خُذْ is the command of أَخَذَ, \"he took\". It is short and irregular, so learn it as it is."}},
    {"u": "1-7-5", "r": 2, "e": 3, "was": "اِشْرَبِ المَاءَ", "set": {"note": "The sukoon of اِشْرَبْ becomes ـِ before اَلْ, so the words join."}},
    {"u": "1-7-5", "r": 2, "e": 5, "was": "لَا تَأْكُلِ السُّكَّرَ", "set": {"note": "For \"do not\", use لَا with the \"you\" verb تَأْكُلُ, not the command. Its last letter takes a sukoon, which becomes ـِ before اَلْ."}},
    {"u": "1-7-5", "r": 2, "e": 6, "was": "خُذْهُ مَرَّتَيْنِ فِي اليَوْمِ", "set": {"note": "ـهُ means \"it\", the medicine. You learned مَرَّتَيْنِ (twice) in Level 6."}},
    {"u": "1-7-5", "r": 2, "e": 7, "was": "خُذْهُ بَعْدَ الأَكْلِ", "set": {"note": "بَعْدَ means \"after\" and قَبْلَ means \"before\". الأَكْلُ means \"eating\"."}},
    {"u": "1-7-5", "q": 9, "was": "How do you say \"do not eat sugar\" (to a man)?", "set": {"w": ["لَا كُلِ السُّكَّرَ", "لَا آكُلُ السُّكَّرَ"]}},

    {"u": "1-7-6", "r": 1, "was": "Kind words to the sick", "set": {"body": B("""
        When someone is ill, Muslims say a short prayer (دُعَاءٌ) for them. Learn these set phrases as they are. Change ـكَ to ـكِ when you speak to a woman.
    """)}},
    {"u": "1-7-6", "r": 1, "e": 2, "was": "شَفَاكَ اللَّهُ", "set": {"note": "شَفَى means \"he healed\". The verb looks past, but the phrase is a wish, like تَقَبَّلَ اللَّهُ."}},
    {"u": "1-7-6", "r": 1, "e": 4, "was": "لَا بَأْسَ، طَهُورٌ", "set": {"note": "The Prophet ﷺ said it when he visited the sick. It means the illness cleanses the person of sins."}},

    {"u": "1-7-7", "r": 1, "e": 6, "was": "هَذِهِ صَحْرَاءُ", "set": {"note": "صَحْرَاءُ is feminine even without ـَةٌ. Like the colour زَرْقَاءُ, it ends in ـَاءُ and takes no tanween. Its plural is صَحَارَى."}},
    {"u": "1-7-7", "r": 2, "was": "Where do you spend the holiday?", "set": {"body": B("""
        قَضَى means "he spent (time)". Its present is يَقْضِي, so "I spend" is أَقْضِي, and "I spent" is قَضَيْتُ. Use فِي for the place.
        Ask a man أَيْنَ تَقْضِي العُطْلَةَ؟ and a woman أَيْنَ تَقْضِينَ العُطْلَةَ؟
    """)}},
    {"u": "1-7-7", "r": 2, "e": 3, "was": "أَيْنَ تَقْضِينَ العُطْلَةَ؟", "set": {"note": "For a woman, تَقْضِي becomes تَقْضِينَ."}},
    {"u": "1-7-7", "r": 2, "e": 6, "was": "قَضَيْنَا الإِجَازَةَ عِنْدَ جَدِّي", "set": {"note": "عِنْدَ means \"at\" someone's place. You know it from عِنْدِي, \"I have\", literally \"at me\"."}},
    {"u": "1-7-7", "r": 2, "e": 8, "was": "تَبْدَأُ الأُسْبُوعَ القَادِمَ", "set": {"note": "القَادِمُ means \"coming\" or \"next\". It is the opposite of المَاضِي, and it follows its noun."}},

    {"u": "1-7-8", "r": 1, "was": "What did you do?", "set": {"body": B("""
        Now you can tell about a trip in the past. Learn the verbs of a holiday: نَزَلَ means "he stayed" (at a hotel) or "he got off", زَارَ means "he visited", سَبَحَ means "he swam" and صَوَّرَ means "he took photos".
        - Add نَا for "we": نَزَلْنَا (we stayed). زَارَ drops its long ا, as in زُرْتُ: زُرْنَا (we visited).
        - Add تُمْ for "you" when you speak to a group: نَزَلْتُمْ (you all stayed), فَعَلْتُمْ (you all did).
    """)}},
    {"u": "1-7-8", "r": 2, "was": "It was beautiful", "set": {"body": B("""
        You know كَانَ from the weather in Level 5. For a feminine thing, say كَانَتْ; before اَلْ it becomes كَانَتِ. The describing word after it ends with ـًا: كَانَتِ العُطْلَةُ جَمِيلَةً.
    """)}},

    {"u": "1-7-9", "r": 1, "was": "Which do you prefer?", "set": {"body": B("""
        فَضَّلَ means "he preferred", so "I prefer" is أُفَضِّلُ. The thing you prefer ends with ـَ: أُفَضِّلُ البَحْرَ.
        - Use عَلَى for the thing you like less: أُفَضِّلُ البَحْرَ عَلَى الجَبَلِ (I prefer the sea to the mountain).
        - Use أَوْ ("or") to offer a choice.
        To make plans, put سَـ before the present, or use the separate word سَوْفَ. Both mean "will": سَأُسَافِرُ and سَوْفَ أُسَافِرُ.
    """)}},
    {"u": "1-7-9", "r": 1, "e": 7, "was": "عُطْلَةً سَعِيدَةً", "set": {"note": "Like حَجًّا مَبْرُورًا, this wish ends with ـًا. سَعِيدٌ means \"happy\"."}},
]
