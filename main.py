import argparse
import random
from termcolor import colored

from constants import *

# Define command line arguments
parser = argparse.ArgumentParser(description='Learn Hiragana')
parser.add_argument('--group', type=str, default='all', help='Group of characters to learn')
parser.add_argument('--count', type=int, default=25, help='Number of characters to practice')

def main() -> None:
    groups: list[str] = ["hiragana", "dakuon", "combo", "small_っ", "long_vowel", "all"]

    args: argparse.Namespace = parser.parse_args()

    group: str = args.group.strip().lower()
    if not group:
        group = input("Enter the group of characters to learn: ").strip().lower()

    count: int = args.count
    if not args.count:
        try:
            count = int(input("Enter the number of characters to practice: ").strip())
        except ValueError:
            print("Invalid input. Please enter a valid integer.")
            return

    if group not in groups:
        print(f"Invalid group: {group}")
        print("Valid groups are:")
        for g in groups:
            print(f"  - {g}")
        return

    match group:
        case "hiragana":
            results: dict[str, tuple[str, bool]] = testFromGroup(HIRAGANA, count)
        case "dakuon":
            results: dict[str, tuple[str, bool]] = testFromGroup(DAKUON, count)
        case "combo":
            results: dict[str, tuple[str, bool]] = testFromGroup(COMBO, count)
        case "small_っ":
            results: dict[str, tuple[str, bool]] = testFromGroup(SMALL_っ, count)
        case "long_vowel":
            results: dict[str, tuple[str, bool]] = testFromGroup(LONG_VOWEL, count)
        case "all":
            results: dict[str, tuple[str, bool]] = testFromGroup(ALL, count)
        case _:
            raise ValueError("Invalid group")

    correctCount = sum(1 for result in results.values() if result[1])
    
    percentage = (correctCount / count) * 100
    if percentage < 80:
        print(f"\nYou got {colored(f'{percentage:.1f}%', 'red')} of the characters correct.")
        print(f"You got {colored(f'{correctCount} out of {count}', 'red')} characters correct.")
    else:
        print(f"\nYou got {colored(f'{percentage:.1f}%', 'green')} of the characters correct.")
        print(f"You got {colored(f'{correctCount} out of {count}', 'green')} characters correct.")
    print(f"\n{colored('Incorrect answers:', 'red')}:")
    
    for char, (userInput, correct) in results.items():
        if not correct:
            print(f"{char}: Your answer: {colored(userInput, 'red')} (correct: {colored(ALL[char], 'green')})")



def testFromGroup(group: dict[str, str], count: int) -> dict[str, tuple[str, bool]]:
    """
    Test the user on the given group of characters.
    Args:
        group: dict[str, str] - Dictionary mapping hiragana characters to their romaji equivalents
        count: int - Number of characters to test (must be positive)
    Returns:
        dict[str, tuple[str, bool]] - Dictionary mapping tested hiragana characters to a tuple of (user input, whether correct)
    Raises:
        ValueError - If count is not a positive integer or group is not a dictionary
    """
    if not count or count <= 0 or type(count) != int:
        raise ValueError("Count must be greater than 0 and an integer")

    if not group or type(group) != dict:
        raise ValueError("Group must be a dictionary")
    
    results: dict[str, tuple[str, bool]] = {}

    for i in range(count):
        key: str = random.choice(list(group.keys()))
        value: str = group[key]
        userInput: str = input(f"Enter the romaji for {key}: ")
        results[key] = (userInput, userInput == value)

    return results

if __name__ == "__main__":
    main()
