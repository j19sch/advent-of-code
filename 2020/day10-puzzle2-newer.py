
def open_file(in_file):
	with open(f'./{in_file}', 'r') as input_file:
		input_list = input_file.readlines()
	return [int(_.rstrip()) for _ in input_list]


# adapters = open_file('day10-example.txt')
# adapters = open_file('day10-example2.txt')
adapters = open_file('day10-input.txt')


device_max = max(adapters) + 3
adapters.append(device_max)  # in or out?

charging_outlet = 0
adapters.append(charging_outlet)  # in or out?

the_dict = {k: [] for k in adapters}

for k,v in the_dict.items():
	if k + 1 in adapters:
		v.append(k+1)
	if k + 2 in adapters:
		v.append(k+2)
	if k + 3 in adapters:
		v.append(k+3)

print(sorted(the_dict))


def find_next_nodes(node, solutions_counter):
	# print(f'node: {node}')
	for item in the_dict[node]:
		if item == device_max:
			# print('solution')
			solutions_counter += 1
			print(f'solutions: {solutions_counter}')
		else:
			solutions_counter = find_next_nodes(item, solutions_counter)

	return solutions_counter


counter = 0
pointer = 0

counter = find_next_nodes(pointer, counter)
print(counter)

# print(the_dict[pointer])

# for item in the_dict[pointer]:
# 	print(the_dict[item])