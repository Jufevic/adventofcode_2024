from pathlib import Path

CURRENT_FOLDER = Path(__file__).absolute().parent
INPUT_FILE = CURRENT_FOLDER / "input.txt"
DEMO_INPUT_FILE = CURRENT_FOLDER / "demo_input.txt"
START = "S"
EXIT = "E"
EMPTY = "."
WALL = "#"
CHEAT_LENGTH = 2
MIN_SAVE = 100

graph = {}
with open(INPUT_FILE) as f:
    for row, line in enumerate(f.read().splitlines()):
        for col, value in enumerate(line):
            position = row + 1j * col
            if value == START:
                graph[position] = EMPTY
                start = position
            elif value == EXIT:
                graph[position] = EMPTY
                goal = position
            else:
                graph[position] = value


def distances_from(position):
    """Find the minimum distance from a given position to all other positions in
    the racetrack."""
    distances = {position: 0}
    frontier = {position}
    steps = 0
    while frontier:
        steps += 1
        new_frontier = set()
        for current in frontier:
            for direction in (1, 1j, -1, -1j):
                neighbour = current + direction
                if (
                    neighbour in graph
                    and neighbour not in distances
                    and graph[neighbour] == "."
                ):
                    new_frontier.add(neighbour)
                    distances[neighbour] = steps
        frontier = new_frontier
    return distances


distances_from_start = distances_from(start)
distances_to_goal = distances_from(goal)
init_steps = distances_from_start[goal]
print(
    f"Fastest time in the original racetrack: {distances_from_start[goal]} picoseconds."
)

speedups = 0
for position, start_distance in distances_from_start.items():
    # print(f"Cheat start position: {position}")
    frontier = {position}
    visited = {position}
    steps = 0
    # Only explore cheats at most CHEAT_LENGTH long
    while steps < CHEAT_LENGTH:
        steps += 1
        new_frontier = set()
        for current in frontier:
            for direction in (1, 1j, -1, -1j):
                neighbour = current + direction
                if neighbour in graph and neighbour not in visited:
                    new_frontier.add(neighbour)
                    visited.add(neighbour)
                    if neighbour in distances_to_goal:
                        new_length = (
                            start_distance + steps + distances_to_goal[neighbour]
                        )
                        time_save = init_steps - new_length
                        # Only consider shortcut if the time saved is higher than
                        # or equal to MIN_SAVE
                        if time_save >= MIN_SAVE:
                            speedups += 1
        frontier = new_frontier

print(f"There are {speedups} cheats that save at least {MIN_SAVE} picoseconds.")
