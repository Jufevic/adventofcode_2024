from pathlib import Path

CURRENT_FOLDER = Path(__file__).absolute().parent
INPUT_FILE = CURRENT_FOLDER / 'input.txt'
DEMO_INPUT_FILE = CURRENT_FOLDER / 'demo_input.txt'

safe = 0
with open(INPUT_FILE) as f:
    for line in f.read().splitlines():
        numbers = [int(i) for i in line.split()]
        sign = numbers[1] - numbers[0]
        for a, b in zip(numbers[:-1], numbers[1:]):
            if abs(b - a) < 1 or abs(b - a) > 3:
                break
            if (b - a) * sign < 0:
                break
        else:
            safe += 1
print(safe)