# Stage 1 · Level 10 (was Stage 2 · Level 1) — content corrections and improvements.
INTRO_ABOUT = "Now you will talk about the wider world. First you will learn the passive voice (what was done, without saying who did it), how to use لَوْ and إِنْ for \"if\", and يُوجَدُ for \"there is\"."
FIXES = [
    # This theme used to open "Level 4".
    {"u": "1-10-1", "set": {"about": INTRO_ABOUT}},
    {"u": "1-10-2", "set": {"about": INTRO_ABOUT}},

    {"u": "1-10-1", "r": 1, "was": "The passive: what was done", "set": {"body": B("""
        Sometimes we do not say who did something: "the book was written", "the door was opened". Arabic shows this by changing the vowels of the verb. The first letter takes ـُ, and the letter before the last takes ـِ.
        - كَتَبَ (he wrote) becomes كُتِبَ (it was written).
        - فَتَحَ (he opened) becomes فُتِحَ (it was opened).
        The thing it happened to becomes the subject, so it ends with ـُ: كُتِبَ الكِتَابُ. For a feminine subject add ـتْ: كُتِبَتِ الرِّسَالَةُ.
    """)}},
    {"u": "1-10-1", "r": 2, "was": "Now-form passive", "set": {"body": B("""
        In the present, the passive starts with يُـ, or تُـ for a feminine subject, and the letter before the last takes ـَ.
        - يَكْتُبُ (he writes) becomes يُكْتَبُ (it is written).
        - يَفْتَحُ (he opens) becomes يُفْتَحُ (it is opened).
        Use it for general facts and for how things are done: تُكْتَبُ هَكَذَا (it is written like this).
    """)}},
    {"u": "1-10-1", "r": 2, "e": 4, "was": "يُقَالُ إِنَّ العَرَبِيَّةَ", "set": {"note": "يُقَالُ (it is said) is the passive of يَقُولُ. After قَالَ and يُقَالُ, \"that\" is إِنَّ, not أَنَّ."}},

    {"u": "1-10-2", "set": {"titleAr": "لَوْ، إِنْ، إِذَا · يُوجَدُ"}},
    {"u": "1-10-2", "r": 1, "was": "If", "set": {"body": B("""
        Arabic has three words for "if".
        - إِذَا, which you know, is for something likely: إِذَا ذَهَبْتَ (if you go).
        - إِنْ is for something possible. It is more formal, and its answer often starts with فَـ: إِنْ نَجَحْتَ فَلَكَ جَائِزَةٌ.
        - لَوْ is for something unreal, "if it were so". Use the past after it, and start the answer with لَـ: لَوْ دَرَسْتَ لَنَجَحْتَ (if you had studied, you would have passed).
    """)}},
    {"u": "1-10-2", "r": 1, "e": 4, "was": "إِنْ شَاءَ اللَّهُ", "set": {"note": "إِنْ here means \"if\". Muslims say it whenever they speak about the future."}},
    {"u": "1-10-2", "r": 2, "was": "There is", "set": {"title": "There is (يُوجَدُ)", "body": B("""
        You know هُنَاكَ ("there is"). A more formal way is يُوجَدُ, the passive of وَجَدَ (he found): "it is found", so "there is". Use تُوجَدُ for a feminine noun.
        - For "there is not", say لَا يُوجَدُ or لَيْسَ هُنَاكَ.
        - For "there was", put كَانَ before هُنَاكَ: كَانَ هُنَاكَ ازْدِحَامٌ.
        The noun after them usually has no اَلْ and ends with tanween.
    """)}},
    # Mosques open before dawn, for the Fajr prayer.
    {"u": "1-10-2", "l": 4, "was": "بُنِيَ قَبْلَ سَنَةٍ", "set": {"ar": "بُنِيَ قَبْلَ سَنَةٍ، وَيُفْتَحُ قَبْلَ الفَجْرِ."}},
    {"u": "1-10-2", "cq": 4, "was": "When is it opened?", "set": {"a": "قَبْلَ الفَجْرِ", "w": ["بَعْدَ الظُّهْرِ", "فِي المَسَاءِ"]}},

    {"u": "1-10-3", "r": 1, "e": 7, "was": "هَذِهِ أَخْبَارٌ جَدِيدَةٌ", "set": {"en": "this is fresh news", "note": "أَخْبَارٌ means \"news\". It is the plural of خَبَرٌ, a thing, so it is described with a feminine singular word."}},
    # These verbs share the pattern اِفْتَعَلَ: a تَـ after the first root letter.
    {"u": "1-10-3", "r": 2, "was": "Contacting and meeting", "set": {"body": B("""
        Some verbs start with اِ and add a تَـ after the first root letter. This pattern is called اِفْتَعَلَ.
        - اِجْتَمَعَ (root ج م ع, "gather") means "he met" with others.
        - اِنْتَشَرَ (root ن ش ر) means "it spread".
        - اِتَّصَلَ بِـ (root و ص ل, "join") means "he contacted, he called". The و merges with the ت, giving تّ.
        Their present forms start with يَـ: يَجْتَمِعُ, يَنْتَشِرُ, يَتَّصِلُ. The اِ at the start is only said at the beginning of a sentence.
    """)}},
    {"u": "1-10-3", "r": 2, "e": 3, "was": "اِجْتَمَعَ الأَصْدِقَاءُ", "set": {"note": "The verb comes first, so it stays singular."}},
    {"u": "1-10-3", "r": 2, "e": 6, "was": "اِسْتَقْبَلْنَا الضُّيُوفَ", "set": {"note": "ضَيْفٌ is a guest; its plural is ضُيُوفٌ. اِسْتَقْبَلَ starts with اِسْتَـ, another pattern you will meet often."}},
    {"u": "1-10-3", "r": 2, "e": 7, "was": "اِتَّصَلْتُ بِكَ أَمْسِ", "set": {"note": "بِكَ is بِـ with ـكَ, \"you\"."}},
    # With a verb first, a broken plural of people may also take a feminine verb, so that is not a safe wrong answer.
    {"u": "1-10-3", "q": 12, "was": "How do you say \"the friends met\"?", "set": {"w": ["اِجْتَمَعُوا الأَصْدِقَاءُ", "يَجْتَمِعُ الأَصْدِقَاءُ"]}},
    # The call came before the complaint about being busy; and the "news" now has something to spread.
    {"u": "1-10-4", "l": 3, "was": "أَتَّصِلُ بِكِ كُلَّ يَوْمٍ", "set": {"ar": "كُلَّمَا اتَّصَلْتُ بِكِ كُنْتِ مَشْغُولَةً."}},
    {"u": "1-10-4", "l": 7, "was": "كُلَّمَا اِتَّصَلْتُ بِكِ", "set": {"ar": "سَأَتَّصِلُ بِكِ كُلَّ يَوْمٍ."}},
    {"u": "1-10-4", "l": 8, "was": "وَأَنَا أُرْسِلُ رِسَالَةً", "set": {"ar": "وَأَنَا أُرْسِلُ رِسَالَةً كُلَّ يَوْمٍ. نَجَحْتُ فِي الامْتِحَانِ!"}},
    {"u": "1-10-4", "l": 9, "was": "شُكْرًا. اِنْتَشَرَ", "set": {"ar": "مَبْرُوكٌ! اِنْتَشَرَ الخَبَرُ بِسُرْعَةٍ."}},
    {"u": "1-10-4", "l": 10, "was": "مَعَ السَّلَامَةِ", "set": {"ar": "شُكْرًا. مَعَ السَّلَامَةِ."}},
    {"u": "1-10-4", "cq": 10, "was": "What does Maryam say at the end?", "set": {"w": ["مَبْرُوكٌ", "عَفْوًا"]}},

    {"u": "1-10-4", "r": 1, "was": "The more, the more", "set": {"body": B("""
        كُلَّمَا means "every time" or, in a comparison, "the more... the more". Both verbs are usually in the past, but the meaning is general: كُلَّمَا قَرَأْتُ تَعَلَّمْتُ (the more I read, the more I learn).
    """)}},
    # In the middle of a sentence the first ا of these verbs is silent.
    {"u": "1-10-4", "r": 1, "e": 1, "was": "كُلَّمَا اِتَّصَلْتُ بِهِ", "set": {"ar": "كُلَّمَا اتَّصَلْتُ بِهِ كَانَ مَشْغُولًا", "tr": "kullamā ttaṣaltu bihi kāna mashghūlan", "note": "مَشْغُولٌ means \"busy\". After كُلَّمَا the first ا of اتَّصَلْتُ is silent."}},
    {"u": "1-10-4", "r": 1, "e": 3, "was": "كُلَّمَا اِزْدَادَ العِلْمُ", "set": {"ar": "كُلَّمَا ازْدَادَ العِلْمُ ازْدَادَ الأَدَبُ", "tr": "kullamā zdāda l-ʿilmu zdāda l-adabu"}},
    {"u": "1-10-4", "q": 5, "was": "How do you say \"every time I called him, he was busy\"?", "set": {"a": "كُلَّمَا اتَّصَلْتُ بِهِ كَانَ مَشْغُولًا", "w": ["كُلَّمَا اتَّصَلْتُ بِهِ كَانَ مَشْغُولٌ", "كُلَّمَا أَتَّصِلُ بِهِ كَانَ مَشْغُولًا"]}},
    {"u": "1-10-4", "r": 2, "was": "Although", "set": {"body": B("""
        مَعَ أَنَّ means "although". Like أَنَّ, it is followed by a noun ending with ـَ, or it takes a pronoun ending: مَعَ أَنَّهُ (although he).
        لَكِنَّ means "but" and works the same way: لَكِنَّهُ (but he). You know the short form وَلَكِنْ, which is followed by a whole sentence with no change.
    """)}},
    {"u": "1-10-4", "r": 2, "e": 2, "was": "مَعَ أَنَّهُ مَشْغُولٌ", "set": {"ar": "مَعَ أَنَّهُ مَشْغُولٌ، يَرُدُّ دَائِمًا", "tr": "maʿa annahu mashghūlun, yaruddu dāʾiman", "en": "although he is busy, he always answers"}},

    # "النظافة من الإيمان" is a popular saying; the authentic hadith is الطُّهُورُ شَطْرُ الإِيمَانِ.
    {"u": "1-10-5", "r": 1, "was": "Cleaning words", "set": {"body": B("""
        نَظَافَةٌ is cleanliness. نَظِيفٌ means "clean" and وَسِخٌ means "dirty".
        Cleanliness matters in Islam. A popular saying is النَّظَافَةُ مِنَ الإِيمَانِ (cleanliness is part of faith), and the Prophet ﷺ said: الطُّهُورُ شَطْرُ الإِيمَانِ, "purity is half of faith".
    """)}},
    {"u": "1-10-5", "r": 1, "e": 1, "was": "النَّظَافَةُ مِنَ الإِيمَانِ", "set": {"note": "إِيمَانٌ means \"faith\". This is a well-known saying, not the words of a hadith."}},
    {"u": "1-10-5", "w": 15, "was": "وَسِخٌ", "set": {"pl": "وَسِخُونَ"}},
    {"u": "1-10-5", "r": 2, "was": "Cleaning verbs", "set": {"body": B("""
        غَسَلَ means "he washed" (يَغْسِلُ, "he washes"). نَظَّفَ, with a doubled ظ, means "he cleaned". رَمَى means "he threw" and كَنَسَ means "he swept".
        The thing you wash or clean is the object, so it ends with ـَ: نَظَّفْتُ الغُرْفَةَ.
    """)}},

    {"u": "1-10-6", "r": 1, "was": "Commands", "set": {"body": B("""
        You learned commands in Levels 6 and 7. Here is the full rule: start from the "you" verb and drop its تَـ or تُـ.
        - For a man, end with a sukoon: تَغْسِلُ becomes اِغْسِلْ (wash!), and تُنَظِّفُ becomes نَظِّفْ (clean!). Add اِ in front only when the word would start with a sukoon.
        - For a woman, end with ـِي: اِغْسِلِي. For a group, end with ـُوا: نَظِّفُوا.
        - For "do not", keep the "you" verb after لَا, with the same endings: لَا تَغْسِلْ, لَا تَغْسِلِي. A verb that ends in a long vowel loses it: تَرْمِي becomes لَا تَرْمِ.
    """)}},
    {"u": "1-10-6", "r": 1, "e": 5, "was": "لَا تَشْرَبِ المَاءَ الوَسِخَ", "set": {"note": "The sukoon of تَشْرَبْ becomes ـِ before اَلْ. الوَسِخَ describes المَاءَ, so it ends with ـَ too."}},
    {"u": "1-10-6", "r": 1, "e": 6, "was": "حَاضِرٌ، سَأَغْسِلُ يَدَيَّ", "set": {"en": "right away, I will wash my hands"}},
    # Wudu must include washing the arms to the elbows (Quran 5:6); it was missing.
    {"u": "1-10-6", "r": 2, "was": "Steps", "set": {"body": B("""
        ثُمَّ means "then". Use it to give steps in order. أَوَّلًا means "first", ثَانِيًا "second" and أَخِيرًا "finally".
        Learn them with the main steps of wudu: wash the hands, then the face, then the arms up to the elbows, then wipe the head, and finally wash the feet.
    """)}},
    {"u": "1-10-6", "r": 2, "e": 3, "was": "ثُمَّ أَمْسَحُ رَأْسِي", "set": {"ar": "ثُمَّ أَغْسِلُ ذِرَاعَيَّ إِلَى المِرْفَقَيْنِ", "tr": "thumma aghsilu dhirāʿayya ilā l-mirfaqayni", "en": "then I wash my arms up to the elbows", "note": "ذِرَاعٌ is the arm and مِرْفَقٌ is the elbow. Both are in the dual here."}},
    {"u": "1-10-6", "r": 2, "e": 4, "was": "أَخِيرًا أَغْسِلُ قَدَمَيَّ", "set": {"ar": "ثُمَّ أَمْسَحُ رَأْسِي", "tr": "thumma amsaḥu raʾsī", "en": "then I wipe my head", "note": "مَسَحَ means \"he wiped\". رَأْسٌ is a head."}},
    {"u": "1-10-6", "r": 2, "e": 5, "was": "الوُضُوءُ قَبْلَ الصَّلَاةِ", "set": {"ar": "أَخِيرًا أَغْسِلُ قَدَمَيَّ", "tr": "akhīran aghsilu qadamayya", "en": "finally I wash my feet", "note": "قَدَمٌ is a foot. Two feet are قَدَمَانِ; with \"my\" it is قَدَمَيَّ."}},
    {"u": "1-10-6", "r": 2, "add": {"ar": "الوُضُوءُ قَبْلَ الصَّلَاةِ", "tr": "al-wuḍūʾu qabla ṣ-ṣalāti", "en": "wudu is before prayer", "note": "وُضُوءٌ is wudu, the washing before prayer."}},
    {"u": "1-10-6", "w": 0, "add": {"ar": "ذِرَاعٌ", "pl": "أَذْرُعٌ", "en": "arm", "type": "noun"}},
    {"u": "1-10-6", "w": 0, "add": {"ar": "مِرْفَقٌ", "pl": "مَرَافِقُ", "en": "elbow", "type": "noun"}},
    {"u": "1-10-6", "l": 5, "was": "نَعَمْ، ثُمَّ تَمْسَحُ رَأْسَكَ", "set": {"ar": "نَعَمْ، ثُمَّ تَغْسِلُ ذِرَاعَيْكَ، ثُمَّ تَمْسَحُ رَأْسَكَ."}},

    {"u": "1-10-7", "r": 1, "was": "Islam and faith", "set": {"body": B("""
        دِينٌ is a religion. مُسْلِمٌ is a Muslim, and the plural is مُسْلِمُونَ. أَسْلَمَ means "he became Muslim". آمَنَ بِـ means "he believed in", and a believer is مُؤْمِنٌ.
        A pillar is رُكْنٌ (plural أَرْكَانٌ). The six pillars of faith (أَرْكَانُ الإِيمَانِ) are belief in Allah, His angels, His books, His messengers, the Last Day, and destiny (القَدَرُ).
    """)}},
    {"u": "1-10-7", "r": 1, "e": 1, "was": "الإِسْلَامُ دِينُ السَّلَامِ", "set": {"note": "This is an إِضَافَةٌ: \"the religion of peace\". الإِسْلَامُ and السَّلَامُ share the root س ل م."}},
    {"u": "1-10-7", "r": 1, "e": 3, "was": "آمَنْتُ بِاللَّهِ", "set": {"en": "I have believed in Allah"}},
    {"u": "1-10-7", "r": 1, "e": 6, "was": "أُؤْمِنُ بِاليَوْمِ الآخِرِ", "set": {"note": "آخِرٌ means \"last\"; do not mix it up with آخَرُ, \"other\". The Last Day is the Day of Judgement."}},
    {"u": "1-10-7", "r": 2, "was": "The five pillars", "set": {"body": B("""
        There are five pillars of Islam (أَرْكَانُ الإِسْلَامِ): the two testimonies of faith, prayer, zakat, fasting in Ramadan, and Hajj to the House for those who are able.
    """)}},
    {"u": "1-10-7", "r": 2, "e": 1, "was": "الشَّهَادَتَانِ", "set": {"note": "The Shahada has two parts, so it is called الشَّهَادَتَانِ, with the dual ending ـَانِ."}},
    {"u": "1-10-7", "r": 2, "e": 5, "was": "الزَّكَاةُ", "set": {"en": "zakat, the obligatory alms", "note": "Zakat purifies wealth. مَالٌ is wealth or money."}},
    {"u": "1-10-7", "r": 2, "e": 7, "was": "حَجُّ البَيْتِ", "set": {"note": "The House is the Kaʿbah. You learned الحَجُّ in Level 7."}},
    {"u": "1-10-7", "r": 2, "e": 8, "was": "أَرْكَانُ الإِسْلَامِ خَمْسَةٌ", "set": {"note": "رُكْنٌ is masculine, so the number keeps ـَةٌ: خَمْسَةٌ."}},

    {"u": "1-10-8", "r": 1, "was": "Counting three to ten", "set": {"body": B("""
        You learned in Level 3 that the numbers from 3 to 10 take the opposite gender of the thing counted, and the thing is plural and ends with ـٍ. The key is to look at the singular, not the plural.
        - رِجَالٌ comes from رَجُلٌ, which is masculine, so the number keeps ـَةٌ: ثَمَانِيَةُ رِجَالٍ.
        - سَمَاوَاتٌ comes from سَمَاءٌ, which is feminine, so the number drops ـَةٌ: سَبْعُ سَمَاوَاتٍ.
        - نِسَاءٌ is the plural of امْرَأَةٌ, which is feminine: تِسْعُ نِسَاءٍ.
        For 1 and 2 the noun stays singular: كِتَابٌ وَاحِدٌ, كِتَابَانِ.
    """)}},
    {"u": "1-10-8", "r": 1, "e": 5, "was": "سِتَّةُ أَرْكَانٍ", "set": {"note": "There are six pillars of faith. رُكْنٌ is masculine, so سِتَّةُ keeps ـَةٌ."}},
    {"u": "1-10-8", "r": 1, "e": 7, "was": "ثَمَانِيَةُ رِجَالٍ", "set": {"note": "Look at the singular رَجُلٌ: it is masculine, so the number keeps ـَةٌ."}},
    {"u": "1-10-8", "r": 1, "e": 9, "was": "عَشَرَةُ طُلَّابٍ", "set": {"note": "The singular طَالِبٌ is masculine, so the number is عَشَرَةُ."}},
    {"u": "1-10-8", "r": 2, "was": "The Quran and the Prophet", "set": {"body": B("""
        قُرْآنٌ is the Quran. سُورَةٌ is a chapter of it, and آيَةٌ is a verse. نَبِيٌّ is a prophet.
        After the Prophet's name, Muslims say صَلَّى اللَّهُ عَلَيْهِ وَسَلَّمَ, "may Allah send blessings and peace upon him". It is written ﷺ for short.
    """)}},
    # The first prayer of the day is Fajr itself, not a prayer after it.
    {"u": "1-10-8", "l": 5, "was": "كَمْ مَرَّةً الصَّلَاةُ", "set": {"ar": "كَمْ مَرَّةً نُصَلِّي فِي اليَوْمِ؟"}},
    {"u": "1-10-8", "l": 6, "was": "خَمْسَ مَرَّاتٍ", "set": {"ar": "خَمْسَ مَرَّاتٍ، وَالأُولَى صَلَاةُ الفَجْرِ."}},
    {"u": "1-10-8", "cq": 5, "was": "How many prayers a day?", "set": {"a": "خَمْسُ صَلَوَاتٍ", "w": ["ثَلَاثُ صَلَوَاتٍ", "عَشْرُ صَلَوَاتٍ"]}},
    {"u": "1-10-8", "cq": 6, "was": "When is the first prayer?", "set": {"q": "Which is the first prayer of the day?", "a": "صَلَاةُ الفَجْرِ", "w": ["صَلَاةُ الظُّهْرِ", "صَلَاةُ العِشَاءِ"]}},

    {"u": "1-10-9", "r": 1, "was": "Young people", "set": {"body": B("""
        You met شَابٌّ (young man) and شَابَّةٌ (young woman) in Level 6. شَبَابٌ means "youth" or "young people", and it is also the plural of شَابٌّ, along with شُبَّانٌ.
    """)}},
    {"u": "1-10-9", "r": 1, "e": 3, "was": "الشَّبَابُ أَمَلُ المُسْتَقْبَلِ", "set": {"tr": "ash-shabābu amalu l-mustaqbali"}},
    {"u": "1-10-9", "r": 1, "e": 4, "was": "لَهُ حُلْمٌ كَبِيرٌ", "set": {"note": "لَهُ, literally \"for him\", means \"he has\". حُلْمٌ is a dream; the plural is أَحْلَامٌ."}},
    # لِـ + الشَّبَابِ drops the ا of اَلْ; both ل are written.
    {"u": "1-10-9", "r": 1, "e": 8, "was": "هَذَا المَرْكَزُ لِلشَّبَابِ", "set": {"tr": "hādhā l-markazu li-sh-shabābi", "note": "لِـ before اَلْ drops the ا of اَلْ: لِـ and الشَّبَابِ make لِلشَّبَابِ."}},
    {"u": "1-10-9", "r": 2, "was": "Dreams and hopes", "set": {"body": B("""
        أَحْلُمُ بِـ means "I dream of". أَتَمَنَّى أَنْ means "I hope to" or "I wish to", and the verb after أَنْ ends with ـَ.
        سَوْفَ, like سَـ, makes the future. Some say it points further ahead. The verb after it keeps its ـُ: سَوْفَ أُسَافِرُ.
    """)}},
    {"u": "1-10-9", "r": 2, "e": 3, "was": "سَوْفَ أُسَافِرُ", "set": {"note": "سَوْفَ, like سَـ, makes the future. The verb after it keeps its ـُ."}},
    {"u": "1-10-9", "r": 2, "e": 5, "was": "لَعَلَّكَ تَنْجَحُ", "set": {"note": "لَعَلَّ means \"perhaps\" or \"hopefully\". Like أَنَّ, it takes a pronoun ending: ـكَ means \"you\"."}},
    {"u": "1-10-9", "r": 2, "e": 6, "was": "أَنَا أُحِبُّ المُسْتَقْبَلَ", "set": {"ar": "المُسْتَقْبَلُ لِلشَّبَابِ", "tr": "al-mustaqbalu li-sh-shabābi", "en": "the future belongs to young people", "note": "لِـ here means \"belongs to\", as in لَهُ (he has)."}},

    {"u": "1-10-10", "r": 1, "was": "Advice", "set": {"body": B("""
        نَصِيحَةٌ is advice. يَنْبَغِي أَنْ means "one should". عَلَيْكَ أَنْ means "you should" or "you must" to a man, and عَلَيْكِ أَنْ is for a woman; you know عَلَيْكَ from يَجِبُ عَلَيْكَ.
        In both, the verb after أَنْ ends with ـَ, and verbs ending in ـِينَ or ـُونَ drop their ن.
    """)}},
    {"u": "1-10-10", "r": 1, "e": 2, "was": "عَلَيْكَ أَنْ تَنَامَ مُبَكِّرًا", "set": {"note": "مُبَكِّرًا means \"early\". It ends with ـًا, like other words that tell when or how."}},
    {"u": "1-10-10", "r": 1, "e": 3, "was": "عَلَيْكِ أَنْ تَشْكُرِي", "set": {"note": "وَالِدَانِ means \"parents\". شَكَرَ means \"he thanked\". After أَنْ, تَشْكُرِينَ drops its ن."}},
    # تَضِيعَ (to get lost) was used for "to waste"; the verb is تُضِيعَ.
    {"u": "1-10-10", "r": 1, "e": 4, "was": "لَا يَنْبَغِي أَنْ تَضِيعَ", "set": {"ar": "لَا يَنْبَغِي أَنْ تُضِيعَ الوَقْتَ", "tr": "lā yanbaghī an tuḍīʿa l-waqta", "note": "أَضَاعَ means \"he wasted\" (يُضِيعُ in the present). As a direct order, \"do not waste\" is لَا تُضِعِ الوَقْتَ: the long ي drops."}},
    {"u": "1-10-10", "r": 2, "was": "Volunteering", "set": {"body": B("""
        تَطَوَّعَ means "he volunteered" (يَتَطَوَّعُ, "he volunteers"), and a volunteer is مُتَطَوِّعٌ. سَاعَدَ means "he helped". Young people often volunteer to help others.
    """)}},
    {"u": "1-10-10", "r": 2, "e": 3, "was": "سَاعَدَ الشَّبَابُ الفُقَرَاءَ", "set": {"tr": "sāʿada sh-shabābu l-fuqarāʾa"}},
    # "Each other" is بَعْضُنَا بَعْضًا.
    {"u": "1-10-10", "r": 2, "e": 4, "was": "نُسَاعِدُ بَعْضَنَا", "set": {"ar": "يُسَاعِدُ بَعْضُنَا بَعْضًا", "tr": "yusāʿidu baʿḍunā baʿḍan", "note": "Literally \"some of us help others\". بَعْضٌ means \"some\"."}},
    {"u": "1-10-10", "q": 9, "was": "How do you say \"we help each other\"?", "set": {"a": "يُسَاعِدُ بَعْضُنَا بَعْضًا", "w": ["يُسَاعِدُ بَعْضَنَا بَعْضٌ", "سَاعَدْنَا بَعْضٌ"]}},
    {"u": "1-10-10", "l": 1, "was": "السَّلَامُ عَلَيْكُمْ. كَيْفَ حَالُكُمْ؟", "set": {"ar": "السَّلَامُ عَلَيْكُمْ. كَيْفَ حَالُكَ؟"}},
    {"u": "1-10-10", "cq": 1, "was": "What does the student dream of?", "set": {"a": "بِوَظِيفَةٍ جَيِّدَةٍ", "w": ["بِبَيْتٍ كَبِيرٍ", "بِسَيَّارَةٍ جَدِيدَةٍ"]}},

    {"u": "1-10-11", "r": 1, "e": 7, "was": "لَا تَرْمِ القُمَامَةَ", "set": {"note": "لَا with the \"you\" verb. تَرْمِي loses its long ي."}},
]
