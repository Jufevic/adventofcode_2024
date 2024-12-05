from pathlib import Path
from parse import parse
from collections import Counter

CURRENT_FOLDER = Path(__file__).absolute().parent
INPUT_FILE = CURRENT_FOLDER / 'input.txt'
DEMO_INPUT_FILE = CURRENT_FOLDER / 'demo_input.txt'

with open(INPUT_FILE) as f:
    rules, pages = f.read().split("\n\n")

orders = [tuple(parse(r"{:d}|{:d}", line)) for line in rules.split("\n")]
updates = [tuple(map(int, line.split(","))) for line in pages.split("\n")]

total = 0
for update in updates:
    relevant = []
    for a, b in orders:
        if a in update and b in update:
            relevant.append((a, b))
    for a, b in relevant:
        if update.index(a) > update.index(b):
            c = Counter(b for a, b in relevant)
            for number, count in c.items():
                if count == len(update) // 2:
                    total += number
                    break
            break

print(total)