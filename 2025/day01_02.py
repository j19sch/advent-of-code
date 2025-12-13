example_start = 50

example = ["L68", "L30", "R48", "L5", "R60", "L55", "L1", "L99", "R14", "L82"]


def open_file():
    with open("./day01-input.txt", "r") as input_file:
        input_list = input_file.readlines()
    return input_list


def split_input(input):
    return [input[0], int(input[1:])]


def how_many_crosses(position, direction, number):
    if direction == "R":
        if (position + number) % 100 == 0:
            crosses = (
                ((position + number) // 100 - 1) if (position + number) > 100 else 0
            )
        else:
            crosses = (position + number) // 100
        return crosses
    else:
        if position == 0:
            crosses = number // 100 if number > 100 else 0
        else:
            crosses = number // 100
            if (number % 100) > position:
                crosses = crosses + 1

        return crosses


if __name__ == "__main__":
    position = example_start
    count_zero = 0

    # input = example
    input = open_file()

    for rotation in input:
        [direction, number] = split_input(rotation)
        crosses = how_many_crosses(position, direction, number)
        if direction == "L":
            position = position - number
        else:
            position = position + number

        position = position % 100
        if position == 0:
            count_zero = count_zero + 1

        count_zero = count_zero + crosses

    print(count_zero)

# 7223 too high
