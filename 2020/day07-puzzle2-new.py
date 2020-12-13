from pprint import pprint
import re


def open_file(in_file):
	with open(f'./{in_file}', 'r') as input_file:
		input_list = input_file.readlines()
	return [_.rstrip() for _ in input_list]

def parse_input_file(the_file):
	ruleset = {}

	regex = r'(\w+ \w+ bag)s contain (.+?)\.$'

	for rule in the_file:

		m = re.match(regex, rule)
		container, contents = m.groups()

		ruleset[container] = {}

		if contents == "no other bags":
			continue
		else:
			ruleset[container] = {}
			split_contents = [_.lstrip() for _ in contents.split(',')]
			split_contents = [_[:-1] if _.endswith('s') else _ for _ in split_contents]
			for sc in split_contents:
				ruleset[container][sc[2:]] = int(sc[0])

	return ruleset

rules_file = open_file('day07-example.txt')
# rules_file = open_file('day07-example2.txt')
# rules_file = open_file('day07-input.txt')

rules = parse_input_file(rules_file)
# pprint(rules)

"""
{'bright white bag': {'shiny gold bag': 1},
 'dark olive bag': {'dotted black bag': 4, 'faded blue bag': 3},
 'dark orange bag': {'bright white bag': 3, 'muted yellow bag': 4},
 'dotted black bag': {},
 'faded blue bag': {},
 'light red bag': {'bright white bag': 1, 'muted yellow bag': 2},
 'muted yellow bag': {'faded blue bag': 9, 'shiny gold bag': 2},
 'shiny gold bag': {'dark olive bag': 1, 'vibrant plum bag': 2},
 'vibrant plum bag': {'dotted black bag': 6, 'faded blue bag': 5}}
"""


def count_the_bags(a_bag, a_bag_count, total_bags, rules):
	print(f"a_bag: {a_bag}, a_bag_count: {a_bag_count}")
	print(f"in a_bag: {rules[a_bag]}")

	num_of_bags = sum(rules[a_bag].values()) * a_bag_count
	print(f"number of bags: {num_of_bags}")

	total_bags += num_of_bags
	print(f"total bags: {total_bags}")
	print()

	for bag, number in rules[a_bag].items():
		a_bag_count = number
		count_the_bags(bag, a_bag_count, total_bags, rules)
	# 	print(f"bag: {bag}, number: {number}")

	# 	a_bag_count *= number
		
	# 	# num_of_bags = sum(rules[bag].values()) * a_bag_count
	# 	# print(f"number of bags: {num_of_bags}")
		
	# 	# total_bags += num_of_bags
	# 	# print(f"total bags: {total_bags}")
	# 	# print()

	# 	count_the_bags(bag, number, total_bags, rules)


my_bag = "shiny gold bag"


# outer_bags_count = 1
# inner_bags_count = sum(rules[my_bag].values()) * outer_bags_count
# print(inner_bags_count)

# 1 + 1*7 + 2 + 2*11 = 32 bags!
# 'shiny gold bag': {'dark olive bag': 1, 'vibrant plum bag': 2},
# 'dark olive bag': {'dotted black bag': 4, 'faded blue bag': 3}, -> 7
# 'vibrant plum bag': {'dotted black bag': 6, 'faded blue bag': 5}} -> 11

# for bag, number in rules[my_bag].items():
# 	asd = sum(rules[bag].values()) * outer_bags_count
# 	print(bag, asd)


count_the_bags(my_bag, 1, 0, rules)