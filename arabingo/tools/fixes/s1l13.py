# Stage 1 · Level 13 (was Stage 2 · Level 4) — content corrections and improvements.
FIXES = [
    {"u": "1-13-1", "r": 1, "was": "Words of Ramadan", "set": {"body": B("""
        شَهْرٌ is a month (plural شُهُورٌ). رَمَضَانُ is the ninth month of the Islamic year, the month of fasting. صِيَامٌ and صَوْمٌ both mean fasting, and a person who fasts is صَائِمٌ.
        The fast starts at dawn (الفَجْرُ) and ends at sunset (المَغْرِبُ).
    """)}},
    {"u": "1-13-1", "r": 1, "e": 1, "was": "رَمَضَانُ شَهْرُ الصِّيَامِ", "set": {"note": "شَهْرُ الصِّيَامِ is an إِضَافَةٌ. رَمَضَانُ never takes tanween."}},
    {"u": "1-13-1", "r": 1, "e": 4, "was": "هَذَا إِفْطَارٌ", "set": {"tr": "hādhā ifṭārun"}},
    {"u": "1-13-1", "r": 2, "e": 6, "was": "بَعْدَ أَنْ نُصَلِّيَ", "set": {"ar": "نَقْرَأُ القُرْآنَ بَعْدَ أَنْ نُصَلِّيَ", "tr": "naqraʾu l-qurʾāna baʿda an nuṣalliya", "en": "we read the Quran after we pray", "note": "For a regular action, بَعْدَ أَنْ takes a present verb ending in ـَ: نُصَلِّي becomes نُصَلِّيَ.", "re": None}},

    # Sins spoil the reward of the fast but do not break it; eating by mistake does not break it either.
    {"u": "1-13-2", "r": 1, "was": "Allowed and not allowed", "set": {"body": B("""
        يَجُوزُ means "it is allowed" and لَا يَجُوزُ means "it is not allowed".
        - Eating and drinking on purpose in the daytime break the fast. If you eat because you forgot, the fast is still valid.
        - A person who is ill or travelling may break the fast and make up the days later. Making up a missed fast is called قَضَاءٌ.
        - Bad words and deeds do not break the fast, but they spoil its reward.
    """)}},
    {"u": "1-13-2", "r": 2, "was": "Blessed nights and deeds", "set": {"body": B("""
        لَيْلَةُ القَدْرِ is the Night of Power. The Quran says it is better than a thousand months. It is sought in the last ten nights of Ramadan, the best nights of the year.
        اِعْتِكَافٌ is staying in the mosque for worship, often in those last ten nights. In Ramadan Muslims also give more charity and read more Quran.
    """)}},
    {"u": "1-13-2", "r": 2, "e": 1, "was": "لَيْلَةُ القَدْرِ خَيْرٌ", "set": {"note": "These are words of the Quran (97:3). خَيْرٌ مِنْ means \"better than\"."}},
    {"u": "1-13-2", "r": 2, "e": 5, "was": "يَدْعُو الصَّائِمُ عِنْدَ الإِفْطَارِ", "set": {"tr": "yadʿū ṣ-ṣāʾimu ʿinda l-ifṭāri"}},
    {"u": "1-13-2", "w": 4, "was": "اعْتِكَافٌ", "set": {"ar": "اِعْتِكَافٌ"}},

    # Zakat has a minimum amount and is usually 2.5%; its recipients are named in the Quran (9:60).
    {"u": "1-13-3", "r": 1, "was": "Who gives and who receives", "set": {"body": B("""
        Zakat is a duty on a Muslim whose savings reach a set minimum and stay with him for a full year. It is usually 2.5% of those savings.
        The Quran names who receives it, starting with the poor (فَقِيرٌ) and the needy (مِسْكِينٌ). Other words for people in need are يَتِيمٌ (orphan), أَرْمَلَةٌ (widow) and مُحْتَاجٌ (someone in need).
    """)}},
    {"u": "1-13-3", "r": 2, "was": "Verbs of giving", "set": {"body": B("""
        أَعْطَى means "he gave", and أَنْفَقَ means "he spent", often on good causes. تَصَدَّقَ بِـ means "he gave in charity". أَخْرَجَ, literally "he took out", is used for paying zakat. جَمَعَ means "he gathered" and وَزَّعَ means "he distributed".
        Their present forms are يُعْطِي, يُنْفِقُ, يَتَصَدَّقُ, يُخْرِجُ, يَجْمَعُ and يُوَزِّعُ.
    """)}},

    {"u": "1-13-4", "r": 1, "was": "Whoever and whatever", "set": {"body": B("""
        مَنْ can mean "whoever" and مَا can mean "whatever". Use them to make general rules: مَنْ يَتَصَدَّقْ يَأْخُذْ أَجْرًا (whoever gives in charity gets a reward).
        Both verbs end with a sukoon. A verb that ends in a long vowel loses it: يُعْطِي becomes يُعْطِ, as in مَنْ يُعْطِ يَأْخُذْ.
    """)}},
    {"u": "1-13-4", "r": 1, "e": 5, "was": "خَيْرُ النَّاسِ أَنْفَعُهُمْ لِلنَّاسِ", "set": {"note": "This is reported as a saying of the Prophet ﷺ. أَنْفَعُهُمْ means \"the most useful of them\"."}},
    # The hadith in Sahih Muslim names the three deeds that go on after death.
    {"u": "1-13-4", "r": 2, "was": "Ongoing charity", "set": {"body": B("""
        صَدَقَةٌ جَارِيَةٌ is "ongoing charity", a good deed whose reward continues after a person dies, like building a well or a mosque. جَارِيَةٌ means "flowing", and وَقْفٌ is an endowment.
        The Prophet ﷺ said that when a person dies, his deeds stop except three: ongoing charity, knowledge that benefits people, and a righteous child who prays for him.
    """)}},
    {"u": "1-13-4", "l": 4, "was": "لِلفُقَرَاءِ وَالمَسَاكِينِ", "set": {"ar": "لِلفُقَرَاءِ وَالمَسَاكِينِ، كَمَا قَالَ اللَّهُ فِي القُرْآنِ."}},

    {"u": "1-13-5", "r": 1, "was": "Words of repentance", "set": {"body": B("""
        تَوْبَةٌ is repentance, and تَابَ إِلَى means "he repented to", literally "he turned back to". ذَنْبٌ is a sin (plural ذُنُوبٌ). مَغْفِرَةٌ is forgiveness, and غَفَرَ means "he forgave".
        Three names of Allah: غَفُورٌ (Forgiving), رَحِيمٌ (Merciful) and تَوَّابٌ (always accepting repentance).
    """)}},
    {"u": "1-13-5", "r": 1, "e": 3, "was": "اللَّهُ غَفُورٌ رَحِيمٌ", "set": {"note": "Two of the names of Allah. غَفُورٌ means \"very forgiving\", more than غَافِرٌ."}},
    {"u": "1-13-5", "r": 1, "e": 4, "was": "اللَّهُ تَوَّابٌ", "set": {"note": "The pattern فَعَّالٌ, with a doubled middle letter, means \"very much\": تَوَّابٌ is \"always accepting repentance\"."}},
    {"u": "1-13-5", "r": 2, "e": 5, "was": "يَجِبُ أَنْ نَرُدَّ الحُقُوقَ", "set": {"tr": "yajibu an narudda l-ḥuqūqa"}},

    {"u": "1-13-6", "r": 1, "was": "Asking forgiveness", "set": {"body": B("""
        The pattern اِسْتَفْعَلَ often means "to ask for": اِسْتَغْفَرَ means "he asked for forgiveness". The command is اِسْتَغْفِرْ, and أَسْتَغْفِرُ اللَّهَ means "I ask Allah for forgiveness".
        قَدْ before a past verb means "already" or "indeed": قَدْ تُبْتُ (I have repented). لَقَدْ is stronger.
    """)}},
    {"u": "1-13-6", "r": 1, "e": 5, "was": "إِنْ تَتُبْ يَتُبِ اللَّهُ", "set": {"note": "Both verbs end with a sukoon after إِنْ, and تَتُوبُ loses its long و: تَتُبْ. Before اَلْ the sukoon becomes ـِ: يَتُبِ اللَّهُ."}},
    {"u": "1-13-6", "r": 1, "e": 7, "was": "رَبَّنَا اغْفِرْ لَنَا", "set": {"tr": "rabbanā ghfir lanā"}},
    # اعتذر إليه is the classical form, so it cannot be a wrong answer.
    {"u": "1-13-6", "q": 10, "was": "How do you say \"I apologise to you\" to a man?", "set": {"w": ["أَعْتَذِرُ بِكَ", "اِعْتَذَرْتُ مِنْكِ"]}},

    {"u": "1-13-7", "r": 1, "e": 1, "was": "الدُّعَاءُ عِبَادَةٌ", "set": {"note": "The Prophet ﷺ said: الدُّعَاءُ هُوَ العِبَادَةُ, \"dua is worship itself\". عِبَادَةٌ means \"worship\"."}},
    {"u": "1-13-7", "r": 1, "e": 4, "was": "اللَّهُمَّ اغْفِرْ لِي", "set": {"note": "اللَّهُمَّ means \"O Allah\". The مَّ at the end takes the place of يَا."}},
    {"u": "1-13-7", "r": 2, "was": "Etiquette of dua", "set": {"body": B("""
        Some times are best for dua: the last third of the night, between the adhan and the iqama, while prostrating (السُّجُودُ), and on Friday.
        Begin by praising Allah and sending blessings on the Prophet ﷺ. Face the qibla, be sure that Allah hears you, and do not rush.
    """)}},
    {"u": "1-13-7", "r": 2, "e": 3, "was": "أَقْرَبُ مَا يَكُونُ العَبْدُ", "set": {"note": "A hadith in Sahih Muslim. عَبْدٌ is a servant, and سَاجِدٌ means \"prostrating\"."}},

    {"u": "1-13-8", "r": 1, "e": 1, "was": "الحَمْدُ لِلَّهِ الَّذِي أَحْيَانَا", "set": {"note": "The first words of the dua on waking up. أَحْيَا means \"he gave life\", and الَّذِي means \"who\"."}},
    {"u": "1-13-8", "r": 1, "e": 3, "was": "الحَمْدُ لِلَّهِ الَّذِي أَطْعَمَنِي", "set": {"note": "The first words of the dua after eating. أَطْعَمَ means \"he fed\", and ـنِي means \"me\"."}},
    {"u": "1-13-8", "r": 2, "e": 1, "was": "رَبَّنَا آتِنَا فِي الدُّنْيَا", "set": {"note": "From the Quran (2:201). آتَى means \"he gave\", دُنْيَا is this world, and حَسَنَةٌ is something good."}},
    {"u": "1-13-8", "r": 2, "e": 4, "was": "رَبِّ زِدْنِي عِلْمًا", "set": {"note": "From the Quran (20:114). زَادَ is \"he increased\"; the command is زِدْ, and ـنِي is \"me\"."}},
    {"u": "1-13-8", "r": 2, "e": 5, "was": "رَبِّ اشْرَحْ لِي صَدْرِي", "set": {"note": "The dua of Musa in the Quran (20:25). شَرَحَ means \"he expanded\" or \"he explained\"."}},
    # The reply repeated the example above it.
    {"u": "1-13-8", "r": 2, "e": 6, "was": "رَبِّ زِدْنِي عِلْمًا", "set": {"ar": "رَبَّنَا تَقَبَّلْ مِنَّا", "tr": "rabbanā taqabbal minnā", "en": "our Lord, accept from us", "note": "Ibrahim and Ismail made this dua as they built the Kaʿbah (Quran 2:127). تَقَبَّلْ is the command of تَقَبَّلَ.", "re": None}},
]
