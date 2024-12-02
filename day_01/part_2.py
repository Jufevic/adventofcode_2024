from pathlib import Path
from collections import Counter
from aocd import submit

CURRENT_FOLDER = Path(__file__).absolute().parent
INPUT_FILE = CURRENT_FOLDER / 'input.txt'
DEMO_INPUT_FILE = CURRENT_FOLDER / 'demo_input.txt'

lefts = []
rights = []
with open(INPUT_FILE) as f:
    for line in f.read().splitlines():
        left, right = map(int, line.split())
        lefts.append(left)
        rights.append(right)

left_c = Counter(lefts)
right_c = Counter(rights)
similarity = 0
for number, count in left_c.items():
    similarity += number * count * right_c[number]
submit(similarity)