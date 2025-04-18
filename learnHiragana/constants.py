GROUPS: list[str] = [
    "hiragana", 
    "all", 
    "hiragana_base", 
    "base", 
    "dakuon", 
    "combo", 
    "small_っ", 
    "long_vowel", 
    "katakana", 
    "katakana_base", 
    "katakana_dakuon", 
    "katakana_combo", 
    "small_ッ"
]

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

    "ぢゃ": "ja",
    "ぢゅ": "ju",
    "ぢょ": "jo",

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
    "っか": "kka",
    "っさ": "ssa",
    "った": "tta",
    "っぱ": "ppa"
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

KATAKANA_BASE: dict[str, str] = {
    "ア": "a",
    "イ": "i",
    "ウ": "u",
    "エ": "e",
    "オ": "o",

    "カ": "ka",
    "キ": "ki",
    "ク": "ku",
    "ケ": "ke",
    "コ": "ko",
    
    "サ": "sa",
    "シ": "shi",
    "ス": "su",
    "セ": "se",
    "ソ": "so",
    
    "タ": "ta",
    "チ": "chi",
    "ツ": "tsu",
    "テ": "te",
    "ト": "to",

    "ナ": "na",
    "ニ": "ni",
    "ヌ": "nu",
    "ネ": "ne",
    "ノ": "no",

    "ハ": "ha",
    "ヒ": "hi",
    "フ": "fu",
    "ヘ": "he",
    "ホ": "ho",

    "マ": "ma",
    "ミ": "mi",
    "ム": "mu",
    "メ": "me",
    "モ": "mo",
    
    "ヤ": "ya",
    "ユ": "yu",
    "ヨ": "yo",

    "ラ": "ra",
    "リ": "ri",
    "ル": "ru",
    "レ": "re",
    "ロ": "ro",

    "ワ": "wa",
    "ヲ": "wo",

    "ン": "n"
}

KATAKANA_DAKUON: dict[str, str] = {
    "ガ": "ga",
    "ギ": "gi",
    "グ": "gu",
    "ゲ": "ge",
    "ゴ": "go",

    "ザ": "za",
    "ジ": "ji",
    "ズ": "zu",
    "ゼ": "ze",
    "ゾ": "zo",

    "ダ": "da",
    "ヂ": "ji",
    "ヅ": "zu",
    "デ": "de",
    "ド": "do",

    "バ": "ba",
    "ビ": "bi",
    "ブ": "bu",
    "ベ": "be",
    "ボ": "bo",

    "パ": "pa",
    "ピ": "pi",
    "プ": "pu",
    "ペ": "pe",
    "ポ": "po"
}

KATAKANA_COMBO: dict[str, str] = {
    "キャ": "kya",
    "キュ": "kyu",
    "キョ": "kyo",

    "ギャ": "gya",
    "ギュ": "gyu",
    "ギョ": "gyo",

    "シャ": "sha",
    "シュ": "shu",
    "ショ": "sho",

    "ジャ": "ja",
    "ジュ": "ju",
    "ジョ": "jo",
    
    "チャ": "cha",
    "チュ": "chu",
    "チョ": "cho",

    "ニャ": "nya",
    "ニュ": "nyu",
    "ニョ": "nyo",

    "ヒャ": "hya",
    "ヒュ": "hyu",
    "ヒョ": "hyo",
    
    "ビャ": "bya",
    "ビュ": "byu",
    "ビョ": "byo",

    "ピャ": "pya",
    "ピュ": "pyu",
    "ピョ": "pyo",

    "ミャ": "mya",
    "ミュ": "myu",
    "ミョ": "myo",
    
    "リャ": "rya",
    "リュ": "ryu",
    "リョ": "ryo"
}

SMALL_ッ: dict[str, str] = {
    "ッ+k": "kk",
    "ッ+s": "ss",
    "ッ+t": "tt",
    "ッ+p": "pp"
}

KATAKANA: dict[str, str] = {
    **KATAKANA_BASE,
    **KATAKANA_DAKUON,
    **KATAKANA_COMBO,
    **SMALL_ッ
}