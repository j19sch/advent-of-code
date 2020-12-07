example = [
	"..##.......",
	"#...#...#..",
	".#....#..#.",
	"..#.#...#.#",
	".#...##..#.",
	"..#.##.....",
	".#.#.#....#",
	".#........#",
	"#.##...#...",
	"#...##....#",
	".#..#...#.#"
]

slopes = [
	(1, 1),
	(3, 1),  # puzzle 1
	(5, 1),
	(7, 1),
	(1, 2)
]

def open_file(in_file):
	with open(f'./{in_file}', 'r') as input_file:
		input_list = input_file.readlines()
	return [_.rstrip() for _ in input_list]


def count_trees(trees_map, slope):

	map_width = len(trees_map[0])
	map_height = len(trees_map)
	print("map size", map_width, map_height)

	x = 0
	y = 0
	print(x, y, trees_map[y][x])

	trees = 0

	for _ in range(map_height - 1):
		x += slope[0]
		if x > map_width - 1:
			x -= map_width

		y += slope[1]

		# try/except instead of calculating the range for Right 1, down 2
		try:
			trees_map[y]
		except IndexError:
			break

		print(x, y, trees_map[y][x])

		if trees_map[y][x] == "#":
			trees += 1

	return trees


def multiple_slopes(the_map, the_slopes):
	trees_product = 1

	for slope in the_slopes:
		print(f"slope: {slope}")
		example_trees = count_trees(the_map, slope)
		print(example_trees)
		trees_product *= example_trees

	return trees_product


example_map = open_file('day03-example.txt')
example_product = multiple_slopes(example_map, slopes)
print(example_product)

puzzle_map = open_file('day03-input.txt')
puzzle_product = multiple_slopes(puzzle_map, slopes)
print(puzzle_product)
