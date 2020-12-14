def open_file(in_file):
	with open(f'./{in_file}', 'r') as input_file:
		input_list = input_file.readlines()
	return [_.rstrip() for _ in input_list]


# instr_file = open_file('day08-example.txt')
instr_file = open_file('day08-input.txt')
# print(instr_file)


def exec_instruction(idx, acc, vis):
	op, arg = instr_file[idx].split(' ')
	arg = int(arg[1:]) if arg.startswith("+") else int(arg[1:]) * -1
	# print(op, arg)

	vis.append(idx)

	if op == 'acc':
		acc += arg
		new_idx = idx + 1
	elif op == 'jmp':
		new_idx = idx + arg
	elif op == 'nop':
		new_idx = idx + 1

	# print(idx, acc, new_idx)

	if new_idx not in vis:
		acc = exec_instruction(new_idx, acc, vis)		

	return acc


accumulator = 0
index = 0
visited = []

accumulator = exec_instruction(index, accumulator, visited)
print(accumulator)