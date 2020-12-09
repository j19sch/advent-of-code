from math import ceil, floor


def open_file(in_file):
	with open(f'./{in_file}', 'r') as input_file:
		input_list = input_file.readlines()
	return [_.rstrip() for _ in input_list]


def determine_row(bp):
	bottom = 0
	top = 127

	for _ in bp[:7]:
		middle = (bottom + top ) / 2

		if _ == "F":
			top = floor(middle)
		elif _ == "B":
			bottom = ceil(middle)

	return bottom


def determine_column(bp):
	bottom = 0
	top = 7

	for _ in bp[7:]:
		middle = (bottom + top ) / 2

		if _ == "L":
			top = floor(middle)
		elif _ == "R":
			bottom = ceil(middle)

	return bottom

def calculate_seat_id(row, column):
	row = determine_row(boarding_pass)
	column = determine_column(boarding_pass)
	seat_id = (row * 8) + column
	return seat_id


boarding_passes = open_file('day05-input.txt')

seat_ids = []

for boarding_pass in boarding_passes:
	row = determine_row(boarding_pass)
	column = determine_column(boarding_pass)
	seat_id = calculate_seat_id(row, column)
	seat_ids.append(seat_id)


seat_ids.sort()


for index, seat in enumerate(seat_ids):
	if seat_ids[index + 1] != seat + 1:
		print(seat + 1)
		break
