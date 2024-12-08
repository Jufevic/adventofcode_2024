from collections import defaultdict
from itertools import combinations
from pathlib import Path

CURRENT_FOLDER = Path(__file__).absolute().parent
INPUT_FILE = CURRENT_FOLDER / "input.txt"
DEMO_INPUT_FILE = CURRENT_FOLDER / "demo_input.txt"

graph = {}
antennas = defaultdict(set)
with open(INPUT_FILE) as f:
    for row, line in enumerate(f.read().splitlines()):
        for col, value in enumerate(line):
            pos = row + 1j * col
            graph[pos] = value
            if value != ".":
                antennas[value].add(pos)

antinodes = set()
for positions in antennas.values():
    for a, b in combinations(positions, 2):
        for antinode in (2 * a - b, 2 * b - a):
            if antinode in graph:
                antinodes.add(antinode)

print(len(antinodes))
