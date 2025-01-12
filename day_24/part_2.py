from pathlib import Path
from parse import parse
from collections import defaultdict

CURRENT_FOLDER = Path(__file__).absolute().parent
INPUT_FILE = CURRENT_FOLDER / "input.txt"
CORRECTED_INPUT_FILE = CURRENT_FOLDER / "corrected_input.txt"
DEMO_INPUT_FILE = CURRENT_FOLDER / "demo_input.txt"
DEMO_INPUT_2_FILE = CURRENT_FOLDER / "demo_input_2.txt"

with open(INPUT_FILE) as f:
    wires_block, gates_block = f.read().split("\n\n")

computed = {}
for wire in wires_block.splitlines():
    name, value = parse("{}: {:d}", wire)
    computed[name] = value

gates = set()
inputs = defaultdict(set)
outputs = defaultdict(set)
for gate_line in gates_block.splitlines():
    first, operation, second, output = parse("{} {} {} -> {}", gate_line)
    first, second = sorted((first, second))
    gate = first, operation, second, output
    gates.add(gate)
    inputs[first].add(gate)
    inputs[second].add(gate)
    outputs[output].add(gate)

input_gates = defaultdict(dict)
for first, operation, second, output in gates:
    if first.startswith("x") or second.startswith("x"):
        input_gates[int(first[1:])][operation] = (first, operation, second, output)

# For every full adder, we should have
# Sum = (X XOR Y) XOR Cin
# Cout = (X AND Y) OR (Cin AND (X XOR Y))
values = {}
for gate_number, subdict in sorted(input_gates.items()):
    print(f"GATE {gate_number}")
    for operation, gate in sorted(subdict.items(), reverse=True):
        first, operation, second, output = gate
        values[output] = f"{first} {operation} {second}"
        for fir, ope, sec, out in inputs[output]:
            if fir in values:
                fir = f"({values[fir]})"
            if sec in values:
                sec = f"({values[sec]})"
            print(f"{out} = {fir} {ope} {sec}")
        print()
    print()

print(",".join(sorted(("z09", "z05", "z30", "nbf", "gbf", "hdt", "mht", "jgt"))))
