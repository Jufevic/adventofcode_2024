from pathlib import Path
from itertools import product

CURRENT_FOLDER = Path(__file__).absolute().parent
INPUT_FILE = CURRENT_FOLDER / "input.txt"
DEMO_INPUT_FILE = CURRENT_FOLDER / "demo_input.txt"

with open(INPUT_FILE) as f:
    blocks = f.read().split("\n\n")

keys = set()
locks = set()

for block in blocks:
    lines = block.splitlines()
    heights = [0] * 5

    # If this is a lock
    if lines[0] == "#" * 5:
        for col in range(5):
            for row in range(1, 7):
                if lines[row][col] == ".":
                    break
            heights[col] = row - 1
        locks.add(tuple(heights))

    # If this is a key
    if lines[0] == "." * 5:
        for col in range(5):
            for row in range(1, 7):
                if lines[row][col] == "#":
                    break
            heights[col] = 6 - row
        keys.add(tuple(heights))


def pair_fit(lock, key):
    for a, b in zip(lock, key):
        if a + b > 5:
            return False
    return True


print(sum(pair_fit(lock, key) for lock, key in product(locks, keys)))
