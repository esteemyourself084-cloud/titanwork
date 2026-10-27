# Stage 1 · Level 1 — content corrections and improvements.
FIXES = [
    # Arabic at a glance: most (not all) letters join; explain tanween, which every transliteration uses.
    {"u": "1-1-1", "r": 1, "was": "Arabic at a glance", "set": {"body": B("""
        Arabic is written and read from right to left. It has 28 letters. Most letters join to the next letter inside a word, so a letter can look a little different at the start, middle or end of a word. There are no capital letters.
        Short vowels are not letters. They are small marks written above or below a letter, called الحَرَكَاتُ (the vowel marks). They tell you how to say the word. Here are the three main ones.
        - فَتْحَةٌ (fatḥa) is a small line above the letter. It gives the sound "a".
        - ضَمَّةٌ (ḍamma) is a small و above the letter. It gives the sound "u".
        - كَسْرَةٌ (kasra) is a small line below the letter. It gives the sound "i".
        When the mark is doubled at the end of a word, it adds an "n" sound: ـٌ is read "un", ـٍ is "in" and ـً is "an". This is called تَنْوِينٌ, and it means "a" or "an" in English: كِتَابٌ is "a book".
    """)}},
    {"u": "1-1-1", "r": 1, "e": 2, "was": "كُتُبٌ", "set": {"note": "The same three letters with different vowel marks. The ضَمَّةٌ gives the sound \"u\", and the double ضَمَّةٌ at the end adds \"-un\", so it is read \"ku-tu-bun\". It means many books."}},

    # The verb: show how to talk about the future.
    {"u": "1-1-2", "r": 1, "was": "The verb and its three tenses", "set": {"body": B("""
        A فِعْلٌ has three tenses. The tense shows when the action happens.
        - الفِعْلُ المَاضِي (the past) is for what already happened.
        - الفِعْلُ المُضَارِعُ (the present) is for what is happening now or happens regularly. Put سَـ in front of it to talk about the future: سَيَكْتُبُ means "he will write".
        - فِعْلُ الأَمْرِ (the command) is for telling someone to do something.
        Look at the same verb in all three tenses. The three root letters stay, and the vowel marks and extra letters change.
    """)}},
    # The noun: not every plural changes shape — many just add an ending.
    {"u": "1-1-2", "r": 2, "was": "The noun and its number", "set": {"body": B("""
        An اِسْمٌ can be in three numbers. English has only two, but Arabic has a special form for exactly two things.
        - مُفْرَدٌ (singular) means one.
        - مُثَنَّى (dual) means exactly two. Add ـَانِ to the end: كِتَابٌ becomes كِتَابَانِ.
        - جَمْعٌ (plural) means three or more. Some plurals only add an ending, like مُعَلِّمُونَ (teachers). Many others change the whole shape of the word, like كُتُبٌ (books), so learn each plural together with its singular.
    """)}},

    # Masculine, feminine and "the": feminine words without ـة, the dropped tanween, and silent lam.
    {"u": "1-1-4", "r": 2, "was": "Masculine, feminine", "set": {"body": B("""
        Every اِسْمٌ is either masculine (مُذَكَّرٌ) or feminine (مُؤَنَّثٌ). Most feminine words end in ـَةٌ, a round letter called تَاءٌ مَرْبُوطَةٌ. A few feminine words have no ending at all, like أُمٌّ (mother) and شَمْسٌ (sun).
        To say "the", put اَلْ at the start of the word. The double ending then becomes a single mark: كِتَابٌ (a book) becomes الكِتَابُ (the book).
        With some letters, such as ش, س, ت and ط, the ل of اَلْ is not pronounced. The next letter is said twice instead and carries a شَدَّةٌ (ـّ). So الشَّمْسُ is read "ash-shamsu", not "al-shamsu".
    """)}},
    {"u": "1-1-4", "r": 2, "e": 5, "was": "الكِتَابُ", "set": {"note": "Put اَلْ at the start to say \"the\": a book becomes the book. The double ending ـٌ becomes a single ـُ."}},
    {"u": "1-1-4", "r": 2, "add": {"ar": "الشَّمْسُ", "tr": "ash-shamsu", "en": "the sun", "note": "The ل is silent and the ش is doubled, so you say \"ash-shamsu\". شَمْسٌ is also one of the feminine words without ـَةٌ."}},
    {"u": "1-1-4", "r": 2, "add": {"ar": "الطَّالِبَةُ", "tr": "aṭ-ṭālibatu", "en": "the (female) student", "note": "Feminine with ـَةُ, and the ل is silent again: \"aṭ-ṭālibatu\"."}},

    # أَرَادَ is taught with أُرِيدُ in "Handy phrases", not in "How are you?".
    {"u": "1-1-6", "w": 4, "del": True, "was": "أَرَادَ"},
    {"u": "1-1-8", "w": 0, "add": {"ar": "أَرَادَ", "pl": "", "en": "to want", "type": "verb"}},

    # Prices are asked with بِكَمْ, as in the Shopping lessons.
    {"u": "1-1-8", "r": 2, "e": 5, "was": "كَمْ هَذَا؟", "set": {"ar": "بِكَمْ هَذَا؟", "tr": "bikam hādhā", "en": "how much is this?", "note": "بِكَمْ asks for a price, literally \"for how much?\". Use it in a shop."}},
    {"u": "1-1-8", "q": 6, "was": "How do you ask \"How much is this?\"", "set": {"q": "How do you ask the price: \"How much is this?\"", "a": "بِكَمْ هَذَا؟", "w": ["مَا هَذَا؟", "مَنْ هَذَا؟"]}},

    # Conversation questions that offered only one wrong answer.
    {"u": "1-1-8", "cq": 3, "was": "Who is the teacher?", "set": {"w": ["مَرْيَمُ", "خَالِدٌ"]}},
    {"u": "1-1-8", "cq": 4, "was": "Who is the student?", "set": {"w": ["أَحْمَدُ", "سَارَةُ"]}},
    {"u": "1-1-8", "cq": 5, "was": "Where is Maryam from?", "set": {"w": ["مِنْ مِصْرَ", "مِنْ مَكَّةَ"]}},
    {"u": "1-1-8", "cq": 6, "was": "Where is Ahmad from?", "set": {"w": ["مِنْ لُبْنَانَ", "مِنْ مَكَّةَ"]}},
]
