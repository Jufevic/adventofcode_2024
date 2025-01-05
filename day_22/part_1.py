from pathlib import Path

CURRENT_FOLDER = Path(__file__).absolute().parent
INPUT_FILE = CURRENT_FOLDER / "input.txt"
DEMO_INPUT_FILE = CURRENT_FOLDER / "demo_input.txt"


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


total = 0

with open(INPUT_FILE) as f:
    for line in f.read().splitlines():
        secret_number = int(line)
        for _ in range(2000):
            secret_number = evolve(secret_number)
        total += secret_number

print(total)
