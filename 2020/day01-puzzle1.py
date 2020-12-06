example = [1721, 979, 366, 299, 675, 1456]


def open_file():
	with open('./day01-input.txt', 'r') as input_file:
		input_list = input_file.readlines()
	return [int(_) for _ in input_list]



def find_nums_that_sum_to_2020(the_nums):
	for item in the_nums:
		needed = 2020 - item
		if needed in the_nums:
			break
	return item, needed



one, two = find_nums_that_sum_to_2020(example)
print(one, two)
print(one * two)

nums = open_file()
one, two = find_nums_that_sum_to_2020(nums)
print(one, two)
print(one * two)