filename = 'day05-input.txt'


def get_input_parameters(number_of_inputs, intcode_program, read_pos, mode_params):
    input_param_locs = tuple()
    for _ in range(1, number_of_inputs + 1):
        input = intcode_program[read_pos + _] if mode_params[_ - 1] == 0 else read_pos + _
        input_param_locs = (*input_param_locs, input)

    return input_param_locs


def parse_instruction(intcode_program,read_pos):
    instruction = str(intcode_program[read_pos])

    # print(f"step {step}: {instruction}")

    opcode = int(instruction[-2:])
    mode_param_1 = int(instruction[-3:-2] if instruction[-3:-2] != "" else 0)
    mode_param_2 = int(instruction[-4:-3] if instruction[-4:-3] != "" else 0)
    mode_param_3 = int(instruction[-5:-4] if instruction[-5:-4] != "" else 0)
    mode_params = [mode_param_1, mode_param_2, mode_param_3]

    return opcode, mode_params

with open(filename, 'r') as input_file:
    intcode_program = [int(_) for _ in input_file.read().split(',')]

    read_pos = 0

    input_instruction = 5
    step = 0

    while True:
        step += 1

        opcode, mode_params = parse_instruction(intcode_program,read_pos)

        if opcode == 99:
            break

        if opcode == 1:  # addition
            input_a_loc, input_b_loc, output_loc = get_input_parameters(3, intcode_program, read_pos, mode_params)
            result = intcode_program[input_a_loc] + intcode_program[input_b_loc]
            intcode_program[output_loc] = result
            read_pos += 4
        elif opcode == 2:  # multiplication
            input_a_loc, input_b_loc, output_loc = get_input_parameters(3, intcode_program, read_pos, mode_params)
            result = intcode_program[input_a_loc] * intcode_program[input_b_loc]
            intcode_program[output_loc] = result
            read_pos += 4
        elif opcode == 3:  # input
            input_instruction_loc, = get_input_parameters(1, intcode_program, read_pos, mode_params)
            intcode_program[input_instruction_loc] = input_instruction
            read_pos += 2
        elif opcode == 4:  # output
            output_loc, = get_input_parameters(1, intcode_program, read_pos, mode_params)
            output = intcode_program[output_loc]
            print(f"output: {output}")
            read_pos += 2
        elif opcode == 5:  # jump-if-true
            check_loc, value_loc = get_input_parameters(2, intcode_program, read_pos, mode_params)
            if intcode_program[check_loc] != 0:
                read_pos = intcode_program[value_loc]
            else:
                read_pos += 3
        elif opcode == 6:  # jump-if-false
            check_loc, value_loc = get_input_parameters(2, intcode_program, read_pos, mode_params)
            if intcode_program[check_loc] == 0:
                read_pos = intcode_program[value_loc]
            else:
                read_pos += 3
        elif opcode == 7:  # less than
            val1_loc, val2_loc, output_loc = get_input_parameters(3, intcode_program, read_pos, mode_params)
            intcode_program[output_loc] = 1 if intcode_program[val1_loc] < intcode_program[val2_loc] else 0
            read_pos += 4
        elif opcode == 8:  # equals
            val1_loc, val2_loc, output_loc = get_input_parameters(3, intcode_program, read_pos, mode_params)
            intcode_program[output_loc] = 1 if intcode_program[val1_loc] == intcode_program[val2_loc] else 0
            read_pos += 4
