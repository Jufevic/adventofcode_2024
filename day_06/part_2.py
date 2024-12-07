from pathlib import Path

CURRENT_FOLDER = Path(__file__).absolute().parent
INPUT_FILE = CURRENT_FOLDER / "input.txt"
DEMO_INPUT_FILE = CURRENT_FOLDER / "demo_input.txt"

graph = {}
with open(INPUT_FILE) as f:
    for row, line in enumerate(f.read().splitlines()):
        for col, value in enumerate(line):
            graph[row + 1j * col] = value

start = next(pos for pos, value in graph.items() if value == "^")
current = start
direction = -1
obstacles = set()

def travel(graph, current, direction):
    visited = {(current, direction)}
    while current in graph:
        next_pos = current + direction

        # Will the guard leave the mapped area?
        if next_pos not in graph:
            break

        # The guard turns right at an obstacle
        while graph[next_pos] == "#":
            direction *= -1j
            next_pos = current + direction
            if next_pos not in graph:
                return visited
        current = next_pos
        if (current, direction) in visited:
            return visited, True
        visited.add((current, direction))
    return visited, False

path = travel(graph, current, direction)[0]
for (position, direct) in path:
    if travel(graph | {position: "#"}, start, -1)[1]:
        obstacles.add(position)

print(len(obstacles))
