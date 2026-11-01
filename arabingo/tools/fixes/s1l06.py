# Stage 1 · Level 6 — content corrections and improvements.
FIXES = [
    {"u": "1-6-1", "r": 1, "was": "Describing people", "set": {"body": B("""
        A describing word comes after the noun and agrees with it. For a woman, add ـَةٌ: سَعِيدٌ becomes سَعِيدَةٌ.
        رَجُلٌ is "a man" and امْرَأَةٌ is "a woman". Their plurals are رِجَالٌ (men) and نِسَاءٌ (women). With اَلْ, امْرَأَةٌ drops its first ا and becomes المَرْأَةُ.
    """)}},
    # "This is a man" and "this man" are different: the second is only a phrase.
    {"u": "1-6-1", "r": 2, "was": "Friends, neighbours and children", "set": {"body": B("""
        Here are words for people around you. Learn the singular and the plural together. Add ـِي to say "my": صَدِيقِي is "my friend".
        Ask who someone is with مَنْ هَذَا؟ for a man and مَنْ هَذِهِ؟ for a woman.
        - هَذَا رَجُلٌ, with no اَلْ, is a sentence: "this is a man".
        - هَذَا الرَّجُلُ, with اَلْ, is only a phrase: "this man". Add more words to say something about him: هَذَا الرَّجُلُ جَارِي (this man is my neighbour).
    """)}},
    {"u": "1-6-1", "r": 2, "e": 1, "was": "هَذَا صَدِيقِي", "set": {"note": "The plural of صَدِيقٌ is أَصْدِقَاءُ. A woman friend is صَدِيقَةٌ."}},
    {"u": "1-6-1", "r": 2, "e": 4, "was": "هَذِهِ جَارَتِي", "set": {"note": "جَارَةٌ is a woman neighbour. Before ـِي, the ة becomes ت: جَارَتِي."}},
    {"u": "1-6-1", "q": 13, "was": "How do you say \"this man is my neighbour\"?", "set": {"w": ["هَذَا رَجُلٌ جَارِي", "هَذِهِ الرَّجُلُ جَارِي"]}},

    # Places were in Level 4, and the restaurant was never taught before.
    {"u": "1-6-2", "r": 1, "was": "Places in the city", "set": {"body": B("""
        You learned some places in the city in Level 4, such as مَسْجِدٌ and مَطَارٌ. Learn more of them now.
        Many place words start with مَـ, which often means "the place of": مَطْعَمٌ (restaurant) comes from طَعَامٌ, "food". The post office is مَكْتَبُ البَرِيدِ, "the office of the post".
    """)}},
    {"u": "1-6-2", "r": 1, "e": 2, "was": "هَذَا بَنْكٌ", "set": {"note": "The plural is بُنُوكٌ. In formal Arabic a bank is also called مَصْرِفٌ."}},
    {"u": "1-6-2", "r": 1, "e": 7, "was": "هَذَا مَطْعَمٌ", "set": {"note": "The plural is مَطَاعِمُ. It is the place where you eat طَعَامٌ (food)."}},
    {"u": "1-6-2", "w": 0, "add": {"ar": "مَطْعَمٌ", "pl": "مَطَاعِمُ", "en": "restaurant", "type": "noun"}},
    {"u": "1-6-2", "r": 2, "was": "Near and far", "set": {"body": B("""
        Use قَرِيبٌ مِنْ for "near to" and بَعِيدٌ عَنْ for "far from". Use بَيْنَ for "between". You already know أَمَامَ, خَلْفَ and بِجَانِبِ from Level 4.
        The noun after all these words ends with ـِ: بَيْنَ البَنْكِ وَالمَسْجِدِ.
    """)}},
    {"u": "1-6-2", "r": 2, "e": 5, "was": "هَلْ المَطْعَمُ قَرِيبٌ؟", "set": {"ar": "هَلِ المَطْعَمُ قَرِيبٌ؟", "tr": "hali l-maṭʿamu qarībun", "note": "Before اَلْ, هَلْ becomes هَلِ so the words run together."}},
    # بَعِيدٌ مِنْ is also correct Arabic, so it cannot be a wrong answer.
    {"u": "1-6-2", "q": 10, "was": "How do you say \"the bank is far from the house\"?", "set": {"w": ["البَنْكُ قَرِيبٌ مِنَ البَيْتِ", "البَنْكُ بَعِيدٌ عَنِ البَيْتُ"]}},

    {"u": "1-6-3", "r": 1, "was": "Giving directions", "set": {"body": B("""
        يَمِينٌ is "right" and يَسَارٌ is "left". Say عَلَى اليَمِينِ for "on the right" and عَلَى اليَسَارِ for "on the left".
        To give directions, use the command form you met in Level 1. For a man it ends with a sukoon, and for a woman it ends with ـِي.
        - اِذْهَبْ and اِذْهَبِي mean "go".
        - اِنْعَطِفْ and اِنْعَطِفِي mean "turn".
        مُسْتَقِيمًا means "straight ahead", and ثُمَّ means "then".
    """)}},
    {"u": "1-6-3", "r": 1, "e": 3, "was": "اِذْهَبْ مُسْتَقِيمًا", "set": {"note": "The command for a man ends with a sukoon."}},
    # In the middle of a sentence the first ا of a command is silent.
    {"u": "1-6-3", "r": 1, "e": 8, "was": "اِذْهَبْ مُسْتَقِيمًا ثُمَّ", "set": {"ar": "اِذْهَبْ مُسْتَقِيمًا ثُمَّ انْعَطِفْ عَلَى اليَمِينِ", "tr": "idhhab mustaqīman thumma nʿaṭif ʿalā l-yamīni", "note": "ثُمَّ joins two steps. In the middle of a sentence the first ا of انْعَطِفْ is silent, so you say \"thumma nʿaṭif\"."}},
    {"u": "1-6-3", "w": 8, "was": "اِنْعَطَفَ", "set": {"pl": "يَنْعَطِفُ"}},
    {"u": "1-6-3", "q": 8, "was": "How does a man ask \"Do you know where the bank is?\"", "set": {"q": "How do you ask a man \"Do you know where the bank is?\""}},
    {"u": "1-6-3", "l": 4, "was": "اِذْهَبْ مُسْتَقِيمًا ثُمَّ", "set": {"ar": "اِذْهَبْ مُسْتَقِيمًا ثُمَّ انْعَطِفْ عَلَى اليَمِينِ."}},
    # Yusuf asked for directions, so he thanks Layla, not the other way round.
    {"u": "1-6-3", "l": 12, "was": "نَعَمْ، هُوَ سَعِيدٌ", "set": {"ar": "نَعَمْ، هُوَ سَعِيدٌ."}},
    {"u": "1-6-3", "l": 13, "was": "عَفْوًا", "set": {"ar": "شُكْرًا. مَعَ السَّلَامَةِ."}},
    {"u": "1-6-3", "l": 0, "add": {"w": "f", "n": "لَيْلَى", "ar": "عَفْوًا. مَعَ السَّلَامَةِ."}},
    {"u": "1-6-3", "cq": 9, "was": "Is the man happy?", "set": {"w": ["لَا، هُوَ مُتْعَبٌ", "لَا، هُوَ مَرِيضٌ"]}},
    {"u": "1-6-3", "cq": 10, "was": "How does Yusuf say \"you are welcome\"?", "set": {"q": "How does Layla say \"you are welcome\"?"}},

    {"u": "1-6-4", "r": 1, "was": "What is your hobby?", "set": {"body": B("""
        هِوَايَةٌ means "hobby", and the plural is هِوَايَاتٌ. Ask مَا هِوَايَتُكَ؟ to a man and مَا هِوَايَتُكِ؟ to a woman. Answer with هِوَايَتِي and the name of the hobby.
        The name of a hobby is a noun made from a verb, called a مَصْدَرٌ: قَرَأَ (he read) gives القِرَاءَةُ (reading), and سَبَحَ (he swam) gives السِّبَاحَةُ (swimming).
    """)}},
    {"u": "1-6-4", "r": 1, "e": 2, "was": "هِوَايَتِي القِرَاءَةُ", "set": {"tr": "hiwāyatī l-qirāʾatu"}},
    {"u": "1-6-4", "r": 1, "e": 4, "was": "هِوَايَتِي السِّبَاحَةُ", "set": {"tr": "hiwāyatī s-sibāḥatu"}},
    {"u": "1-6-4", "r": 1, "e": 5, "was": "هِوَايَتُهُ الرَّسْمُ", "set": {"tr": "hiwāyatuhu r-rasmu"}},
    {"u": "1-6-4", "r": 1, "e": 6, "was": "هِوَايَتُهَا الطَّبْخُ", "set": {"tr": "hiwāyatuhā ṭ-ṭabkhu"}},
    {"u": "1-6-4", "r": 2, "was": "I like and I do not like", "set": {"body": B("""
        You know أُحِبُّ. After it, the name of a hobby with اَلْ ends with ـَ: أُحِبُّ القِرَاءَةَ. To say "I do not like", put لَا before أُحِبُّ. Add كَثِيرًا for "a lot".
        Ask a man هَلْ تُحِبُّ...؟ and a woman هَلْ تُحِبِّينَ...؟. In the answer, ـهُ means "it" for a masculine word and ـهَا for a feminine word: أُحِبُّهُ, أُحِبُّهَا.
    """)}},
    {"u": "1-6-4", "r": 2, "e": 3, "was": "لَا أُحِبُّ الجَرْيَ", "set": {"tr": "lā uḥibbu l-jarya"}},
    {"u": "1-6-4", "w": 11, "was": "رَسَمَ", "set": {"pl": "يَرْسُمُ"}},
    {"u": "1-6-4", "w": 12, "was": "طَبَخَ", "set": {"pl": "يَطْبُخُ"}},
    {"u": "1-6-4", "w": 13, "was": "مَشَى", "set": {"pl": "يَمْشِي"}},

    {"u": "1-6-5", "r": 1, "was": "Verbs for hobbies", "set": {"body": B("""
        These verbs tell what you do. In the present, the first letter shows who does the action, as you saw in Level 4.
        - أَ is for "I": أَلْعَبُ (I play).
        - يَـ is for "he" and تَـ is for "she": يَلْعَبُ, تَلْعَبُ.
        - نَـ is for "we": نَلْعَبُ (we play).
    """)}},
    {"u": "1-6-5", "r": 1, "e": 7, "was": "أَلْعَبُ مَعَ أَصْدِقَائِي", "set": {"note": "أَصْدِقَاءُ with ـِي gives أَصْدِقَائِي. Before the ـِي, the hamza sits on a seat shaped like ي: ئ."}},
    {"u": "1-6-5", "r": 2, "was": "How often?", "set": {"body": B("""
        Use these words to say how often you do something. دَائِمًا means "always", أَحْيَانًا means "sometimes", and كُلَّ يَوْمٍ means "every day". To say "never", put لَا before the verb and أَبَدًا after it.
        مَرَّةٌ means "one time" or "once". مَرَّتَيْنِ is "twice", and from three to ten use the plural: ثَلَاثَ مَرَّاتٍ.
    """)}},
    {"u": "1-6-5", "r": 2, "e": 6, "was": "أَسْبَحُ مَرَّتَيْنِ", "set": {"note": "مَرَّتَيْنِ means \"twice\". It is the dual of مَرَّةٌ."}},
    {"u": "1-6-5", "r": 2, "e": 8, "was": "ثَلَاثَ مَرَّاتٍ", "set": {"note": "مَرَّةٌ is feminine, so the number drops ـَةٌ: ثَلَاثَ, not ثَلَاثَةَ. The plural مَرَّاتٌ ends with ـٍ."}},

    {"u": "1-6-6", "r": 1, "was": "Free time and the weekend", "set": {"body": B("""
        وَقْتٌ means "time" and فَرَاغٌ means "emptiness", so وَقْتُ الفَرَاغِ is "free time". نِهَايَةٌ means "end", so نِهَايَةُ الأُسْبُوعِ, "the end of the week", is "the weekend". Say فِي before them: فِي وَقْتِ الفَرَاغِ.
        Talk about the past with the verbs you know: لَعِبْتُ (I played), سَبَحْتُ (I swam), رَسَمْتُ (I drew), طَبَخْتُ (I cooked) and مَشَيْتُ (I walked). For the future, put سَـ before the present: سَأَلْعَبُ (I will play).
    """)}},
    {"u": "1-6-6", "w": 4, "was": "لَعِبَ", "set": {"pl": "يَلْعَبُ"}},
    {"u": "1-6-6", "w": 5, "was": "سَبَحَ", "set": {"pl": "يَسْبَحُ"}},

    {"u": "1-6-7", "r": 1, "was": "Means of transport", "set": {"body": B("""
        You know سَيَّارَةٌ. Learn more ways to travel. To say how you travel, put بِـ ("by") before the noun. بِـ is written joined to the next word, and the noun after it ends with ـِ: بِالطَّائِرَةِ (by plane).
        Ask بِمَاذَا تُسَافِرُ؟, literally "by what do you travel?".
    """)}},
    {"u": "1-6-7", "r": 2, "was": "At the airport", "set": {"body": B("""
        مَطَارٌ means "airport". Here are the main things you see and need there. جَوَازُ السَّفَرِ means "the passport", literally "the permit of travel".
    """)}},
    {"u": "1-6-7", "r": 2, "e": 6, "was": "أَيْنَ بَوَّابَةُ الرِّحْلَةِ؟", "set": {"note": "This is an إِضَافَةٌ: بَوَّابَةُ has no tanween, and الرِّحْلَةِ ends with ـِ."}},
    {"u": "1-6-7", "r": 2, "e": 7, "was": "هِيَ عَلَى اليَمِينِ", "set": {"note": "You learned عَلَى اليَمِينِ with the directions in this level. هِيَ is used because بَوَّابَةٌ is feminine."}},

    {"u": "1-6-8", "r": 1, "was": "Booking a ticket", "set": {"body": B("""
        حَجْزٌ means "booking". أَحْجِزُ means "I book" and حَجَزْتُ means "I booked".
        - ذَهَابٌ means "going", so a one-way ticket is ذَهَابٌ فَقَطْ, "going only".
        - إِيَابٌ means "coming back", so a return ticket is ذَهَابٌ وَإِيَابٌ.
        Ask the price with كَمْ سِعْرُ...؟ ("how much is the price of...?") or with بِكَمْ, as in Level 5.
    """)}},
    {"u": "1-6-8", "r": 1, "e": 2, "was": "ذَهَابٌ فَقَطْ", "set": {"note": "ذَهَابٌ means \"going\" and فَقَطْ means \"only\"."}},
    {"u": "1-6-8", "r": 1, "e": 5, "was": "أَرْبَعُمِئَةِ رِيَالٍ", "set": {"note": "Number 400, written ٤٠٠. Like ثَلَاثُمِئَةٍ, it is written as one word."}},
    {"u": "1-6-8", "r": 1, "e": 7, "was": "حَجَزْتُ تَذْكِرَتَيْنِ", "set": {"note": "تَذْكِرَتَانِ becomes تَذْكِرَتَيْنِ because it is the object of the verb."}},
    {"u": "1-6-8", "w": 16, "was": "حَجَزَ", "set": {"pl": "يَحْجِزُ"}},
    {"u": "1-6-8", "r": 2, "was": "Telling the time", "set": {"body": B("""
        You met كَمِ السَّاعَةُ؟ ("what time is it?") in Level 3. Answer with السَّاعَةُ and an ordinal number (first, second, third...). سَاعَةٌ is feminine, so the ordinal ends with ـَةُ: السَّاعَةُ الثَّالِثَةُ is "three o'clock", literally "the third hour".
        Most ordinals come from the numbers you know: ثَلَاثَةٌ gives الثَّالِثَةُ. "First" is different: الأُولَى. For 11 and 12 o'clock, say الحَادِيَةَ عَشْرَةَ and الثَّانِيَةَ عَشْرَةَ.
        Add وَالنِّصْفُ for "half past" and وَالرُّبْعُ for "a quarter past". To say "at", put فِي before السَّاعَةِ.
    """)}},
    {"u": "1-6-8", "r": 2, "e": 11, "was": "مَتَى تُسَافِرُ؟", "set": {"en": "when are you travelling? (to a man)"}},
    {"u": "1-6-8", "r": 2, "e": 12, "was": "أُسَافِرُ فِي السَّاعَةِ الثَّالِثَةِ", "set": {"en": "I am travelling at three o'clock"}},

    # Country names do change after إِلَى; and لَمْ was used without being taught.
    {"u": "1-6-9", "r": 1, "was": "Trips in the past and the future", "set": {"body": B("""
        Use the verbs you know. سَافَرْتُ means "I travelled" and سَأُسَافِرُ means "I will travel". Say وَصَلْتُ for "I arrived" and رَجَعْتُ for "I returned".
        Most country names without اَلْ, like مِصْرُ, take no tanween, so after إِلَى they end with ـَ: إِلَى مِصْرَ. A name that ends with a long ا, like تُرْكِيَا, never changes.
        To say "I did not travel", you can use مَا with the past, as you know: مَا سَافَرْتُ. Another common way is لَمْ with the present form, which then ends with a sukoon: لَمْ أُسَافِرْ.
    """)}},
    {"u": "1-6-9", "r": 1, "e": 6, "was": "هَلْ سَافَرْتَ إِلَى الإِمَارَاتِ؟", "set": {"tr": "hal sāfarta ilā l-imārāti", "note": "الإِمَارَاتُ has اَلْ, so after إِلَى it ends with ـِ."}},
    {"u": "1-6-9", "r": 1, "e": 7, "was": "لَا، لَمْ أُسَافِرْ", "set": {"note": "After لَمْ, أُسَافِرُ loses its ـُ and ends with a sukoon. It means the same as مَا سَافَرْتُ."}},
    {"u": "1-6-9", "w": 1, "was": "رَجَعَ", "set": {"pl": "يَرْجِعُ"}},
    {"u": "1-6-9", "cq": 1, "was": "Where does Khalid want a ticket to?", "set": {"a": "إِلَى القَاهِرَةِ", "w": ["إِلَى جُدَّةَ", "إِلَى تُرْكِيَا"]}},
    {"u": "1-6-9", "cq": 7, "was": "What does the employee ask him", "set": {"q": "What does the employee ask him about?"}},
]
