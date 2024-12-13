from pathlib import Path

CURRENT_FOLDER = Path(__file__).absolute().parent
INPUT_FILE = CURRENT_FOLDER / "input.txt"
DEMO_INPUT_FILE = CURRENT_FOLDER / "demo_input.txt"
DEMO_INPUT_3_FILE = CURRENT_FOLDER / "demo_input_3.txt"
DEMO_INPUT_4_FILE = CURRENT_FOLDER / "demo_input_4.txt"

graph = {}
with open(INPUT_FILE) as f:
    for row, line in enumerate(f.read().splitlines()):
        for col, value in enumerate(line):
            graph[row + 1j * col] = value


total = 0
to_visit = set(graph.keys())
while to_visit:
    pos = next(iter(to_visit))
    value = graph[pos]
    island = {pos}
    queue = [pos]
    # Set of fences coordinates as tuples of start and end positions
    fences = set()
    # Start DFS from there
    while queue:
        new_queue = []
        for pos in queue:
            for direction, start in {1: 1 + 1j, 1j: 1j, -1: 0, -1j: 1}.items():
                neighbour = pos + direction
                if neighbour not in graph or graph[neighbour] != value:
                    fences.add((pos + start, pos + start + direction * -1j))
                elif neighbour not in island:
                    new_queue.append(neighbour)
                    island.add(neighbour)
        queue = new_queue
    to_visit -= island
    area = len(island)

    sides = 0
    while fences:
        # Pick any fence as the starting point
        first = fences.pop()
        start, current = first
        start_direction = current - start
        direction = start_direction
        # Continue fencing until we're back to the starting point
        while any(current in fence for fence in fences):
            # Use right-hand rule: turn right if we can,
            # otherwise go straight ahead, otherwise go left
            for angle in (-1j, 1, 1j):
                new_direction = direction * angle
                neighbour = current + new_direction
                if (current, neighbour) in fences:
                    fences.remove((current, neighbour))
                    break
                elif (neighbour, current) in fences:
                    fences.remove((neighbour, current))
                    break

            if new_direction != direction:
                sides += 1
            current = neighbour
            direction = new_direction
        if start_direction != direction:
            sides += 1
    total += area * sides

print(total)
