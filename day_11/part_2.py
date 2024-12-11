from pathlib import Path
from collections import Counter, defaultdict

CURRENT_FOLDER = Path(__file__).absolute().parent
INPUT_FILE = CURRENT_FOLDER / "input.txt"
DEMO_INPUT_FILE = CURRENT_FOLDER / "demo_input.txt"

with open(INPUT_FILE) as f:
    stones = [int(stone) for stone in f.read().split()]

stones = Counter(stones)


def change(stones):
    new_stones = defaultdict(int)
    for stone, count in stones.items():
        if stone == 0:
            new_stones[1] += count
            continue
        elif len(str(stone)) % 2 == 0:
            s = str(stone)
            n = len(s)
            new_stones[int(s[: n // 2])] += count
            new_stones[int(s[n // 2 :])] += count
            continue
        else:
            new_stones[stone * 2024] += count
    return new_stones


for _ in range(75):
    stones = change(stones)

print(sum(stones.values()))
