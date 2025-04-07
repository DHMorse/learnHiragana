# Learn Hiragana

A command-line interface (CLI) program designed to help users learn and practice Hiragana characters. This tool provides an interactive way to test your knowledge of Hiragana characters and their corresponding romaji.

## Features

- Practice different groups of Hiragana characters:
  - Base characters
  - Dakuon (voiced consonants)
  - Combo characters
  - Small っ characters
  - Long vowel characters
  - All characters combined
- Customizable number of characters per practice session
- Immediate feedback on correct/incorrect answers
- Score tracking with percentage calculation
- Color-coded results for better visibility

## Installation

1. Clone this repository:
```bash
git clone https://github.com/DHMorse/learnHiragana
cd learnHiragana
```
## uv

2. Install dependencies:
```bash
uv sync
```

## pip

2. Install dependencies:
```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

## Usage

Run the program with default settings (25 characters from all groups):
```bash
python src/main.py
```

### Command Line Arguments

- `--group`: Specify which group of characters to practice
  - Options: base, dakuon, combo, small_っ, long_vowel, all
  - Default: all
- `--count`: Set the number of characters to practice
  - Default: 25

Example:
```bash
python main.py --group base --count 10
```

### Interactive Mode

If no arguments are provided, the program will prompt you to:
1. Enter the group of characters you want to practice
2. Specify how many characters you want to test

## Results

After completing the practice session, you'll receive:
- Your overall score as a percentage
- Number of correct answers
- A detailed list of incorrect answers with the correct romaji

## Requirements

- Python 3.10 or higher