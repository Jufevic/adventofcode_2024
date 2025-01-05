from pathlib import Path
from collections import defaultdict

CURRENT_FOLDER = Path(__file__).absolute().parent
INPUT_FILE = CURRENT_FOLDER / "input.txt"
DEMO_INPUT_FILE = CURRENT_FOLDER / "demo_input.txt"

graph = defaultdict(list)

with open(INPUT_FILE) as f:
    for line in f.read().splitlines():
        first, second = line.split("-")
        graph[first].append(second)
        graph[second].append(first)

three_connections = set()
for first, connections in graph.items():
    for second in connections:
        for third in graph[second]:
            if third in connections:
                three_connections.add(frozenset({first, second, third}))

total = 0
for trio in three_connections:
    if any(computer.startswith("t") for computer in trio):
        total += 1
print(total)
