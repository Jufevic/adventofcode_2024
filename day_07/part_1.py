from pathlib import Path

CURRENT_FOLDER = Path(__file__).absolute().parent
INPUT_FILE = CURRENT_FOLDER / "input.txt"
DEMO_INPUT_FILE = CURRENT_FOLDER / "demo_input.txt"


total = 0
with open(INPUT_FILE) as f:
    for line in f.read().splitlines():
        test_value, numbers = line.split(":")
        test_value = int(test_value)
        numbers = [int(i) for i in numbers.split()]
        values = {numbers[0]}
        for number in numbers[1:]:
            new_values = set()
            for value in values:
                new_values.add(value + number)
                new_values.add(value * number)
            values = new_values
        if test_value in values:
            total += test_value

print(total)
