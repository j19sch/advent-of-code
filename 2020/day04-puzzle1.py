def open_file(in_file):
	with open(f'./{in_file}', 'r') as input_file:
		input_list = input_file.readlines()
	return [_.rstrip() for _ in input_list]


required_fields = ['byr', 'iyr', 'eyr', 'hgt','hcl', 'ecl', 'pid']
optional_fields = ['cid']


def count_valid_passports(the_passports):
	passports = []
	index = 0

	for _ in the_passports:
		try:
			passports[index]
		except IndexError:
			passports.append({})

		if _ != "":
			items = _.split(" ")
			for item in items:
				split = item.split(":", 1)
				passports[index][split[0]] = split[1]
		else:
			index += 1

	# print(passports)

	valid_passports = [passport for passport in passports if all(_ in passport.keys() for _ in required_fields)]
	return len(valid_passports)

example_file = open_file('day04-example.txt')
example_count = count_valid_passports(example_file)
print(example_count)

puzzle_file = open_file('day04-input.txt')
puzzle_count = count_valid_passports(puzzle_file)
print(puzzle_count)