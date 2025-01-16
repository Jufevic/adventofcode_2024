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


def keypad_moves(start, end, keypad):
    """Give list of shortest move sequences on the keypad to move from start to end.

    Args:
        start (complex): start position
        end (complex): end position
        keypad (dict): dict of position: symbol on this keypad

    Returns:
        list: Shortest move sequences on the keypad to move from start to end

    Example:
        keypad_moves(3 + 2j, 2 + 1j, NUMPAD) -> ["<^A", "^<A"]
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
def numpad_moves(start, end):
    return keypad_moves(start, end, keypad=NUMPAD)


@cache
def dirpad_moves(start, end):
    return keypad_moves(start, end, keypad=DIRPAD)


@cache
def movement_cost(sequence, robots):
    """Find the number of movements needed to generate the given sequence, with `robots` robots.

    We assume that the initial position is the 'A' position on the dirpad.

    :param sequence: A sequence, as a string of direction symbols
        (any of '<', '^', '>', 'v'), followed by 'A'.
    :param robots: The number of robots typing that sequence (for robots=1, that's just the)
    """
    if robots == 1:
        total = 0
        for a, b in zip("A" + sequence, sequence):
            initial_pos = REVERSE_DIRPAD[a]
            end_pos = REVERSE_DIRPAD[b]
            total += manhattan_distance(initial_pos, end_pos) + 1
        return total
    total = 0
    for a, b in zip("A" + sequence, sequence):
        best_so_far = float("inf")
        initial_pos = REVERSE_DIRPAD[a]
        end_pos = REVERSE_DIRPAD[b]
        for possibility in dirpad_moves(initial_pos, end_pos):
            best_so_far = min(best_so_far, movement_cost(possibility, robots - 1))
        total += best_so_far
    return total


total = 0

with open(INPUT_FILE) as f:
    for line in f.read().splitlines():
        number = int(line[:-1])
        subtotal = 0
        for a, b in zip("A" + line, line):
            init_pos = REVERSE_NUMPAD[a]
            end_pos = REVERSE_NUMPAD[b]
            sequences = numpad_moves(init_pos, end_pos)
            min_length = float("inf")
            for sequence in sequences:
                min_length = min(min_length, movement_cost(sequence, robots=25))
            subtotal += min_length
        total += number * subtotal

print(total)
