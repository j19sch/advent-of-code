import re

def open_file(in_file):
	with open(f'./{in_file}', 'r') as input_file:
		input_list = input_file.readlines()
	return [_.rstrip() for _ in input_list]


required_fields = ['byr', 'iyr', 'eyr', 'hgt','hcl', 'ecl', 'pid']
optional_fields = ['cid']


def return_valid_passports_mandatory_fields(the_passports):
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
	return valid_passports


def return_valid_passports_field_validations(the_passports):
	valid_passports = []

	for _ in the_passports:
		if int(_['byr']) < 1920 or int(_['byr']) > 2002:
			continue

		if int(_['iyr']) < 2010 or int(_['iyr']) > 2020:
			continue

		if int(_['eyr']) < 2020 or int(_['eyr']) > 2030:
			continue

		if _['hgt'].endswith('cm'):
			if int(_['hgt'][:-2]) < 150 or int(_['hgt'][:-2]) > 193:
				continue
		elif _['hgt'].endswith('in'):
			if int(_['hgt'][:-2]) < 59 or int(_['hgt'][:-2]) > 76:
				continue
		else:
			continue

		if re.compile(r"^#[a-z0-9]{6}$").match(_['hcl']) is None:
			continue

		if _['ecl'] not in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']:
			continue

		if re.compile(r"^[0-9]{9}$").match(_['pid']) is None:
			continue

		valid_passports.append(_)

	return valid_passports

puzzle_file = open_file('day04-input.txt')
valid_passports_step_1 = return_valid_passports_mandatory_fields(puzzle_file)
print(len(valid_passports_step_1))

valid_passports_step_2 = return_valid_passports_field_validations(valid_passports_step_1)
print(len(valid_passports_step_2))

# not 11
# not 187