with open('./day01-input.txt', 'r') as input_data:
    result = sum([int(_) for _ in input_data.readlines()])
    print(result)
