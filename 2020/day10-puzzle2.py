import json

def open_file(in_file):
	with open(f'./{in_file}', 'r') as input_file:
		input_list = input_file.readlines()
	return [int(_.rstrip()) for _ in input_list]


adapters = open_file('day10-example2.txt')
# print(sorted(adapters))

adapters = open_file('day10-input.txt')

device_max = max(adapters) + 3
adapters.append(device_max)
# print(device_max)

charging_outlet = 0

the_tree = {charging_outlet: None}


def build_tree(node, new_number, solution_counter):
	# print()
	# print(f'tree: {the_tree}')
	# print(f'node: {node}, new_number: {new_number}')
	if node is None:
		pass
	else:
		for node_key in node.keys():

			if new_number > node_key and new_number < node_key + 4:
				if node[node_key] is None:
					node[node_key] = {new_number: None}
				else:
					node[node_key].update({new_number: None})

				if new_number == device_max:
					solution_counter += 1  # always 0 + 1

			solution_counter = build_tree(node[node_key], new_number, solution_counter)

	return solution_counter

for adapter in sorted(adapters):
	solution_counter = build_tree(the_tree, adapter, 0)


# print(json.dumps(the_tree, sort_keys=True, indent=4))
print(solution_counter)