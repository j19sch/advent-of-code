import itertools

# lessons learned:
# - tuples are not sets
# - print() is very expensive

with open('./day01-input.txt', 'r') as input_data:
    result = 0
    seen_results = {result}

    for line in itertools.cycle(input_data.readlines()):
        result += int(line)
        if result in seen_results:
            first_seen_before = result
            break
        else:
            seen_results.add(result)

    print(f'==> the answer: {first_seen_before}')