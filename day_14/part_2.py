from pathlib import Path
from parse import parse
from matplotlib import pyplot as plt
import numpy as np

CURRENT_FOLDER = Path(__file__).absolute().parent
INPUT_FILE = CURRENT_FOLDER / "input.txt"
DEMO_INPUT_FILE = CURRENT_FOLDER / "demo_input.txt"
WIDTH = 101
HEIGHT = 103

xs = []
ys = []
vxs = []
vys = []
with open(INPUT_FILE) as f:
    for line in f.read().splitlines():
        px, py, vx, vy = parse("p={:d},{:d} v={:d},{:d}", line)
        xs.append(px)
        ys.append(py)
        vxs.append(vx)
        vys.append(vy)

xs = np.array(xs)
ys = np.array(ys)
vxs = np.array(vxs)
vys = np.array(vys)

for step in range(10000):
    grid = np.zeros((HEIGHT, WIDTH))
    grid[ys, xs] += 1
    print(f"{step=}\r", end="")
    fig, ax = plt.subplots()
    ax.imshow(grid)
    ax.set_title(f"{step=}")
    ax.xaxis.set_visible(False)
    ax.yaxis.set_visible(False)
    fig.savefig(CURRENT_FOLDER / f"{step}.png")
    plt.close()

    # Prepare for next step
    xs = (xs + vxs) % WIDTH
    ys = (ys + vys) % HEIGHT
