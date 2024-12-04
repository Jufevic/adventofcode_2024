from pathlib import Path

CURRENT_FOLDER = Path(__file__).absolute().parent
INPUT_FILE = CURRENT_FOLDER / "input.txt"
DEMO_INPUT_FILE = CURRENT_FOLDER / "demo_input.txt"
WORD = {"M", "A", "S"}

matrix = []
with open(INPUT_FILE) as f:
    for line in f.read().splitlines():
        matrix.append(list(line))

total = 0
height = len(matrix)
width = len(matrix[0])
for i, row in enumerate(matrix):
    for j, letter in enumerate(row):
        if not ((1 <= i < height - 1) and (1 <= j < width - 1)):
            continue
        if letter == "A":
            diagonal = [
                matrix[ni][nj]
                for ni, nj in zip(range(i - 1, i + 2), range(j - 1, j + 2))
            ]
            antidiagonal = [
                matrix[ni][nj]
                for ni, nj in zip(range(i - 1, i + 2), reversed(range(j - 1, j + 2)))
            ]
            if set(diagonal) == WORD and set(antidiagonal) == WORD:
                total += 1

print(total)
