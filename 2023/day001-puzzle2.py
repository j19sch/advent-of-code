import re

def open_file():
	with open('./day01-input.txt', 'r') as input_file:
		input_list = input_file.readlines()
	return [_.rstrip() for _ in input_list]


example_input_1 = [
	"1abc2",
	"pqr3stu8vwx",
	"a1b2c3d4e5f",
	"treb7uchet"
]

example_input_2 = [
"two1nine",
"eightwothree",
"abcone2threexyz",
"xtwone3four",
"4nineeightseven2",
"zoneight234",
"7pqrstsixteen",
"sgeightwo3"
]

mapping = {
	"zero": "0",
	"one" : '1',
	"two": "2",
	"three": "3",
	"four": "4",
	"five": "5",
	"six": "6",
	"seven": "7",
	"eight": "8",
	"nine": "9"
}

# the_input = example_input_1
# the_input = example_input_2
the_input = open_file()


the_numbers = []

for inputs in the_input:
	pattern = r'(?=(\d|zero|one|two|three|four|five|six|seven|eight|nine))'

	regex_result = re.findall(pattern, inputs)
	print(regex_result)
	
	first = regex_result[0]
	if first in mapping.keys():
		first = mapping[first]

	last = regex_result[-1]
	if last in mapping.keys():
		last = mapping[last]

	first_last = first + last
	number = int(first_last)
	the_numbers.append(number)

result = sum(the_numbers)
print(result)

# 54412 too low
# probably an overal in two letter ones at the end
# sgeightwo3 -> ['eight', '3']