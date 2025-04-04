GROUPS: list[str] = ["hiragana", "all", "hiragana_base", "base", "dakuon", "combo", "small_っ", "long_vowel"]

HIRAGANA_BASE: dict[str, str] = {
    "あ": "a",
    "い": "i",
    "う": "u",
    "え": "e",
    "お": "o",

    "か": "ka",
    "き": "ki",
    "く": "ku",
    "け": "ke",
    "こ": "ko",
    
    "さ": "sa",
    "し": "shi",
    "す": "su",
    "せ": "se",
    "そ": "so",
    
    "た": "ta",
    "ち": "chi",
    "つ": "tsu",
    "て": "te",
    "と": "to",
    
    "な": "na",
    "に": "ni",
    "ぬ": "nu",
    "ね": "ne",
    "の": "no",
    
    "は": "ha",
    "ひ": "hi",
    "ふ": "fu",
    "へ": "he",
    "ほ": "ho",
    
    "ま": "ma",
    "み": "mi",
    "む": "mu",
    "め": "me",
    "も": "mo",

    "や": "ya",
    "ゆ": "yu",
    "よ": "yo",

    "ら": "ra",
    "り": "ri",
    "る": "ru",
    "れ": "re",
    "ろ": "ro",

    "わ": "wa",

    "ん": "n"
}

DAKUON: dict[str, str] = {
    "が": "ga",
    "ぎ": "gi",
    "ぐ": "gu",
    "げ": "ge",
    "ご": "go",

    "ざ": "za",
    "じ": "ji",
    "ず": "zu",
    "ぜ": "ze",
    "ぞ": "zo",

    "だ": "da",
    "ぢ": "ji",
    "づ": "zu",
    "で": "de",
    "ど": "do",

    "ば": "ba",
    "び": "bi",
    "ぶ": "bu",
    "べ": "be",
    "ぼ": "bo",
    
    "ぱ": "pa",
    "ぴ": "pi",
    "ぷ": "pu",
    "ぺ": "pe",
    "ぽ": "po"
}

COMBO: dict[str, str] = {
    "きゃ": "kya",
    "きゅ": "kyu",
    "きょ": "kyo",
    
    "ぎゃ": "gya",
    "ぎゅ": "gyu",
    "ぎょ": "gyo",

    "しゃ": "sha",
    "しゅ": "shu",
    "しょ": "sho",

    "じゃ": "ja",
    "じゅ": "ju",
    "じょ": "jo",

    "ちゃ": "cha",
    "ちゅ": "chu",
    "ちょ": "cho",

    "ぢゃ": "nya",
    "ぢゅ": "nyu",
    "ぢょ": "nyo",

    "ひゃ": "hya",
    "ひゅ": "hyu",
    "ひょ": "hyo",

    "びゃ": "bya",
    "びゅ": "byu",
    "びょ": "byo",

    "ぴゃ": "pya",
    "ぴゅ": "pyu",
    "ぴょ": "pyo",

    "みゃ": "mya",
    "みゅ": "myu",
    "みょ": "myo",

    "りゃ": "rya",
    "りゅ": "ryu",
    "りょ": "ryo"
}

SMALL_っ: dict[str, str] = {
    "っ+k": "kk",
    "っ+s": "ss",
    "っ+t": "tt",
    "っ+p": "pp"
}

LONG_VOWEL: dict[str, str] = {
    "ああ": "aa",
    "いい": "ii",
    "うう": "uu",
    "ええ": "ee",
    "おお": "oo"
}

HIRAGANA: dict[str, str] = {
    **HIRAGANA_BASE,
    **DAKUON,
    **COMBO,
    **SMALL_っ,
    **LONG_VOWEL   
}