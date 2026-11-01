# Stage 1 · Level 4 — content corrections and improvements.
DAYS_ABOUT = "Talk about your week and your day. You will learn the days of the week, today, tomorrow and yesterday, the parts of the day, and your first everyday verbs such as I go, I eat and I study."
FIXES = [
    {"u": "1-4-1", "r": 1, "e": 7, "was": "هَذِهِ بَيْضَةٌ", "set": {"note": "بَيْضَةٌ is one egg, and it is feminine. بَيْضٌ means eggs in general."}},
    {"u": "1-4-1", "r": 2, "was": "Drinks", "set": {"body": B("""
        شَرَابٌ means "a drink", and المَشْرُوبَاتُ means "drinks". Most drink words are masculine, so point at them with هَذَا. قَهْوَةٌ ends with ـَةٌ, so it is feminine: هَذِهِ قَهْوَةٌ.
        To name a juice, put the fruit after عَصِيرُ: عَصِيرُ بُرْتُقَالٍ is "orange juice", literally "juice of oranges".
    """)}},
    {"u": "1-4-1", "r": 2, "e": 1, "was": "هَذَا مَاءٌ", "set": {"note": "You met مَاءٌ in Level 1, in أُرِيدُ مَاءً (I want water)."}},

    # The object of both verbs is accusative; ال vs no ال decides ـً or ـَ.
    {"u": "1-4-2", "r": 1, "was": "I want and I like", "set": {"body": B("""
        You know أُرِيدُ (I want). Now learn أُحِبُّ, which means "I like" or "I love". To say "I do not like", put لَا before it: لَا أُحِبُّ.
        After both verbs, the thing ends with a فَتْحَةٌ.
        - Without اَلْ it takes tanween: أُرِيدُ خُبْزًا (I want some bread).
        - With اَلْ it takes a single ـَ: أُحِبُّ الشَّايَ (I like tea).
        Arabic uses اَلْ when you talk about a thing in general, so "I like tea" is أُحِبُّ الشَّايَ, with اَلْ.
    """)}},
    {"u": "1-4-2", "r": 2, "e": 8, "was": "لَا، لَسْتُ عَطْشَى", "set": {"note": "لَسْتُ means \"I am not\". It is the \"I\" form of لَيْسَ."}},
    {"u": "1-4-2", "w": 5, "was": "عَطْشَى", "set": {"pl": "عِطَاشٌ"}},

    {"u": "1-4-4", "r": 1, "was": "Rooms in the house", "set": {"body": B("""
        غُرْفَةٌ means "room", and its plural is غُرَفٌ. Some rooms have a one-word name, like مَطْبَخٌ (kitchen). Others are named with غُرْفَةُ and a second noun, just like كِتَابُ العَرَبِيَّةِ: غُرْفَةُ النَّوْمِ is "the room of sleep", the bedroom.
    """)}},
    {"u": "1-4-4", "r": 1, "e": 2, "was": "هَذَا مَطْبَخٌ", "set": {"note": "مَطْبَخٌ comes from طَبَخَ, \"he cooked\". A مَـ at the start often means \"the place of\". Its plural is مَطَابِخُ."}},
    {"u": "1-4-4", "r": 1, "e": 3, "was": "هَذَا حَمَّامٌ", "set": {"note": "حَمَّامٌ is the bathroom. Its plural is حَمَّامَاتٌ."}},
    {"u": "1-4-4", "r": 2, "was": "Places in the city", "set": {"body": B("""
        مَدِينَةٌ means "city", and its plural is مُدُنٌ. Learn the main places you can find in one.
        Many place words start with مَـ, which often means "the place of": مَطَارٌ (airport) comes from طَارَ, "it flew", and مَسْجِدٌ (mosque) comes from سَجَدَ, "he bowed down in prayer".
    """)}},

    {"u": "1-4-5", "r": 1, "was": "Where is it?", "set": {"body": B("""
        Ask أَيْنَ, then the person or thing, to find where it is. In the answer, say the thing first, then فِي ("in") and the place. The word after فِي ends with ـِ: البَيْتُ becomes فِي البَيْتِ.
    """)}},
    {"u": "1-4-5", "r": 2, "e": 6, "was": "المُعَلِّمُ أَمَامَ السَّبُّورَةِ", "set": {"note": "You learned سَبُّورَةٌ with the classroom words in Level 2."}},

    # "There is": the old explanation was garbled.
    {"u": "1-4-6", "r": 1, "was": "Here and there", "set": {"body": B("""
        هُنَا means "here" and هُنَاكَ means "there".
        To say that something is in a place ("there is"), start with فِي and the place, then say the thing. The thing has no اَلْ and ends with tanween: فِي البَيْتِ غُرْفَةٌ means "in the house there is a room".
    """)}},
    {"u": "1-4-6", "r": 2, "e": 5, "was": "أَسْكُنُ فِي جُدَّةَ", "set": {"note": "جُدَّةُ is a city on the Red Sea. Most city names without اَلْ, like جُدَّةُ and مَكَّةُ, take no tanween, so after فِي they end with ـَ."}},

    # The theme no longer closes a level on its own.
    {"u": "1-4-7", "set": {"about": DAYS_ABOUT}},
    {"u": "1-4-8", "set": {"about": DAYS_ABOUT}},
    {"u": "1-4-9", "set": {"about": DAYS_ABOUT}},
    {"u": "1-4-8", "r": 1, "e": 5, "was": "صَبَاحُ الخَيْرِ", "set": {"note": "You learned this greeting in Level 1."}},
    {"u": "1-4-8", "r": 2, "e": 2, "was": "آكُلُ الخُبْزَ", "set": {"note": "آكُلُ comes from أَكَلَ, \"he ate\". Two hamzas join at the start to make one long آ."}},
    {"u": "1-4-9", "r": 1, "e": 7, "was": "مَاذَا تَفْعَلُ اليَوْمَ؟", "set": {"en": "what are you doing today? (to a man)"}},
    {"u": "1-4-9", "r": 1, "e": 9, "was": "مَاذَا تَفْعَلِينَ غَدًا؟", "set": {"en": "what are you doing tomorrow? (to a woman)"}},
    {"u": "1-4-9", "r": 1, "e": 10, "was": "مَتَى تَنَامِينَ؟", "set": {"note": "مَتَى means \"when\". You learned it with the question words in Level 1."}},
]
