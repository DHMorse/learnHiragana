import argparse
import random
from rich.panel import Panel
from rich.console import Console
from rich.table import Table

from constants import (
    GROUPS,
    HIRAGANA_BASE,
    DAKUON,
    COMBO,
    SMALL_っ,
    LONG_VOWEL,
    HIRAGANA
)

# Define command line arguments
parser = argparse.ArgumentParser(description='Learn Hiragana')
parser.add_argument('--group', type=str, default='hiragana', help='Group of characters to learn')
parser.add_argument('--count', type=int, default=25, help='Number of characters to practice')

def main() -> None:
    console = Console()

    args: argparse.Namespace = parser.parse_args()

    group: str = args.group.strip().lower()
    if not group:
        group = input("Enter the group of characters to learn: ").strip().lower()

    count: int = args.count
    if not args.count:
        try:
            count = int(input("Enter the number of characters to practice: ").strip())
        except ValueError:
            console.print(Panel("Invalid input. Please enter a valid integer.", style="red"))
            return

    if group not in GROUPS:
        errorMsg = "Invalid group: " + group + "\nValid groups are:\n" + "\n".join(f"  - {g}" for g in GROUPS)
        console.print(Panel(errorMsg, style="red"))
        return

    match group:
        case "base":
            results: dict[str, tuple[str, bool]] = testFromGroup(HIRAGANA_BASE, count)
        case "hiragana_base":
            results = testFromGroup(HIRAGANA_BASE, count)
        case "dakuon":
            results = testFromGroup(DAKUON, count)
        case "combo":
            results = testFromGroup(COMBO, count)
        case "small_っ":
            results = testFromGroup(SMALL_っ, count)
        case "long_vowel":
            results = testFromGroup(LONG_VOWEL, count)
        case "hiragana":
            results = testFromGroup(HIRAGANA, count)
        case "all":
            results = testFromGroup(HIRAGANA, count)
        case _:
            raise ValueError("Invalid group")

    correctCount = sum(1 for result in results.values() if result[1])
    percentage = (correctCount / count) * 100
    
    # Create results table
    table = Table(show_header=True, header_style="bold magenta")
    table.add_column("Metric", style="cyan")
    table.add_column("Value", style="green" if percentage >= 80 else "red")
    
    table.add_row("Percentage", f"{percentage:.1f}%")
    table.add_row("Correct Answers", f"{correctCount} out of {count}")
    
    # Create incorrect answers table
    incorrect_table = Table(show_header=True, header_style="bold red")
    incorrect_table.add_column("Character", style="cyan")
    incorrect_table.add_column("Your Answer", style="red")
    incorrect_table.add_column("Correct Answer", style="green")
    
    for char, (userInput, correct) in results.items():
        if not correct:
            incorrect_table.add_row(char, userInput, HIRAGANA[char])
    
    # Display results
    console.print(Panel(table, title="Results", border_style="green" if percentage >= 80 else "red"))
    
    if incorrect_table.row_count > 0:
        console.print(Panel(incorrect_table, title="Incorrect Answers", border_style="red"))



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
