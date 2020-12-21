from itertools import combinations


# NOTE: this takes forever to run on anything bigger than the first example

def open_file(in_file):
	with open(f'./{in_file}', 'r') as input_file:
		input_list = input_file.readlines()
	return [int(_.rstrip()) for _ in input_list]


# adapters = open_file('day10-example.txt')
adapters = open_file('day10-example2.txt')
# adapters = open_file('day10-input.txt')
# print(sorted(adapters))


device_max = max(adapters) + 3
charging_outlet = 0

solution_counter = 0

# print(list(combinations(adapters, r=1)))


for _ in range(1, len(adapters) + 1):
	print(f'number of combinations is {_}')
	for combination in combinations(adapters, r=_):
		combination += (device_max,)
		combination = sorted(combination)

		prev = charging_outlet

		for adapter in combination:
			diff = adapter - prev
			if diff not in [1,2,3]:
				break
			else:
				prev = adapter
		else:
			print(f'solution for {combination}')
			solution_counter += 1


print(solution_counter)