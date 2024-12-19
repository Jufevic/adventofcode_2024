from functools import cache
from pathlib import Path

CURRENT_FOLDER = Path(__file__).absolute().parent
INPUT_FILE = CURRENT_FOLDER / "input.txt"
DEMO_INPUT_FILE = CURRENT_FOLDER / "demo_input.txt"

with open(INPUT_FILE) as f:
    pattern_line, designs = f.read().split("\n\n")

patterns = pattern_line.split(", ")


@cache
def solve(design):
    """Recursively find a combination of towels that form the given pattern."""
    if not design:
        return 1
    total = 0
    for pattern in patterns:
        if len(pattern) <= len(design) and design.startswith(pattern):
            total += solve(design[len(pattern) :])
    return total


print(sum(solve(design) for design in designs.splitlines()))
