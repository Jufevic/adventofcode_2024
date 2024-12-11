from pathlib import Path

CURRENT_FOLDER = Path(__file__).absolute().parent
INPUT_FILE = CURRENT_FOLDER / "input.txt"
DEMO_INPUT_FILE = CURRENT_FOLDER / "demo_input.txt"

with open(INPUT_FILE) as f:
    stones = [int(stone) for stone in f.read().split()]


def change(stones):
    new_stones = []
    for stone in stones:
        if stone == 0:
            new_stones.append(1)
            continue
        elif len(str(stone)) % 2 == 0:
            s = str(stone)
            n = len(s)
            new_stones.append(int(s[: n // 2]))
            new_stones.append(int(s[n // 2 :]))
            continue
        else:
            new_stones.append(stone * 2024)
    return new_stones


for _ in range(25):
    stones = change(stones)

print(len(stones))
