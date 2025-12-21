example = "11-22,95-115,998-1012,1188511880-1188511890,222220-222224, 1698522-1698528,446443-446449,38593856-38593862,565653-565659, 824824821-824824827,2121212118-2121212124"

# performance is lacking (more sets, fewer lists), but it works


def open_file():
    with open("./day02-input.txt", "r") as input_file:
        input = input_file.readlines()
    return input


def is_invalid(id):
    half_length = int(len(id) / 2)
    if id[:half_length] == id[half_length:]:
        return True
    else:
        return False


if __name__ == "__main__":
    invalid_ids = []

    # input = example
    input = open_file()[0]
    id_ranges = [split.split("-") for split in [_ for _ in input.split(",")]]

    for id_range in id_ranges:
        for id in range(int(id_range[0]), int(id_range[-1]) + 1):
            if is_invalid(str(id)) is True:
                invalid_ids.append(id)

    print(sum(invalid_ids))
