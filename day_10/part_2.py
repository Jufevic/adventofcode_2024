from pathlib import Path
from collections import defaultdict

CURRENT_FOLDER = Path(__file__).absolute().parent
INPUT_FILE = CURRENT_FOLDER / "input.txt"
DEMO_INPUT_FILE = CURRENT_FOLDER / "demo_input.txt"

graph = {}
starts = set()
with open(INPUT_FILE) as f:
    for row, line in enumerate(f.read().splitlines()):
        for col, value in enumerate(line):
            pos = row + 1j * col
            graph[pos] = int(value)
            if int(value) == 0:
                starts.add(pos)

total = 0
for start in starts:
    height = 0
    queue = defaultdict(int)
    queue[start] = 1
    while height < 9:
        new_queue = defaultdict(int)
        for pos, multiplicity in queue.items():
            for direction in (1, 1j, -1, -1j):
                neighbour = pos + direction
                if neighbour in graph and graph[neighbour] - height == 1:
                    new_queue[neighbour] += multiplicity
        queue = new_queue
        height += 1
    total += sum(queue.values())

print(total)
