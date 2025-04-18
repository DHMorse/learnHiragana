# Learn Hiragana and Katakana

A command-line interface (CLI) program designed to help users learn and practice Hiragana and Katakana characters. This tool provides an interactive way to test your knowledge of Japanese characters and their corresponding romaji.

## Features

- Practice different groups of characters:
  - Hiragana:
    - Base characters
    - Dakuon (voiced consonants)
    - Combo characters
    - Small っ characters
    - Long vowel characters
    - All Hiragana combined
  - Katakana:
    - Base characters
    - Dakuon (voiced consonants)
    - Combo characters
    - Small ッ characters
    - All Katakana combined
  - All characters combined
- Customizable number of characters per practice session
- Two practice modes:
  - Romaji mode: Type the romaji for given characters
  - Hiragana mode: Type the Hiragana for given romaji
- Immediate feedback on correct/incorrect answers
- Score tracking with percentage calculation
- Color-coded results for better visibility

## Installation

### Using uv (recommended)

1. Clone this repository:
```bash
git clone https://github.com/DHMorse/learnHiragana
cd learnHiragana
```

2. Install dependencies:
```bash
uv sync
```

### Using pip

1. Clone this repository:
```bash
git clone https://github.com/DHMorse/learnHiragana
cd learnHiragana
```

2. Create and activate a virtual environment:
```bash
python3 -m venv venv
source venv/bin/activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

## Usage

Run the program with default settings (25 characters from all groups):
```bash
uv run learnHiragana/main.py
```
or
```bash
python learnHiragana/main.py
```

### Command Line Arguments

- `--group`: Specify which group of characters to practice
  - Options: base, hiragana_base, dakuon, combo, small_っ, long_vowel, hiragana, katakana, katakana_base, katakana_dakuon, katakana_combo, small_ッ, all
  - Default: hiragana
- `--count`: Set the number of characters to practice
  - Default: 25

Example:
```bash
uv run learnHiragana/main.py --group katakana_base --count 10
```
or
```bash
python learnHiragana/main.py --group katakana_base --count 10
```

## Results

After completing the practice session, you'll receive:
- Your overall score as a percentage
- Number of correct answers
- A detailed list of incorrect answers with the correct romaji

## Requirements

- Python 3.10 or higher
- pip or uv