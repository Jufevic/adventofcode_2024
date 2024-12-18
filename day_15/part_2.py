from pathlib import Path

CURRENT_FOLDER = Path(__file__).absolute().parent
INPUT_FILE = CURRENT_FOLDER / "input.txt"
DEMO_INPUT_FILE = CURRENT_FOLDER / "demo_input.txt"
DEMO_INPUT_2_FILE = CURRENT_FOLDER / "demo_input_2.txt"
DEMO_INPUT_3_FILE = CURRENT_FOLDER / "demo_input_3.txt"
EMPTY = "."
WALL = "#"
BOX = "O"
ROBOT = "@"

with open(INPUT_FILE) as f:
    grid, instructions = f.read().split("\n\n")

graph = {}
for row, line in enumerate(grid.splitlines()):
    for col, value in enumerate(line):
        position = row + 2j * col
        if value == WALL:
            graph[position] = WALL
            graph[position + 1j] = WALL
        elif value == BOX:
            graph[position] = "["
            graph[position + 1j] = "]"
        elif value == EMPTY:
            graph[position] = EMPTY
            graph[position + 1j] = EMPTY
        elif value == ROBOT:
            graph[position] = EMPTY
            graph[position + 1j] = EMPTY
            current = position

for instruction in "".join(instructions.splitlines()):
    direction = {"<": -1j, "^": -1, ">": 1j, "v": 1}[instruction]
    neighbour = current + direction
    if graph[neighbour] == WALL:
        continue
    if graph[neighbour] == EMPTY:
        current = neighbour
        continue
    # If we are pushing vertically
    if direction.imag == 0:
        if graph[neighbour] == "[":
            queue = {neighbour, neighbour + 1j}
        elif graph[neighbour] == "]":
            queue = {neighbour - 1j, neighbour}

        # Try to push all blocks in this direction
        can_move = True
        to_move = []
        while queue and can_move:
            new_queue = set()
            for block in queue:
                neighbour = block + direction
                if graph[neighbour] == WALL:
                    can_move = False
                    break
                elif graph[neighbour] in "[]":
                    if direction.imag == 0:
                        if graph[neighbour] == "[":
                            new_queue.add(neighbour)
                            new_queue.add(neighbour + 1j)
                        elif graph[neighbour] == "]":
                            new_queue.add(neighbour)
                            new_queue.add(neighbour - 1j)
                    else:
                        new_queue.add(neighbour + direction)
            to_move.append(queue)
            queue = new_queue

        # If the robot can move, push all boxes
        if not can_move:
            continue
        while to_move:
            blocks = to_move.pop()
            for block in blocks:
                graph[block + direction] = graph[block]
                graph[block] = EMPTY
        current += direction

    # We are pushing horizontally
    else:
        to_move = [neighbour, neighbour + direction]
        while graph[neighbour] in "[]":
            to_move.append(neighbour)
            to_move.append(neighbour + direction)
            neighbour += 2 * direction
        if graph[neighbour] == EMPTY:
            for old, new in zip(to_move[::-1], [neighbour] + to_move[-1:0:-1]):
                graph[new] = graph[old]
                graph[old] = EMPTY
            current += direction
            graph[current] = EMPTY


total = 0
for pos, value in graph.items():
    if value != "[":
        continue
    total += 100 * int(pos.real) + int(pos.imag)

print(total)
