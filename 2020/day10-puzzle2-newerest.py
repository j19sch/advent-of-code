import itertools
from pprint import pprint

def open_file(in_file):
	with open(f'./{in_file}', 'r') as input_file:
		input_list = input_file.readlines()
	return [int(_.rstrip()) for _ in input_list]


# adapters = open_file('day10-example.txt')  # 8
# adapters = open_file('day10-example2.txt')  # 10368 -> 19208
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

# print(f'the dict:\n{the_dict}')

# pprint(sorted(the_dict.items(), key=lambda t: t[0]))

nodes = []

for keeh in sorted(the_dict.keys()):  # sorted not needed
	# print(keeh)
	jump = False
	if len(the_dict[keeh]) > 1:
		jump = True
	elif keeh - 1 in the_dict.keys():
		for _ in the_dict[keeh - 1]:
			if _ > keeh:
				# print("jump")
				jump = True
	elif keeh - 2 in the_dict.keys():
		for _ in the_dict[keeh - 2]:
			if _ >	 keeh:
				# print("jump")
				jump = True
	elif keeh - 3 in the_dict.keys():
		for _ in the_dict[keeh - 3]:
			if _ >	 keeh:
				# print("jump")
				jump = True

	if jump is False:
		nodes.append(keeh)

# print(f'nodes: {nodes}')

broken_up = []
part = {}

for keeh in sorted(the_dict.keys()):
	if keeh not in nodes:
		part[keeh] = the_dict[keeh]
	else:
		part[keeh] = the_dict[keeh]
		broken_up.append(part)
		part = {}

# pprint(broken_up)


def find_next_nodes(node, solutions_counter, dict_part):
	# print(f'dict_part: {dict_part}')
	# print(f'node: {node}')

	if node == device_max:
		return 1

	for item in dict_part[node]:
		if item == max(the_dict_part.values())[0]:
			# print('solution')
			solutions_counter += 1
			# print(f'solutions: {solutions_counter}')
		else:
			solutions_counter = find_next_nodes(item, solutions_counter, dict_part)

	return solutions_counter


total = 1

for the_dict_part in broken_up:
	counter = 0
	counter = find_next_nodes(min(the_dict_part.keys()), counter, the_dict_part)
	total *= counter
	# print(counter)

print(total)