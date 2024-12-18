from pathlib import Path

CURRENT_FOLDER = Path(__file__).absolute().parent
INPUT_FILE = CURRENT_FOLDER / "input.txt"
DEMO_INPUT_FILE = CURRENT_FOLDER / "demo_input.txt"
WIDTH = 71  # 7 for demo input, 71 for real input

graph = {row + 1j * col: "." for row in range(WIDTH) for col in range(WIDTH)}
start = 0
goal = WIDTH - 1 + (WIDTH - 1) * 1j

with open(INPUT_FILE) as f:
    for count, line in enumerate(f.read().splitlines()):
        row, col = map(int, line.split(","))
        graph[row + 1j * col] = "#"
        blocked = True

        current = start
        frontier = {start}
        visited = set()
        while frontier:
            new_frontier = set()
            for current in frontier:
                if current == goal:
                    blocked = False
                    break
                for direction in (1, 1j, -1, -1j):
                    neighbour = current + direction
                    if (
                        neighbour in graph
                        and neighbour not in visited
                        and graph[neighbour] == "."
                    ):
                        new_frontier.add(neighbour)
                        visited.add(neighbour)
            frontier = new_frontier

        if blocked:
            print(f"{row},{col}")
            break
