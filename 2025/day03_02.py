def get_more_largest_joltage(series):
    length_joltage = 12
    joltage = ""

    series = [_ for _ in series]

    while length_joltage > 0:
        largest = max(series[: (len(series) - length_joltage + 1)])
        index_largest = series.index(largest)
        series = series[index_largest + 1 :]
        joltage += largest
        length_joltage -= 1

    return int(joltage)


def open_file():
    with open("./day03-input.txt", "r") as input_file:
        input = input_file.read().splitlines()  # not readlines() because \n
    return input


example = [
    "987654321111111",
    "811111111111119",
    "234234234234278",
    "818181911112111",
]

if __name__ == "__main__":
    # input = example
    input = open_file()

    total_output = 0

    for bank in input:
        total_output = total_output + get_more_largest_joltage(bank)

    print(total_output)
