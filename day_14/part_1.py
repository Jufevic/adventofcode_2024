from pathlib import Path
from parse import parse

CURRENT_FOLDER = Path(__file__).absolute().parent
INPUT_FILE = CURRENT_FOLDER / "input.txt"
DEMO_INPUT_FILE = CURRENT_FOLDER / "demo_input.txt"
WIDTH = 101
HEIGHT = 103

upper_left = 0
upper_right = 0
lower_left = 0
lower_right = 0
with open(INPUT_FILE) as f:
    for line in f.read().splitlines():
        px, py, vx, vy = parse("p={:d},{:d} v={:d},{:d}", line)
        x = (px + vx * 100) % WIDTH
        y = (py + vy * 100) % HEIGHT
        if 0 <= x < WIDTH // 2 and 0 <= y < HEIGHT // 2:
            upper_left += 1
        elif x > WIDTH // 2 and 0 <= y < HEIGHT // 2:
            upper_right += 1
        elif 0 <= x < WIDTH // 2 and y > HEIGHT // 2:
            lower_left += 1
        elif x > WIDTH // 2 and y > HEIGHT // 2:
            lower_right += 1

print(upper_left * upper_right * lower_left * lower_right)
