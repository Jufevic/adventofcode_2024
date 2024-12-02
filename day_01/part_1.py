from pathlib import Path
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

lefts.sort()
rights.sort()
distance = 0
for left, right in zip(lefts, rights):
    distance += abs(left - right)
submit(distance)