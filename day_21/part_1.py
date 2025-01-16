from functools import cache
from itertools import pairwise
from pathlib import Path

CURRENT_FOLDER = Path(__file__).absolute().parent
INPUT_FILE = CURRENT_FOLDER / "input.txt"
DEMO_INPUT_FILE = CURRENT_FOLDER / "demo_input.txt"

NUMPAD = {
    0: "7",
    1j: "8",
    2j: "9",
    1: "4",
    1 + 1j: "5",
    1 + 2j: "6",
    2: "1",
    2 + 1j: "2",
    2 + 2j: "3",
    3 + 1j: "0",
    3 + 2j: "A",
}
REVERSE_NUMPAD = {v: k for k, v in NUMPAD.items()}

DIRPAD = {1j: "^", 2j: "A", 1: "<", 1 + 1j: "v", 1 + 2j: ">"}
REVERSE_DIRPAD = {v: k for k, v in DIRPAD.items()}
DIRECTIONS = {"^": -1, "<": -1j, "v": 1, ">": 1j}
REVERSE_DIRECTIONS = {v: k for k, v in DIRECTIONS.items()}


def manhattan_distance(a, b):
    return int(abs((a - b).real)) + int(abs((a - b).imag))


def direction_changes(sequence):
    return sum(1 for a, b in pairwise(sequence) if b != a)


def keypad_move(start, end, keypad):
    """Give list of shortest move sequences on the keypad to move from start to end.

    Args:
        start (complex): start position
        end (complex): end position
        keypad (dict): dict of position: symbol on this keypad

    Returns:
        list: Shortest move sequences on the keypad to move from start to end

    Example:
        keypad_move(3 + 2j, 2 + 1j, NUMPAD) -> ["<^A", "^<A"]
    """
    # Edge case: no need to move
    if end == start:
        return ["A"]

    # General case: build all possible moves
    max_steps = manhattan_distance(start, end)
    frontier = {(start,)}
    for steps in range(max_steps):
        new_frontier = set()
        for positions in frontier:
            current = positions[-1]
            for direction in (1, 1j, -1, -1j):
                neighbour = current + direction
                if (
                    neighbour in keypad
                    and manhattan_distance(neighbour, end) == max_steps - steps - 1
                ):
                    new_frontier.add(positions + (neighbour,))
        frontier = new_frontier
    sequences = []
    for positions in frontier:
        sequences.append(
            "".join(REVERSE_DIRECTIONS[b - a] for a, b in pairwise(positions)) + "A"
        )

    return sequences


@cache
def numpad_move(start, end):
    return keypad_move(start, end, keypad=NUMPAD)


@cache
def dirpad_move(start, end):
    return keypad_move(start, end, keypad=DIRPAD)


def supersequences(base_sequences):
    """Find the shortest sequence of dirpad presses in order to type the code on the dirpad."""
    results = []
    for code in base_sequences:
        initial_pos = 2j
        sequences = [""]
        for letter in code:
            end_pos = REVERSE_DIRPAD[letter]
            possible_moves = dirpad_move(initial_pos, end_pos)
            new_sequences = []
            for moves in possible_moves:
                for sequence in sequences:
                    new_sequences.append(sequence + moves)
            sequences = new_sequences
            initial_pos = end_pos
        results.extend(sequences)
    return results


def shortest_sequence(code):
    """Find the shortest sequence of dirpad presses in order to type the code on the numpad."""
    # The robot arm is at "A" initially
    initial_pos = 3 + 2j
    sequences = [""]
    for letter in code:
        end_pos = REVERSE_NUMPAD[letter]
        possible_moves = numpad_move(initial_pos, end_pos)
        new_sequences = []
        for moves in possible_moves:
            for sequence in sequences:
                new_sequences.append(sequence + moves)
        sequences = new_sequences
        initial_pos = end_pos

    for robot in range(2):
        sequences = supersequences(sequences)
    return min(sequences, key=len)


total = 0

with open(INPUT_FILE) as f:
    for line in f.read().splitlines():
        number = int(line[:-1])
        sequence = shortest_sequence(line)
        print(f"{line}: {sequence}")
        length = len(sequence)
        total += number * length

print(total)
