from pathlib import Path
from collections import defaultdict

CURRENT_FOLDER = Path(__file__).absolute().parent
INPUT_FILE = CURRENT_FOLDER / "input.txt"
DEMO_INPUT_FILE = CURRENT_FOLDER / "demo_input.txt"

filesystem = []
spaces = []
index = -1
with open(INPUT_FILE) as f:
    for pos, digit in enumerate(f.read()):
        space = int(digit)
        if pos % 2:
            spaces.append(space)
        else:
            index += 1
            filesystem.append(space)

blocks = defaultdict(list)
for index, space in reversed(list(enumerate(filesystem))):
    if index == 0:
        blocks[index] = [(index, space)] + blocks[index]
        break
    for position, empty_space in enumerate(spaces[:index]):
        if empty_space >= space:
            blocks[position].append((index, space))
            spaces[position] = empty_space - space
            spaces[index - 1] += space
            break
    else:
        blocks[index] = [(index, space)] + blocks[index]

new_filesystem = []
for index in range(min(len(filesystem), len(spaces))):
    if blocks[index]:
        for block in blocks[index]:
            digit, space = block
            new_filesystem.extend([digit] * space)
    new_filesystem.extend([0] * spaces[index])

checksum = sum(i * value for i, value in enumerate(new_filesystem))
print(checksum)
