# Stage 1 · Level 3 — content corrections and improvements.
FIXES = [
    # Numbers 1–10: explain the patterns and teach the Arabic digits.
    {"u": "1-3-1", "r": 1, "was": "Numbers one to five", "set": {"body": B("""
        Start with the first five numbers. Say each one slowly.
        - وَاحِدٌ (one) and اِثْنَانِ (two) work like describing words: they come after the thing you count.
        - ثَلَاثَةٌ, أَرْبَعَةٌ and خَمْسَةٌ end with ـَةٌ when you count on your fingers.
        Arabic text often uses its own digits. Learn them with the words: ١ ٢ ٣ ٤ ٥.
    """)}},
    {"u": "1-3-1", "r": 1, "e": 1, "was": "وَاحِدٌ", "set": {"note": "Number 1, written ١."}},
    {"u": "1-3-1", "r": 1, "e": 2, "was": "اِثْنَانِ", "set": {"note": "Number 2, written ٢. Like اِسْمٌ, its first ا is only said at the start of a sentence."}},
    {"u": "1-3-1", "r": 1, "e": 3, "was": "ثَلَاثَةٌ", "set": {"note": "Number 3, written ٣. The letter ث sounds like \"th\" in \"think\"."}},
    {"u": "1-3-1", "r": 1, "e": 4, "was": "أَرْبَعَةٌ", "set": {"note": "Number 4, written ٤. It has the letter ع in the middle."}},
    {"u": "1-3-1", "r": 1, "e": 5, "was": "خَمْسَةٌ", "set": {"note": "Number 5, written ٥. It begins with خ, a rough sound like \"ch\" in the Scottish word \"loch\"."}},
    {"u": "1-3-1", "r": 2, "was": "Numbers six to ten", "set": {"body": B("""
        Now learn six to ten. Like three to five, they end with ـَةٌ when you count on your fingers.
        Their digits are ٦ ٧ ٨ ٩ ١٠. Digits are read from left to right, even inside Arabic text, so ١٠ is ten.
    """)}},
    {"u": "1-3-1", "r": 2, "e": 1, "was": "سِتَّةٌ", "set": {"note": "Number 6, written ٦. The ت is doubled."}},
    {"u": "1-3-1", "r": 2, "e": 2, "was": "سَبْعَةٌ", "set": {"note": "Number 7, written ٧. It has the letter ع in the middle."}},
    {"u": "1-3-1", "r": 2, "e": 3, "was": "ثَمَانِيَةٌ", "set": {"note": "Number 8, written ٨. It has a long ا in the middle: tha-maa-ni-ya-tun."}},
    {"u": "1-3-1", "r": 2, "e": 4, "was": "تِسْعَةٌ", "set": {"note": "Number 9, written ٩. It begins with ت."}},
    {"u": "1-3-1", "r": 2, "e": 5, "was": "عَشَرَةٌ", "set": {"note": "Number 10, written ١٠. It begins with the letter ع."}},

    # The tens: the old text ended with a sentence that made no sense; complete the set 20–90.
    {"u": "1-3-2", "r": 1, "was": "The tens", "set": {"body": B("""
        The tens from 20 to 90 end with ـُونَ, the same ending as plural jobs like مُدَرِّسُونَ.
        - Most tens come from the single numbers: ثَلَاثَةٌ (3) gives ثَلَاثُونَ (30), and أَرْبَعَةٌ (4) gives أَرْبَعُونَ (40).
        - Twenty is the one to watch: عِشْرُونَ comes from عَشَرَةٌ (10).
        - One hundred is مِئَةٌ.
    """)}},
    {"u": "1-3-2", "r": 1, "e": 1, "was": "عِشْرُونَ", "set": {"note": "Number 20, written ٢٠. It comes from عَشَرَةٌ, not from اِثْنَانِ."}},
    {"u": "1-3-2", "r": 1, "e": 2, "was": "ثَلَاثُونَ", "set": {"note": "Number 30, written ٣٠. It comes from ثَلَاثَةٌ, with ـُونَ added."}},
    {"u": "1-3-2", "r": 1, "e": 3, "was": "أَرْبَعُونَ", "set": {"note": "Number 40, written ٤٠. It comes from أَرْبَعَةٌ."}},
    {"u": "1-3-2", "r": 1, "e": 4, "was": "خَمْسُونَ", "set": {"note": "Number 50, written ٥٠. It comes from خَمْسَةٌ."}},
    # keep the tens in order: 60 replaces 100 in fifth place, and 100 moves to the end
    {"u": "1-3-2", "r": 1, "e": 5, "was": "مِئَةٌ", "set": {"ar": "سِتُّونَ", "tr": "sittūna", "en": "sixty", "note": "Number 60, written ٦٠. It comes from سِتَّةٌ."}},
    {"u": "1-3-2", "r": 1, "add": {"ar": "سَبْعُونَ", "tr": "sabʿūna", "en": "seventy", "note": "Number 70, written ٧٠. It comes from سَبْعَةٌ."}},
    {"u": "1-3-2", "r": 1, "add": {"ar": "ثَمَانُونَ", "tr": "thamānūna", "en": "eighty", "note": "Number 80, written ٨٠. It comes from ثَمَانِيَةٌ."}},
    {"u": "1-3-2", "r": 1, "add": {"ar": "تِسْعُونَ", "tr": "tisʿūna", "en": "ninety", "note": "Number 90, written ٩٠. It comes from تِسْعَةٌ."}},
    {"u": "1-3-2", "r": 1, "add": {"ar": "مِئَةٌ", "tr": "miʾatun", "en": "one hundred", "note": "Number 100, written ١٠٠. Many books spell it مِائَةٌ, with an ا that is not pronounced."}},
    {"u": "1-3-2", "w": 0, "add": {"ar": "سِتُّونَ", "pl": "", "en": "sixty", "type": "number"}},
    {"u": "1-3-2", "w": 0, "add": {"ar": "سَبْعُونَ", "pl": "", "en": "seventy", "type": "number"}},
    {"u": "1-3-2", "w": 0, "add": {"ar": "ثَمَانُونَ", "pl": "", "en": "eighty", "type": "number"}},
    {"u": "1-3-2", "w": 0, "add": {"ar": "تِسْعُونَ", "pl": "", "en": "ninety", "type": "number"}},
    # كَمْ: tanween fatha on a word ending in ة has no extra ا.
    {"u": "1-3-2", "r": 2, "was": "How many?", "set": {"body": B("""
        Use كَمْ to ask about a number. After كَمْ, the thing you count is singular and takes tanween fatha (ـً): كِتَابًا. On a word that ends in ة, the mark sits on the ة with no extra ا: سَيَّارَةً.
        Answer with a number and the thing.
    """)}},
    {"u": "1-3-2", "r": 2, "e": 1, "was": "كَمْ كِتَابًا عِنْدَكَ؟", "set": {"note": "كِتَابًا ends with ـًا after كَمْ."}},

    # Ages: 3–10 take the plural سَنَوَاتٍ.
    {"u": "1-3-3", "r": 2, "was": "How old are you?", "set": {"body": B("""
        عُمْرٌ means "age". Ask a man كَمْ عُمْرُكَ؟ and ask a woman كَمْ عُمْرُكِ؟ Answer with عُمْرِي ("my age"), the number and the word for year.
        - From 11 upwards, use the singular with tanween fatha: عُمْرِي عِشْرُونَ سَنَةً.
        - From 3 to 10, use the plural سَنَوَاتٍ. سَنَةٌ is feminine, so the number drops ـَةٌ: عُمْرِي عَشْرُ سَنَوَاتٍ.
    """)}},
    {"u": "1-3-3", "r": 2, "add": {"ar": "عُمْرُهُ سَبْعُ سَنَوَاتٍ", "tr": "ʿumruhu sabʿu sanawātin", "en": "he is seven years old", "note": "From 3 to 10 the word for years is the plural سَنَوَاتٍ, and the number has no ـَةٌ because سَنَةٌ is feminine."}},

    # Old for people.
    {"u": "1-3-5", "r": 1, "e": 6, "was": "كِتَابٌ قَدِيمٌ", "set": {"note": "قَدِيمٌ means \"old\" for things, not for people. For an old person, say كَبِيرٌ فِي السِّنِّ, \"big in age\"."}},

    # Prices are asked with بِكَمْ.
    {"u": "1-3-6", "r": 2, "was": "In the shop", "set": {"body": B("""
        Use أُرِيدُ to say "I want". The thing you want ends with tanween fatha: أُرِيدُ حَقِيبَةً.
        A seller is بَائِعٌ, and the money in Saudi Arabia is the رِيَالٌ. Ask the price with بِكَمْ هُوَ؟ for a masculine thing and بِكَمْ هِيَ؟ for a feminine thing.
        After a number from three to ten, the thing is plural, so رِيَالٌ becomes رِيَالَاتٌ.
    """)}},
    {"u": "1-3-6", "r": 2, "e": 3, "was": "كَمْ هُوَ؟", "set": {"ar": "بِكَمْ هُوَ؟", "tr": "bikam huwa", "en": "how much is it? (masculine)", "note": "بِكَمْ asks for a price. Use هُوَ for a book, a pen or a house."}},
    {"u": "1-3-6", "r": 2, "e": 5, "was": "كَمْ هِيَ؟", "set": {"ar": "بِكَمْ هِيَ؟", "tr": "bikam hiya", "en": "how much is it? (feminine)", "note": "Use هِيَ for a bag, a car or a rose."}},
    {"u": "1-3-6", "q": 4, "was": "How do you ask \"How much is it?\" about a bag?", "set": {"a": "بِكَمْ هِيَ؟", "w": ["بِكَمْ هُوَ؟", "كَمْ عُمْرُهَا؟"]}},
    {"u": "1-3-6", "l": 9, "was": "الحَقِيبَةُ الحَمْرَاءُ جَمِيلَةٌ. كَمْ هِيَ؟", "set": {"ar": "الحَقِيبَةُ الحَمْرَاءُ جَمِيلَةٌ. بِكَمْ هِيَ؟"}},

    # Rakʿahs: tanween on ة words, and Maghrib is the only three-rakʿah prayer.
    {"u": "1-3-7", "r": 2, "was": "How many rakʿahs?", "set": {"body": B("""
        رَكْعَةٌ is one unit of the prayer, and its plural is رَكَعَاتٌ. Ask كَمْ رَكْعَةً؟ After كَمْ the word takes tanween fatha, and because رَكْعَةٌ ends in ة the mark sits on the ة: رَكْعَةً.
        - For two, use the dual: رَكْعَتَانِ.
        - For three to ten, use the plural. رَكْعَةٌ is feminine, so the number drops ـَةٌ: أَرْبَعُ رَكَعَاتٍ.
    """)}},
    {"u": "1-3-7", "r": 2, "e": 1, "was": "كَمْ رَكْعَةً فِي صَلَاةِ الفَجْرِ؟", "set": {"note": "After كَمْ, رَكْعَةٌ becomes رَكْعَةً."}},
    {"u": "1-3-7", "r": 2, "e": 5, "was": "كَمْ رَكْعَةً فِي صَلَاةِ المَغْرِبِ؟", "set": {"note": "The sunset prayer is the only prayer with three rakʿahs."}},
    {"u": "1-3-7", "r": 2, "e": 8, "was": "كَمْ صَلَاةً؟", "set": {"note": "After كَمْ, صَلَاةٌ becomes صَلَاةً."}},

    # Two definite nouns need هِيَ to make a sentence; Makkah is a diptote.
    {"u": "1-3-8", "r": 2, "e": 5, "was": "القِبْلَةُ الكَعْبَةُ", "set": {"ar": "القِبْلَةُ هِيَ الكَعْبَةُ", "tr": "al-qiblatu hiya l-kaʿbatu", "note": "Both words have اَلْ, so we put هِيَ between them to make a sentence, as in هَذِهِ هِيَ المَكْتَبَةُ."}},
    {"u": "1-3-8", "r": 2, "e": 7, "was": "الكَعْبَةُ فِي مَكَّةَ", "set": {"note": "مَكَّةُ is a name that never takes tanween, so after فِي it ends with ـَ instead of ـِ."}},

    # Phrases around the prayer: the explanation was a single line.
    {"u": "1-3-9", "r": 2, "was": "Phrases around the prayer", "set": {"body": B("""
        Muslims say these phrases every day, in and around the prayer. Learn each one as a whole phrase.
        - Two belong to the prayer itself: اللَّهُ أَكْبَرُ opens it, and السَّلَامُ عَلَيْكُمْ وَرَحْمَةُ اللَّهِ closes it.
        - Others are said to people: تَقَبَّلَ اللَّهُ after someone prays, and جَزَاكَ اللَّهُ خَيْرًا to thank someone.
    """)}},
]
