def open_file():
	with open('./day01-input.txt', 'r') as input_file:
		input_list = input_file.readlines()
	return [_.rstrip() for _ in input_list]


example_input = [
	"1abc2",
	"pqr3stu8vwx",
	"a1b2c3d4e5f",
	"treb7uchet"
]


# the_input = example_input

the_input = open_file()


the_numbers = []

for inputs in the_input:
	filtered = [_ for _ in inputs if _ in ["0","1","2","3","4","5","6","7","8","9"]]
	first_last = filtered[0] + filtered[-1]
	number = int(first_last)
	the_numbers.append(number)


result = sum(the_numbers)
print(result)
