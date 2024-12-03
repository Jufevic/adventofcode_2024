from pathlib import Path
import re

CURRENT_FOLDER = Path(__file__).absolute().parent
INPUT_FILE = CURRENT_FOLDER / 'input.txt'
DEMO_INPUT_FILE = CURRENT_FOLDER / 'demo_input.txt'

result = 0
with open(INPUT_FILE) as f:
    for line in f.read().splitlines():
        for a, b in re.findall(r'mul\((\d{1,3}),(\d{1,3})\)', line):
            result += int(a) * int(b)
print(result)