from itertools import product

for combination in product(range(0, 100), repeat=2):
    filename = 'day02-input.txt'

    with open(filename, 'r') as input_file:
        intcode_program = [int(_) for _ in input_file.read().split(',')]

        intcode_program[1] = combination[0]
        intcode_program[2] = combination[1]

        read_pos = 0

        while True:
            opcode = intcode_program[read_pos]
            if opcode == 99:
                break

            input_a = intcode_program[intcode_program[read_pos + 1]]
            input_b = intcode_program[intcode_program[read_pos + 2]]
            output_loc = intcode_program[read_pos + 3]

            if opcode == 1:
                result = input_a + input_b
                intcode_program[output_loc] = result
                read_pos += 4
            elif opcode == 2:
                result = input_a * input_b
                intcode_program[output_loc] = result
                read_pos += 4
            else:
                print(f"Error for {100 * combination[0] + combination[1]}")
                break

    if intcode_program[0] == 19690720:
        print(f"answer: {100 * combination[0] + combination[1]}")
        break
