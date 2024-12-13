from pathlib import Path

CURRENT_FOLDER = Path(__file__).absolute().parent
INPUT_FILE = CURRENT_FOLDER / "input.txt"
DEMO_INPUT_FILE = CURRENT_FOLDER / "demo_input.txt"
DEMO_INPUT_2_FILE = CURRENT_FOLDER / "demo_input_2.txt"

graph = {}
with open(INPUT_FILE) as f:
    for row, line in enumerate(f.read().splitlines()):
        for col, value in enumerate(line):
            graph[row + 1j * col] = value


total = 0
to_visit = set(graph.keys())
while to_visit:
    pos = to_visit.pop()
    value = graph[pos]
    island = {pos}
    queue = [pos]
    perimeter = 0
    # Start DFS from there
    while queue:
        new_queue = []
        for pos in queue:
            for direction in (1, 1j, -1, -1j):
                neighbour = pos + direction
                if neighbour not in graph:
                    perimeter += 1
                else:
                    if graph[neighbour] != value:
                        perimeter += 1
                    elif neighbour not in island:
                        new_queue.append(neighbour)
                        island.add(neighbour)
        queue = new_queue
    to_visit -= island
    area = len(island)
    total += area * perimeter

print(total)
