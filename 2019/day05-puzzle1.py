filename = 'day05-input.txt'

with open(filename, 'r') as input_file:
    intcode_program = [int(_) for _ in input_file.read().split(',')]
    read_pos = 0

    input_instruction = 1
    step = 0

    while True:
        step += 1

        instruction = str(intcode_program[read_pos])

        # print(f"step {step}: {instruction}")

        opcode = int(instruction[-2:])
        mode_param_1 = int(instruction[-3:-2] if instruction[-3:-2] != "" else 0)
        mode_param_2 = int(instruction[-4:-3] if instruction[-4:-3] != "" else 0)
        mode_param_3 = int(instruction[-5:-3] if instruction[-5:-4] != "" else 0)

        if opcode == 99:
            break

        if opcode == 1:
            input_a = intcode_program[intcode_program[read_pos + 1]] if mode_param_1 == 0 else intcode_program[read_pos + 1]
            input_b = intcode_program[intcode_program[read_pos + 2]] if mode_param_2 == 0 else intcode_program[read_pos + 2]
            result = input_a + input_b
            output_loc = intcode_program[read_pos + 3]  # output always in position mode
            intcode_program[output_loc] = result
            read_pos += 4
        elif opcode == 2:
            input_a = intcode_program[intcode_program[read_pos + 1]] if mode_param_1 == 0 else intcode_program[read_pos + 1]
            input_b = intcode_program[intcode_program[read_pos + 2]] if mode_param_2 == 0 else intcode_program[read_pos + 2]
            result = input_a * input_b
            output_loc = intcode_program[read_pos + 3]  # output always in position mode
            intcode_program[output_loc] = result
            read_pos += 4
        elif opcode == 3:
            intcode_program[intcode_program[read_pos + 1]] = input_instruction
            read_pos += 2
        elif opcode == 4:
            output = intcode_program[intcode_program[read_pos + 1]] if mode_param_1 == 0 else intcode_program[read_pos + 1]
            print(f"output: {output}")
            read_pos += 2
