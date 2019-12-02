with open('./day01-input.txt', 'r') as input_data:
    result = 0
    for line in input_data.readlines():
        result += int(line)

    print(result)
