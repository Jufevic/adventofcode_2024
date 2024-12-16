from pathlib import Path

CURRENT_FOLDER = Path(__file__).absolute().parent
INPUT_FILE = CURRENT_FOLDER / "input.txt"
DEMO_INPUT_FILE = CURRENT_FOLDER / "demo_input.txt"
DEMO_INPUT_2_FILE = CURRENT_FOLDER / "demo_input_2.txt"
EMPTY = "."
WALL = "#"
BOX = "O"
ROBOT = "@"

with open(INPUT_FILE) as f:
    grid, instructions = f.read().split("\n\n")

graph = {}
for row, line in enumerate(grid.splitlines()):
    for col, value in enumerate(line):
        position = row + 1j * col
        if value == ROBOT:
            graph[position] = EMPTY
            current = position
        else:
            graph[position] = value

for instruction in "".join(instructions.splitlines()):
    direction = {"<": -1j, "^": -1, ">": 1j, "v": 1}[instruction]
    neighbour = current + direction
    if graph[neighbour] == WALL:
        continue
    if graph[neighbour] == EMPTY:
        current = neighbour
        continue
    while graph[neighbour] == BOX:
        neighbour += direction
    if graph[neighbour] == EMPTY:
        current += direction
        graph[current] = EMPTY
        graph[neighbour] = BOX

total = 0
for pos, value in graph.items():
    if value != BOX:
        continue
    total += 100 * int(pos.real) + int(pos.imag)

print(total)
