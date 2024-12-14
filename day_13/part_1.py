from pathlib import Path
from parse import parse
import numpy as np

CURRENT_FOLDER = Path(__file__).absolute().parent
INPUT_FILE = CURRENT_FOLDER / "input.txt"
DEMO_INPUT_FILE = CURRENT_FOLDER / "demo_input.txt"

tokens = 0
with open(INPUT_FILE) as f:
    for block in f.read().split("\n\n"):
        button_a, button_b, prize = block.split("\n")
        x_a, y_a = parse("Button A: X+{:d}, Y+{:d}", button_a)
        x_b, y_b = parse("Button B: X+{:d}, Y+{:d}", button_b)
        M = np.array([[x_a, x_b], [y_a, y_b]])
        x_c, y_c = parse("Prize: X={:d}, Y={:d}", prize)
        c = np.array([x_c, y_c])
        presses = np.linalg.solve(M, c)

        # Verify the result, there might be floating point precision errors
        presses = np.round(presses).astype(int)
        if np.all(np.dot(M, presses) == c):
            tokens += np.dot(presses, [3, 1])

print(tokens)
