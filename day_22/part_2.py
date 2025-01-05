from pathlib import Path
from collections import Counter

CURRENT_FOLDER = Path(__file__).absolute().parent
INPUT_FILE = CURRENT_FOLDER / "input.txt"
DEMO_INPUT_FILE = CURRENT_FOLDER / "demo_input.txt"
DEMO_INPUT_FILE_2 = CURRENT_FOLDER / "demo_input_2.txt"
DEMO_INPUT_FILE_3 = CURRENT_FOLDER / "demo_input_3.txt"

secret_numbers = []
with open(INPUT_FILE) as f:
    for line in f.read().splitlines():
        secret_numbers.append(int(line))


def mix(secret_number, other):
    return secret_number ^ other


def prune(secret_number):
    return secret_number % 16777216


def evolve(secret_number):
    secret_number = mix(secret_number, secret_number << 6)
    secret_number = prune(secret_number)
    secret_number = mix(secret_number, secret_number >> 5)
    secret_number = prune(secret_number)
    secret_number = mix(secret_number, secret_number << 11)
    secret_number = prune(secret_number)
    return secret_number


c = Counter()
for initial in secret_numbers:
    secret_number = initial
    last_digit = secret_number % 10
    differences = []
    bananas = []
    seen = {}
    for position in range(2000):
        secret_number = evolve(secret_number)
        new_digit = secret_number % 10
        bananas.append(new_digit)
        differences.append(new_digit - last_digit)
        last_digit = new_digit
        if position >= 4:
            sequence = tuple(differences[-4:])
            if sequence not in seen:
                seen[sequence] = new_digit
    c.update(seen)

print(c.most_common(1)[0])
