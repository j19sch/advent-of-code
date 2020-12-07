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

"""
start top-left corner
right 3, down 1
tree pattern repeats
encounter 7 trees
"""

def open_file(in_file):
	with open(f'./{in_file}', 'r') as input_file:
		input_list = input_file.readlines()
	return [_.rstrip() for _ in input_list]


def count_trees(trees_map):

	map_width = len(trees_map[0])
	map_height = len(trees_map)
	print(map_width, map_height)

	x = 0
	y = 0
	print(x, y, trees_map[y][x])

	trees = 0

	for _ in range(map_height - 1):
		x += 3
		if x > map_width - 1:
			x -= map_width

		y += 1
		print(x, y, trees_map[y][x])
		# print(trees_map[y])

		if trees_map[y][x] == "#":
			trees += 1

	return trees


# example_trees = count_trees(example)
# print(example_trees)

example_map = open_file('day03-example.txt')
example_trees = count_trees(example_map)
print(example_trees)

the_map = open_file('day03-input.txt')
puzzle_trees = count_trees(the_map)
print(puzzle_trees)
