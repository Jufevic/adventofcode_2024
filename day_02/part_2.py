from pathlib import Path

CURRENT_FOLDER = Path(__file__).absolute().parent
INPUT_FILE = CURRENT_FOLDER / 'input.txt'
DEMO_INPUT_FILE = CURRENT_FOLDER / 'demo_input.txt'

def is_safe(line):
    sign = line[1] - line[0]
    for a, b in zip(line[:-1], line[1:]):
        if abs(b - a) < 1 or abs(b - a) > 3:
            return False
        if (b - a) * sign < 0:
            return False
    return True
    

safe = 0
with open(DEMO_INPUT_FILE) as f:
    for line in f.read().splitlines():
        numbers = [int(i) for i in line.split()]
        if is_safe(numbers):
            safe += 1
        else:
            for i in range(len(numbers)):
                if is_safe(numbers[:i] + numbers [i + 1:]):
                    safe += 1
                    break
print(safe)