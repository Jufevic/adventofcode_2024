from pathlib import Path
from collections import defaultdict
from heapq import heappop, heappush

CURRENT_FOLDER = Path(__file__).absolute().parent
INPUT_FILE = CURRENT_FOLDER / "input.txt"
DEMO_INPUT_FILE = CURRENT_FOLDER / "demo_input.txt"
DEMO_INPUT_2_FILE = CURRENT_FOLDER / "demo_input_2.txt"
START = "S"
EXIT = "E"
EMPTY = "."
WALL = "#"

empties = set()
with open(INPUT_FILE) as f:
    for row, line in enumerate(f.read().splitlines()):
        for col, value in enumerate(line):
            position = row + 1j * col
            if value == START:
                empties.add(position)
                start = position
            elif value == EXIT:
                empties.add(position)
                goal = position
            elif value == EMPTY:
                empties.add(position)

# Graph construction
graph = defaultdict(dict)
for position in empties:
    for direction in (1, 1j, -1, -1j):
        for new_dir in direction * 1j, direction * -1j:
            graph[(position, direction)][(position, new_dir)] = 1000
        if position + direction in empties:
            graph[(position, direction)][(position + direction, direction)] = 1

# Dijlstra main loop
frontier = []
cost_so_far = defaultdict(int)
cost_so_far[start] = 0
heappush(frontier, (0, (start.real, start.imag, 0, 1), (start, 1j)))
while frontier:
    cost, _, current = heappop(frontier)

    # Early exit
    if current[0] == goal:
        break

    for neighbour, cost in graph[current].items():
        new_cost = cost_so_far[current] + cost
        if neighbour not in cost_so_far or new_cost < cost_so_far[neighbour]:
            cost_so_far[neighbour] = new_cost
            priority = new_cost
            # Add a position tuple to allow sorting of positions with the same priority
            heappush(
                frontier,
                (
                    priority,
                    (
                        neighbour[0].real,
                        neighbour[0].imag,
                        neighbour[1].real,
                        neighbour[1].imag,
                    ),
                    neighbour,
                ),
            )

print(cost)
