# import re

def open_file(in_file):
	with open(f'./{in_file}', 'r') as input_file:
		input_list = input_file.readlines()
	return [_.rstrip() for _ in input_list]



def parse_answers_file(the_file):
	answers = []
	index = 0

	for answer in the_file:
		try:
			answers[index]
		except IndexError:
			answers.append([])

		if answer != "":
			answers[index].extend([_ for _ in answer])
		else:
			index += 1

	return answers

def sum_count_the_answers(answers):
	sum = 0

	for answer in answers:
		sum += len(set(answer))

	return sum


answers_file = open_file('day06-input.txt')
the_answers = parse_answers_file(answers_file)
the_sum = sum_count_the_answers(the_answers)
print(the_sum)
