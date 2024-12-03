from pathlib import Path
import re

CURRENT_FOLDER = Path(__file__).absolute().parent
INPUT_FILE = CURRENT_FOLDER / 'input.txt'
DEMO_INPUT_FILE = CURRENT_FOLDER / 'demo_input_2.txt'

result = 0
with open(INPUT_FILE) as f:
    content = f.read().replace('\n', '')
    new_content = ""
    start = 0
    for m in re.finditer(r"don't\(\)(.*?)do\(\)", content):
        end = m.start()
        new_content = new_content + content[start:m.start()]
        start = m.end()
    new_content = new_content + content[start:]
    for a, b in re.findall(r'mul\((\d{1,3}),(\d{1,3})\)', new_content):
        result += int(a) * int(b)
print(result)