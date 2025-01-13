from pathlib import Path

CURRENT_FOLDER = Path(__file__).absolute().parent
INPUT_FILE = CURRENT_FOLDER / "input.txt"
DEMO_INPUT_7_FILE = CURRENT_FOLDER / "demo_input_7.txt"

with open(INPUT_FILE) as f:
    registers_block, program_line = f.read().split("\n\n")

program = [int(op) for op in program_line.split()[1].split(",")]


def mix(value):
    registers = {"A": value, "B": 0, "C": 0}
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
    return outputs


queue = set(range(8))
for n in range(1, len(program) + 1):
    new_queue = set()
    for value in queue:
        result = mix(value)
        # Compare the `n` last digits of the program with the result
        if result[-n:] == program[-n:]:
            # If we found a valid start value, directly add it to the queue
            if n == len(program):
                new_queue.add(value)
            else:
                for i in range(8):
                    new_queue.add((value << 3) + i)
    queue = new_queue

result = min(queue)
# Sanity check
assert mix(result) == program
print(result)
