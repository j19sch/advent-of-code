def open_file(in_file):
	with open(f'./{in_file}', 'r') as input_file:
		input_list = input_file.readlines()
	return [_.rstrip() for _ in input_list]


# instructions_file = open_file('day08-example.txt')
# instructions_file = open_file('day08-example-fixed.txt')
instructions_file = open_file('day08-input.txt')


# changing exactly one jmp (to nop) or nop (to jmp)

def exec_instruction(idx, acc, vis, instr_file):
	try:
		instr_file[idx]
	except IndexError:
		return acc

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

	acc = exec_instruction(new_idx, acc, vis, instr_file)

	# try:
	# 	acc = exec_instruction(new_idx, acc, vis)
	# except RecursionError:
	# 	print("recursion error")
	# 	pass

	return acc

def run_instructions(instructions):
	accumulator = 0
	index = 0
	visited = []

	try:
		accumulator = exec_instruction(index, accumulator, visited, instructions)
	except RecursionError:
		# print("recursion error")
		pass
	else:
		# print(accumulator)
		return accumulator

	# accumulator = exec_instruction(index, accumulator, visited)

	# return accumulator



idx_of_nops_and_jumps = []

for index, instr in enumerate(instructions_file):
	if instr[:3] in ['nop', 'jmp']:
		idx_of_nops_and_jumps.append(index)

# print(idx_of_nops_and_jumps)

for _ in idx_of_nops_and_jumps:
	fixed_instructions_file = instructions_file.copy()
	if instructions_file[_][:3] == 'nop':
		fixed_instructions_file[_] = f'jmp{instructions_file[_][3:]}'
	else:
		fixed_instructions_file[_] = f'nop{instructions_file[_][3:]}'

	# print(fixed_instructions_file)
	accumulator = run_instructions(fixed_instructions_file)
	if accumulator is not None:
		print(accumulator)
		break