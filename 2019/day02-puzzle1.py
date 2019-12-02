filename = 'day02-input.txt'

with open(filename, 'r') as input_file:
    intcode_program = [int(_) for _ in input_file.read().split(',')]

    intcode_program[1] = 12
    intcode_program[2] = 2

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

    print(intcode_program[0])
