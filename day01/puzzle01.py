with open('./input-puzzle01.txt', 'r') as input_data:
    result = 0
    for line in input_data.readlines():
        result += int(line)

    print(result)
