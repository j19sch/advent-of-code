import re

example_input = [
	"Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green",
	"Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue",
	"Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red",
	"Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red",
	"Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green"
]

split = [re.split(':|;', _) for _ in example_input]
# print(split)

stripped = [[_.strip() for _ in game] for game in split]
# print(stripped)

game_dict = {}

for game in stripped:
	game_index = game.pop(0).split(' ')[1]
	game_dict[game_index] = {}

	# ['Game 1', '3 blue, 4 red', '1 red, 2 green, 6 blue', '2 green']

	for idx, samples in enumerate(game):
		game_dict[game_index][idx] = {}
		# colors_counts = samples.split(', ')  # ['3 blue', '4 red']'
		color_count = [_.split(' ') for _ in samples.split(', ')]  # [['3', 'blue'], ['4', 'red']]

		for _ in color_count:
			md = {_[1]: _[0]}
			game_dict[game_index][idx].update(md)

print(game_dict)

# only 12 red cubes, 13 green cubes, and 14 blue cubes


# so need max per color

# max red, green, blue

for game, samples in game_dict.items():
	for sample, result in samples.items():
		pass



total = {
	"red": 12,
	"green": 13,
	"blue": 14
}

