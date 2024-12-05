from pathlib import Path
from parse import parse

CURRENT_FOLDER = Path(__file__).absolute().parent
INPUT_FILE = CURRENT_FOLDER / 'input.txt'
DEMO_INPUT_FILE = CURRENT_FOLDER / 'demo_input.txt'

with open(INPUT_FILE) as f:
    rules, pages = f.read().split("\n\n")

orders = [tuple(parse(r"{:d}|{:d}", line)) for line in rules.split("\n")]
updates = [tuple(map(int, line.split(","))) for line in pages.split("\n")]

total = 0
for update in updates:
    for a, b in orders:
        if a not in update or b not in update:
            continue
        if update.index(a) > update.index(b):
            break
    else:
        mid_index = len(update) // 2
        total += update[mid_index]

print(total)