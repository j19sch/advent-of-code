examples = [
    [1, 0, 0, 0, 99], #becomes 2,0,0,0,99 (1 + 1 = 2).
    [2, 3, 0, 3, 99], #becomes 2,3,0,6,99 (3 * 2 = 6).
    [2, 4, 4, 5, 99, 0], #becomes 2,4,4,5,99,9801 (99 * 99 = 9801).
    [1, 1, 1, 4, 99, 5, 6, 0, 99] #becomes 30,1,1,4,2,5,6,0,99.
]

for example in examples:
    read_pos = 0

    while True:
        opcode = example[read_pos]
        if opcode == 99:
            break

        input_a = example[example[read_pos + 1]]
        input_b = example[example[read_pos + 2]]
        output_loc = example[read_pos + 3]

        if opcode == 1:
            result = input_a + input_b
            example[output_loc] = result
            read_pos += 4
        elif opcode == 2:
            result = input_a * input_b
            example[output_loc] = result
            read_pos += 4

    print(example)
