# Stage 1 · Level 2 — content corrections and improvements.
FIXES = [
    # Feminine words without ـة were introduced in Level 1.
    {"u": "1-2-2", "r": 1, "was": "Feminine things", "set": {"body": B("""
        Most feminine words end with ـَةٌ. Point at them with هَذِهِ (this) and تِلْكَ (that). A few feminine words do not end with ـَةٌ, like أُمٌّ (mother) and شَمْسٌ (sun), so learn whether a word is masculine or feminine when you learn the word.
    """)}},

    # "my/your" endings: the ending is ـكَ / ـكِ; the noun keeps its own vowel before it.
    {"u": "1-2-3", "r": 2, "was": "My and your", "set": {"body": B("""
        You already met these endings in "what is your name?". Add them to the end of a noun.
        - ـِي means "my": كِتَابِي (my book).
        - ـكَ means "your" when you talk to a man: كِتَابُكَ.
        - ـكِ means "your" when you talk to a woman: كِتَابُكِ.
        Before ـكَ and ـكِ the noun keeps its own vowel, usually ـُ. When a word ends with ـَةٌ, the ة becomes ت before the ending: حَقِيبَةٌ becomes حَقِيبَتِي.
    """)}},

    # School subjects: name the construction, fix a transliteration and a malformed distractor.
    {"u": "1-2-4", "r": 2, "was": "School subjects", "set": {"body": B("""
        دِرَاسَةٌ means "study". مَادَّةٌ means "a school subject", and its plural is مَوَادُّ.
        To say "the book of Arabic", put two nouns side by side. This is called إِضَافَةٌ.
        - The first noun has no tanween and no اَلْ: كِتَابُ.
        - The second noun ends with ـِ: العَرَبِيَّةِ.
        So كِتَابُ العَرَبِيَّةِ means "the Arabic book", literally "the book of Arabic".
    """)}},
    {"u": "1-2-4", "r": 2, "e": 7, "was": "كِتَابُ الإِنْجِلِيزِيَّةِ", "set": {"tr": "kitābu l-injilīziyyati"}},
    {"u": "1-2-4", "q": 1, "was": "How do you ask \"Where is the book?\"", "set": {"w": ["مَتَى الكِتَابُ؟", "مَا الكِتَابُ؟"]}},

    # More relatives: add the two aunts, which the topic was missing.
    {"u": "1-2-6", "r": 1, "was": "More relatives", "set": {"body": B("""
        Arabic has two words for "uncle" and two for "aunt", depending on which side of the family they are on.
        - عَمٌّ is your father's brother, and عَمَّةٌ is your father's sister.
        - خَالٌ is your mother's brother, and خَالَةٌ is your mother's sister.
        - زَوْجٌ is a husband, and زَوْجَةٌ is a wife.
        Add ـِي to each word to say "my": عَمِّي, خَالَتِي, زَوْجَتِي.
    """)}},
    {"u": "1-2-6", "r": 1, "add": {"ar": "هَذِهِ عَمَّتِي", "tr": "hādhihi ʿammatī", "en": "this is my paternal aunt", "note": "عَمَّةٌ is your father's sister. The ة becomes ت before ـِي. Its plural is عَمَّاتٌ."}},
    {"u": "1-2-6", "r": 1, "add": {"ar": "هَذِهِ خَالَتِي", "tr": "hādhihi khālatī", "en": "this is my maternal aunt", "note": "خَالَةٌ is your mother's sister. Its plural is خَالَاتٌ."}},
    {"u": "1-2-6", "w": 0, "add": {"ar": "عَمَّةٌ", "pl": "عَمَّاتٌ", "en": "paternal aunt", "type": "noun"}},
    {"u": "1-2-6", "w": 0, "add": {"ar": "خَالَةٌ", "pl": "خَالَاتٌ", "en": "maternal aunt", "type": "noun"}},

    {"u": "1-2-7", "r": 1, "e": 9, "was": "مَا شَاءَ اللَّهُ", "set": {"en": "what Allah has willed! (said to admire something)"}},

    # More jobs: the explanation was a single line.
    {"u": "1-2-9", "r": 1, "was": "More jobs", "set": {"body": B("""
        Here are more jobs. They follow the same rule: add ـَةٌ for a woman.
        Many job words share a pattern. Words with a doubled middle letter, like طَبَّاخٌ (cook, from طَبَخَ "he cooked"), often name someone who does an action as their work. Words that start with مُـ, like مُوَظَّفٌ (employee) and مُدَرِّسٌ (teacher), are also very common for jobs.
    """)}},
    {"u": "1-2-9", "r": 1, "e": 5, "was": "هِيَ طَالِبَةٌ", "set": {"note": "طَالِبٌ and طَالِبَةٌ were in Level 1. A student is not a job, but you will use the word all the time."}},
    {"u": "1-2-9", "r": 2, "was": "Where people work", "set": {"body": B("""
        مَكَانٌ means "place", so مَكَانُ العَمَلِ is "the place of work". To say where a person is, use فِي ("in"). The word after فِي ends with a كَسْرَةٌ, and because it has اَلْ it takes a single ـِ with no tanween: المَدْرَسَةُ becomes فِي المَدْرَسَةِ.
    """)}},
    {"u": "1-2-9", "r": 2, "e": 4, "was": "المُوَظَّفُ فِي المَكْتَبِ", "set": {"note": "You learned مَكْتَبٌ with the classroom words. Here it means \"office\"."}},
    {"u": "1-2-9", "r": 2, "e": 8, "was": "مَا مَكَانُ العَمَلِ؟", "set": {"en": "what is the place of work?", "note": "Use it to ask where someone works."}},

    # Nationalities: what happens to ال and a final ا.
    {"u": "1-2-10", "r": 1, "was": "Nationalities", "set": {"body": B("""
        جِنْسِيَّةٌ means "nationality". To make a nationality word from a country, add ـِيٌّ for a man and ـِيَّةٌ for a woman. The doubled ي is part of the ending.
        - If the country has اَلْ, drop it: الأُرْدُنُّ (Jordan) gives أُرْدُنِّيٌّ.
        - If the country ends in ا, drop the ا: أَمْرِيكَا gives أَمْرِيكِيٌّ.
        Ask مَا جِنْسِيَّتُكَ؟ for "what is your nationality?"
    """)}},
]
