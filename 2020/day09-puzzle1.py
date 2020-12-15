from itertools import combinations

def open_file(in_file):
	with open(f'./{in_file}', 'r') as input_file:
		input_list = input_file.readlines()
	return [int(_.rstrip()) for _ in input_list]

# numbers_file = open_file('day09-example.txt')
# len_preamble = 5

numbers_file = open_file('day09-input.txt')
len_preamble = 25


for index, number in enumerate(numbers_file[len_preamble:]):
	preamble = numbers_file[index:len_preamble + index]
	the_sums = [sum(combination) for combination in combinations(preamble, r=2)]

	if number not in the_sums:
		print(number)
		break
