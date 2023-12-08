import re

example_input = [
	"Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green",
	"Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue",
	"Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red",
	"Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red",
	"Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green"
]

def open_file():
	with open('./day02-input.txt', 'r') as input_file:
		input_list = input_file.readlines()
	return [_.rstrip() for _ in input_list]


def split_on_colons(unsplit):
	split = [re.split(': |; ', _) for _ in unsplit]
	return split

def turn_into_dict(split_input):
	mydict = {}
	for game in split_input:
		key = game.pop(0).split(' ')[1]
		mydict[key] = game
	return mydict

def create_sample_dict(sample):
	my_dict = {}
	for color in sample:
		split = color.split(" ")
		my_dict.update({split[1]: split[0]})
	return my_dict


def parse_samples(samples):
	parsed_samples = []
	for sample in samples:
		split_per_color = sample.split(", ")
		the_dict = create_sample_dict(split_per_color)
		parsed_samples.append(the_dict)
	return parsed_samples



def get_max_of_each_color(samples):
	counter = {"blue": 0, "red": 0, "green": 0}
	
	for sample in samples:
		for color, count in sample.items():
			if int(count) > counter[color]:
				counter[color] = int(count)

	return counter


def compare_to_bag(sample, bag):
	for color, count in sample.items():
		if int(count) > bag[color]:
			return False
	else:
		return True


bag = {
	"red": 12,
	"green": 13,
	"blue": 14
}


if __name__ == "__main__":
	input_data = open_file()
	# input_data = example_input
	split_input = split_on_colons(input_data)
	dict_input = turn_into_dict(split_input)

	dict_parsed = {k:parse_samples(v) for k,v in dict_input.items()}
	dict_maxes = {k:get_max_of_each_color(v) for k,v in dict_parsed.items()}

	sum_of_possible_games = 0
	for game_id, samples in dict_maxes.items():
		if compare_to_bag(samples, bag) is True:
			sum_of_possible_games += int(game_id)


	print(sum_of_possible_games)