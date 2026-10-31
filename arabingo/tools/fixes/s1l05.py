# Stage 1 · Level 5 — content corrections and improvements.
PAST_ABOUT = "Talk about things that already happened. You will learn the past tense for he, she, I, you and we, how to make it negative, how to ask about it, and time words such as أَمْسِ and الأُسْبُوعُ المَاضِي."
FIXES = [
    # The past-tense theme used to open Level 2.
    {"u": "1-5-1", "set": {"about": PAST_ABOUT}},
    {"u": "1-5-2", "set": {"about": PAST_ABOUT}},
    {"u": "1-5-3", "set": {"about": PAST_ABOUT}},

    {"u": "1-5-1", "r": 1, "was": "He did and she did", "set": {"body": B("""
        In Level 4 you used the present form of the verb, such as أَذْهَبُ (I go). The past form tells what already happened.
        - For "he", the past form ends with ـَ: ذَهَبَ (he went). This is also the form word lists use, so ذَهَبَ is given as "to go".
        - For "she", add تْ: ذَهَبَتْ (she went).
        In a sentence the verb usually comes first, then the person who did it: ذَهَبَ أَحْمَدُ (Ahmad went).
    """)}},
    {"u": "1-5-1", "r": 2, "was": "I did and you did", "set": {"body": B("""
        To say who did the action, add an ending to the "he" form. The letter before the ending takes a sukoon (ـْ), which means no vowel.
        - Add تُ for "I": ذَهَبْتُ (I went).
        - Add تَ for "you" when you talk to a man: ذَهَبْتَ.
        - Add تِ for "you" when you talk to a woman: ذَهَبْتِ.
        Look closely: ذَهَبَتْ (she went) and ذَهَبْتَ (you went) have the same letters. Only the vowel marks show the difference.
    """)}},

    {"u": "1-5-2", "r": 1, "was": "We did", "set": {"body": B("""
        For "we", add نَا to the end, again with a sukoon before it: ذَهَبْنَا (we went). The pronoun for "we" is نَحْنُ. You can say it or leave it out, because نَا already shows who did it.
    """)}},
    {"u": "1-5-2", "r": 2, "was": "Not and why not", "set": {"body": B("""
        Put مَا before a past verb to say it did not happen: مَا ذَهَبْتُ (I did not go). The verb itself does not change.
        To ask about the past, start with a question word: مَتَى (when), أَيْنَ (where), مَاذَا (what) or لِمَاذَا (why). Answer لِمَاذَا with لِأَنَّ (because).
    """)}},
    {"u": "1-5-2", "r": 2, "e": 8, "was": "لِأَنِّي مَرِيضٌ", "set": {"note": "لِأَنِّي is لِأَنَّ (because) joined with ـِي (I). مَرِيضٌ means \"sick\"; a woman says لِأَنِّي مَرِيضَةٌ."}},

    # The time phrase is accusative, so المَاضِي shows its fatha.
    {"u": "1-5-3", "r": 1, "was": "Time words for the past", "set": {"body": B("""
        You already know أَمْسِ (yesterday). Add الأُسْبُوعُ المَاضِي (last week), السَّنَةُ المَاضِيَةُ (last year) and الآنَ (now).
        المَاضِي means "past". It is a describing word, so it comes after its noun and agrees with it: سَنَةٌ is feminine, so it takes المَاضِيَةُ.
        When a time phrase tells when something happened, its words end with ـَ: ذَهَبْتُ الأُسْبُوعَ المَاضِيَ.
    """)}},
    {"u": "1-5-3", "r": 1, "e": 1, "was": "ذَهَبْتُ أَمْسِ", "set": {"note": "أَمْسِ always ends with ـِ. It can also start the sentence: أَمْسِ ذَهَبْتُ."}},
    {"u": "1-5-3", "r": 1, "e": 2, "was": "ذَهَبْتُ الأُسْبُوعَ المَاضِي", "set": {"ar": "ذَهَبْتُ الأُسْبُوعَ المَاضِيَ", "note": "Both words end with ـَ because they tell when."}},

    {"u": "1-5-4", "r": 1, "was": "Clothes and things to buy", "set": {"body": B("""
        مَلَابِسُ means "clothes". Learn the names of common clothes and a few things people buy. Point at a masculine thing with هَذَا and at a feminine thing with هَذِهِ. You met ثَوْبٌ, the long robe, with the colours in Level 3.
        Some things that English calls "a pair" are one singular word in Arabic: سِرْوَالٌ (trousers) and نَظَّارَةٌ (glasses).
    """)}},
    {"u": "1-5-4", "r": 1, "e": 6, "was": "هَذِهِ نَظَّارَةٌ", "set": {"note": "Like سِرْوَالٌ, it is one singular word in Arabic. Its plural is نَظَّارَاتٌ."}},
    {"u": "1-5-4", "r": 1, "e": 8, "was": "قَمِيصٌ أَبْيَضُ", "set": {"note": "Colours come after the noun, as you learned in Level 3. Colour words never take tanween: أَبْيَضُ, not أَبْيَضٌ."}},
    {"u": "1-5-4", "r": 2, "was": "Numbers 11 to 20", "set": {"body": B("""
        From 11 to 19, two words make one number, and the second word is always عَشَرَ.
        - 11 is أَحَدَ عَشَرَ and 12 is اِثْنَا عَشَرَ.
        - From 13 to 19, put the small number first, ending with ـَ: ثَلَاثَةَ عَشَرَ, أَرْبَعَةَ عَشَرَ, خَمْسَةَ عَشَرَ, سِتَّةَ عَشَرَ, سَبْعَةَ عَشَرَ, ثَمَانِيَةَ عَشَرَ, تِسْعَةَ عَشَرَ.
        After these numbers, the counted thing is singular and ends with ـًا: أَحَدَ عَشَرَ رِيَالًا. These are the forms for masculine things, like رِيَالٌ and قَمِيصٌ.
    """)}},
    {"u": "1-5-4", "r": 2, "e": 1, "was": "أَحَدَ عَشَرَ", "set": {"note": "Number 11, written ١١."}},
    {"u": "1-5-4", "r": 2, "e": 2, "was": "اِثْنَا عَشَرَ", "set": {"note": "Number 12, written ١٢. اِثْنَا comes from اِثْنَانِ."}},
    {"u": "1-5-4", "r": 2, "e": 3, "was": "خَمْسَةَ عَشَرَ", "set": {"note": "Number 15, written ١٥. The numbers 13 to 19 follow the same pattern."}},
    {"u": "1-5-4", "r": 2, "e": 4, "was": "عِشْرُونَ", "set": {"note": "Number 20, written ٢٠. You learned it with the tens in Level 3."}},

    {"u": "1-5-5", "r": 1, "was": "Bigger numbers", "set": {"body": B("""
        To make 21, 35 and so on, say the small number first, then وَ ("and"), then the ten: خَمْسَةٌ وَعِشْرُونَ is "five and twenty". After these numbers, the counted thing is singular and ends with ـًا, just as after 11 to 19.
        مِئَةٌ (100) and أَلْفٌ (1000) join the counted thing in an إِضَافَةٌ, like كِتَابُ العَرَبِيَّةِ. The number loses its tanween, and the thing is singular and ends with ـٍ: مِئَةُ رِيَالٍ.
    """)}},
    {"u": "1-5-5", "r": 1, "e": 3, "was": "مِئَةٌ", "set": {"note": "Number 100, written ١٠٠. You met it in Level 3."}},
    {"u": "1-5-5", "r": 1, "e": 6, "was": "ثَلَاثُمِئَةٍ", "set": {"note": "Number 300, written ٣٠٠. ثَلَاثُ and مِئَةٍ are joined and written as one word."}},
    {"u": "1-5-5", "r": 1, "e": 7, "was": "أَلْفٌ", "set": {"note": "Number 1000, written ١٠٠٠. Its plural is آلَافٌ."}},
    {"u": "1-5-5", "r": 2, "was": "How much is it?", "set": {"body": B("""
        بِكَمْ means "for how much?". It is the usual way to ask a price, and the answer can start with بِـ too. After بِـ the number ends with ـٍ, and عِشْرُونَ becomes عِشْرِينَ: بِعِشْرِينَ رِيَالًا.
        You can also ask مَا سِعْرُ...؟, where سِعْرٌ means "price".
        Say that something is غَالٍ ("expensive") or رَخِيصٌ ("cheap"). For a feminine thing they become غَالِيَةٌ and رَخِيصَةٌ.
    """)}},
    {"u": "1-5-5", "r": 2, "e": 2, "was": "بِخَمْسَةٍ وَعِشْرِينَ رِيَالًا", "set": {"note": "After بِـ, خَمْسَةٌ becomes خَمْسَةٍ and عِشْرُونَ becomes عِشْرِينَ."}},
    {"u": "1-5-5", "r": 2, "e": 5, "was": "هَذَا غَالٍ", "set": {"note": "غَالٍ is read \"ghālin\". Its ي comes back in the feminine غَالِيَةٌ."}},

    {"u": "1-5-6", "r": 1, "was": "Buying and paying", "set": {"body": B("""
        أَشْتَرِي means "I buy" and اشْتَرَيْتُ means "I bought". أَدْفَعُ means "I pay" and دَفَعْتُ means "I paid".
        نُقُودٌ means "money". Say نَقْدًا for "in cash" and بِالبِطَاقَةِ for "by card".
        The thing you buy is the object of the verb, so it ends with ـًا: أَشْتَرِي قَمِيصًا.
    """)}},
    {"u": "1-5-6", "r": 1, "e": 1, "was": "أَشْتَرِي قَمِيصًا", "set": {"note": "أَشْتَرِي ends with a long ي, so it has no ـُ at the end like أَذْهَبُ."}},
    # هَلْ takes a kasra before a word that starts with a silent ا.
    {"u": "1-5-6", "r": 1, "e": 5, "was": "هَلْ اشْتَرَيْتَ هَاتِفًا؟", "set": {"ar": "هَلِ اشْتَرَيْتَ هَاتِفًا؟", "tr": "hali shtarayta hātifan", "note": "Before the silent ا of اشْتَرَيْتَ, هَلْ becomes هَلِ so the words run together. تَ means \"you\" to a man."}},
    {"u": "1-5-6", "r": 1, "e": 8, "was": "دَفَعْتُ مِئَتَيْ رِيَالٍ", "set": {"note": "مِئَتَانِ becomes مِئَتَيْنِ as the object of the verb, and its ن drops when رِيَالٍ joins it: مِئَتَيْ رِيَالٍ."}},
    {"u": "1-5-6", "r": 2, "was": "In the shop", "set": {"body": B("""
        بَائِعٌ is a shop assistant, and بَائِعَةٌ is a woman who serves in a shop. In a shop you speak to the whole shop, so use ـكُمْ: هَلْ عِنْدَكُمْ...؟ means "do you have...?"
        مَقَاسٌ means "size", شَيْءٌ means "thing" and آخَرُ means "other" or "another". Ask for the bill with كَمِ الحِسَابُ؟
    """)}},
    {"u": "1-5-6", "r": 2, "e": 1, "was": "هَلْ عِنْدَكُمْ قَمِيصٌ أَزْرَقُ؟", "set": {"note": "عِنْدَكُمْ means \"you have\". ـكُمْ is \"you\" for a group, so it suits a shop."}},
    {"u": "1-5-6", "r": 2, "e": 5, "was": "هَلْ تُرِيدُ شَيْئًا آخَرَ؟", "set": {"note": "شَيْءٌ becomes شَيْئًا as the object. آخَرُ never takes tanween, so it becomes آخَرَ."}},
    {"u": "1-5-6", "w": 9, "was": "اشْتَرَى", "set": {"pl": "يَشْتَرِي"}},
    {"u": "1-5-6", "w": 10, "was": "دَفَعَ", "set": {"pl": "يَدْفَعُ"}},
    {"u": "1-5-6", "q": 3, "was": "How do you say \"I pay in cash\"?", "set": {"w": ["أَدْفَعُ بِالبِطَاقَةِ", "دَفَعْتُ نَقْدًا"]}},
    {"u": "1-5-6", "q": 5, "was": "How does a man ask \"Did you buy a phone?\"", "set": {"q": "How do you ask a man \"Did you buy a phone?\"", "a": "هَلِ اشْتَرَيْتَ هَاتِفًا؟", "w": ["هَلِ اشْتَرَيْتِ هَاتِفًا؟", "هَلْ تَشْتَرِي هَاتِفًا؟"]}},

    {"u": "1-5-7", "r": 1, "e": 4, "was": "الجَوُّ جَمِيلٌ", "set": {"note": "جَمِيلٌ means \"beautiful\". You know it from Level 3."}},
    {"u": "1-5-7", "r": 2, "was": "Rain, sun and wind", "set": {"body": B("""
        These are the main weather words. You know هُنَاكَ as "there". At the start of a sentence it means "there is": هُنَاكَ مَطَرٌ (there is rain).
        For rain you can also say تُمْطِرُ السَّمَاءُ, "the sky is raining". السَّمَاءُ is feminine, so the verb starts with تـ.
    """)}},

    {"u": "1-5-8", "r": 2, "was": "The temperature", "set": {"body": B("""
        دَرَجَةٌ means "degree" and حَرَارَةٌ means "heat", so دَرَجَةُ الحَرَارَةِ is "the temperature". Count the degrees with the number rules you know.
        - From 3 to 10, use the plural دَرَجَاتٍ. دَرَجَةٌ is feminine, so the number drops ـَةٌ: عَشْرُ دَرَجَاتٍ.
        - With عِشْرُونَ and the other tens, use the singular with ـًا: عِشْرُونَ دَرَجَةً.
        Use صِفْرٌ for "zero".
    """)}},
    {"u": "1-5-8", "r": 2, "e": 4, "was": "الحَرَارَةُ عَشْرُ دَرَجَاتٍ", "set": {"note": "دَرَجَةٌ is feminine, so عَشَرَةٌ drops ـَةٌ and becomes عَشْرُ, as in عَشْرُ سَنَوَاتٍ."}},

    {"u": "1-5-9", "r": 1, "was": "Was and will be", "set": {"body": B("""
        Use كَانَ for "was" and سَيَكُونُ for "will be". After these verbs, the describing word ends with ـًا instead of ـٌ: الجَوُّ حَارٌّ becomes كَانَ الجَوُّ حَارًّا.
        The verb agrees with the thing you describe. الجَوُّ is masculine, so it takes كَانَ. For a feminine thing, use كَانَتْ and سَتَكُونُ.
    """)}},
    {"u": "1-5-9", "r": 1, "e": 5, "was": "سَتُمْطِرُ السَّمَاءُ غَدًا", "set": {"note": "سَـ before تُمْطِرُ makes it future, just as سَيَكُونُ is the future of كَانَ."}},
    {"u": "1-5-9", "r": 1, "add": {"ar": "كَانَتِ العَبَاءَةُ غَالِيَةً", "tr": "kānati l-ʿabāʾatu ghāliyatan", "en": "the abaya was expensive", "note": "عَبَاءَةٌ is feminine, so the verb is كَانَتْ. Before ال it becomes كَانَتِ, and غَالِيَةٌ becomes غَالِيَةً."}},
    {"u": "1-5-9", "r": 2, "was": "What to wear", "set": {"body": B("""
        أَلْبَسُ means "I wear" and لَبِسْتُ means "I wore". Ask a man مَاذَا تَلْبَسُ؟ (what are you wearing?).
        The clothes you wear are the object, so they end with ـًا: أَلْبَسُ مِعْطَفًا. مِعْطَفٌ is a coat and مِظَلَّةٌ is an umbrella.
    """)}},
    {"u": "1-5-9", "r": 2, "e": 2, "was": "أَلْبَسُ ثَوْبًا أَبْيَضَ", "set": {"note": "أَبْيَضُ describes ثَوْبًا, so it ends with ـَ too. Colour words never take tanween."}},
    {"u": "1-5-9", "r": 2, "e": 4, "was": "مَاذَا تَلْبَسُ اليَوْمَ؟", "set": {"en": "what are you wearing today? (to a man)"}},
    # A past action needs a past reason: use the كَانَ from this unit.
    {"u": "1-5-9", "r": 2, "e": 6, "was": "لَبِسْتُ مِعْطَفًا لِأَنَّ الجَوَّ بَارِدٌ", "set": {"ar": "لَبِسْتُ مِعْطَفًا لِأَنَّ الجَوَّ كَانَ بَارِدًا", "tr": "labistu miʿṭafan li-anna l-jawwa kāna bāridan", "en": "I wore a coat because the weather was cold", "note": "After لِأَنَّ, الجَوُّ becomes الجَوَّ. Then كَانَ makes بَارِدٌ into بَارِدًا."}},
    {"u": "1-5-9", "l": 6, "was": "كَانَ الجَوُّ مُعْتَدِلًا", "set": {"ar": "كَانَ الجَوُّ مُعْتَدِلًا، وَكَانَتْ هُنَاكَ رِيحٌ."}},
]
