from pathlib import Path
from parse import parse

CURRENT_FOLDER = Path(__file__).absolute().parent
INPUT_FILE = CURRENT_FOLDER / "input.txt"
DEMO_INPUT_FILE = CURRENT_FOLDER / "demo_input.txt"
DEMO_INPUT_2_FILE = CURRENT_FOLDER / "demo_input_2.txt"
DEMO_INPUT_3_FILE = CURRENT_FOLDER / "demo_input_3.txt"
DEMO_INPUT_4_FILE = CURRENT_FOLDER / "demo_input_4.txt"
DEMO_INPUT_5_FILE = CURRENT_FOLDER / "demo_input_5.txt"
DEMO_INPUT_6_FILE = CURRENT_FOLDER / "demo_input_6.txt"

with open(INPUT_FILE) as f:
    registers_block, program_line = f.read().split("\n\n")

registers = {}
for line in registers_block.splitlines():
    register, value = parse("Register {}: {:d}", line)
    registers[register] = value

program = [int(op) for op in program_line.split()[1].split(",")]
position = 0
outputs = []

# Continue the program until the instruction position is in the program
while 0 <= position < len(program):
    opcode = program[position]
    operand = program[position + 1]
    literal = operand
    if operand == 4:
        operand = registers["A"]
    elif operand == 5:
        operand = registers["B"]
    elif operand == 6:
        operand = registers["C"]
    match opcode:
        case 0:
            registers["A"] = registers["A"] >> operand
            position += 2
        case 1:
            registers["B"] = registers["B"] ^ literal
            position += 2
        case 2:
            registers["B"] = operand % 8
            position += 2
        case 3:
            if registers["A"] != 0:
                position = literal
            else:
                position += 2
        case 4:
            registers["B"] = registers["B"] ^ registers["C"]
            position += 2
        case 5:
            outputs.append(operand % 8)
            position += 2
        case 6:
            registers["B"] = registers["A"] >> operand
            position += 2
        case 7:
            registers["C"] = registers["A"] >> operand
            position += 2

print(f"{registers=}")
print(",".join(map(str, outputs)))
