example = [1721, 979, 366, 299, 675, 1456]

# 979, 366, and 675
# Multiplying them together produces the answer, 241861950.


def open_file():
	with open('./day01-input.txt', 'r') as input_file:
		input_list = input_file.readlines()
	return [int(_) for _ in input_list]

def find_three_numbers_that_sum_to_2020(the_nums):
	for index, a_num in enumerate(the_nums):
		print(index, a_num)

		for _ in range(index + 1, len(the_nums) - 1):
			next_up = the_nums[_] # IndexError if a_num is last item
			sum_1_2 = a_num + next_up
			needed = 2020 - sum_1_2
			if needed in the_nums[_ + 1:]:
				return a_num, next_up, needed
				# break

	# return a_num, next_up, needed


one, two, three = find_three_numbers_that_sum_to_2020(example)
print(one, two, three)
print(one * two * three)


nums = open_file()
one, two, three = find_three_numbers_that_sum_to_2020(nums)
print(one, two, three)
print(one * two * three)