from itertools import product
from pathlib import Path

CURRENT_FOLDER = Path(__file__).absolute().parent
INPUT_FILE = CURRENT_FOLDER / "input.txt"
DEMO_INPUT_FILE = CURRENT_FOLDER / "demo_input.txt"
WORD = "XMAS"

matrix = []
with open(INPUT_FILE) as f:
    for line in f.read().splitlines():
        matrix.append(list(line))

total = 0
height = len(matrix)
width = len(matrix[0])
for i, row in enumerate(matrix):
    for j, letter in enumerate(row):
        for di, dj in product(range(-1, 2), repeat=2):
            if (di, dj) == (0, 0):
                continue
            for index, letter in enumerate(WORD):
                ni, nj = i + index * di, j + index * dj
                if not (
                    (0 <= ni < height)
                    and (0 <= nj < width)
                    and (matrix[ni][nj] == letter)
                ):
                    break
            else:
                total += 1

print(total)
