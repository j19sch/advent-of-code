from operator import index


def get_largest_joltage(series):
    # series_dict = {index: value for index,value in enumerate(series)}
    series = [_ for _ in series]
    largest = max(series)
    index_largest = series.index(largest)

    if index_largest != (len(series) - 1):
        second_largest = max(series[index_largest + 1 :])
        return int(f"{largest}{second_largest}")
    else:
        print("here")
        second_largest = max(series[:index_largest])
        return int(f"{second_largest}{largest}")


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
        total_output = total_output + get_largest_joltage(bank)

    print(total_output)

# 16478 too low
