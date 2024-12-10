from pathlib import Path
from collections import deque

CURRENT_FOLDER = Path(__file__).absolute().parent
INPUT_FILE = CURRENT_FOLDER / "input.txt"
DEMO_INPUT_FILE = CURRENT_FOLDER / "demo_input.txt"

filesystem = deque([])
occupation = []
index = -1
with open(INPUT_FILE) as f:
    for pos, digit in enumerate(f.read()):
        space = int(digit)
        if pos % 2:
            occupation.extend([False] * space)
        else:
            index += 1
            filesystem.extend([index] * space)
            occupation.extend([True] * space)

new_filesystem = []
for occupied in occupation[: len(filesystem)]:
    if occupied:
        new_filesystem.append(filesystem.popleft())
    else:
        new_filesystem.append(filesystem.pop())

checksum = sum(i * value for i, value in enumerate(new_filesystem))
print(checksum)
