import re

example = [
	"1-3 a: abcde",
	"1-3 b: cdefg",
	"2-9 c: ccccccccc"
]  # 2 are valid


def open_file():
	with open('./day02-input.txt', 'r') as input_file:
		input_list = input_file.readlines()
	return input_list


def parse_input_line(line):
	m = re.match("(\d+)-(\d+) (\w): (\w+)", line)
	return m.groups()



def return_number_of_valid_passwords(passwords):
	valid = 0

	for ex in passwords:
		pos1, pos2, letter, password = parse_input_line(ex)
		pos1 = int(pos1)
		pos2 = int(pos2)

		first = password[pos1 - 1] == letter
		second = password[pos2 - 1] == letter
		
		if first ^ second:
			valid += 1

	return valid


example_result = return_number_of_valid_passwords(example)
print(example_result)

password_list = open_file()
input_result = return_number_of_valid_passwords(password_list)
print(input_result)
