from pathlib import Path
from parse import parse
from operator import and_, or_, xor

CURRENT_FOLDER = Path(__file__).absolute().parent
INPUT_FILE = CURRENT_FOLDER / "input.txt"
DEMO_INPUT_FILE = CURRENT_FOLDER / "demo_input.txt"
DEMO_INPUT_2_FILE = CURRENT_FOLDER / "demo_input_2.txt"
OPERATIONS = {"AND": and_, "OR": or_, "XOR": xor}

with open(INPUT_FILE) as f:
    wires_block, gates_block = f.read().split("\n\n")

computed = {}
for wire in wires_block.splitlines():
    name, value = parse("{}: {:d}", wire)
    computed[name] = value

open_gates = set()
for gate in gates_block.splitlines():
    first, operation, second, output = parse("{} {} {} -> {}", gate)
    open_gates.add((first, second, OPERATIONS[operation], output))

while open_gates:
    for gate in open_gates.copy():
        first, second, operation, output = gate
        if first in computed and second in computed:
            computed[output] = operation(computed[first], computed[second])
            open_gates.remove(gate)

output = 0
for bit, value in computed.items():
    if bit.startswith("z"):
        output += (1 << int(bit[1:])) * value
print(output)
