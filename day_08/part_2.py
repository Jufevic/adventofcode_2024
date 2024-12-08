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
        for start, side in (a, a - b), (b, b - a):
            n = 0
            while (antinode := start + n * side) in graph:
                antinodes.add(antinode)
                n += 1

print(len(antinodes))
