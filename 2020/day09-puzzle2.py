from itertools import accumulate


def open_file(in_file):
	with open(f'./{in_file}', 'r') as input_file:
		input_list = input_file.readlines()
	return [int(_.rstrip()) for _ in input_list]


invalid_number = 133015568

numbers_file = open_file('day09-input.txt')

start = 0
positions = 0

for index in range(0, len(numbers_file) - 1):
	loop_counter = 0
	for result in accumulate(numbers_file[index:]):
		if result == invalid_number and loop_counter != 0:
			start = index
			positions = loop_counter
			break
		elif result > invalid_number:
			break
		else:
			loop_counter += 1


print(start, positions)
the_range = numbers_file[start:start+positions+1]
print(sum(the_range))
print(min(the_range) + max(the_range))
