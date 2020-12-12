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


def find_parent_bags(a_bag, rules, get_the_bags):
	for k,v in rules.items():
		if a_bag in v:
			get_the_bags.add(k)
			find_parent_bags(k, rules, get_the_bags)
		else:
			continue
			
	return get_the_bags


"""
{'bright white bag': {'shiny gold bag': 1},
 ==> 'dark olive bag': {'dotted black bag': 4, 'faded blue bag': 3},
 'dark orange bag': {'bright white bag': 3, 'muted yellow bag': 4},
 'dotted black bag': {},
 'faded blue bag': {},
 'light red bag': {'bright white bag': 1, 'muted yellow bag': 2},
 'muted yellow bag': {'faded blue bag': 9, 'shiny gold bag': 2},
 ==> 'shiny gold bag': {'dark olive bag': 1, 'vibrant plum bag': 2},
 ==> 'vibrant plum bag': {'dotted black bag': 6, 'faded blue bag': 5}}
"""

def add_child_bags(a_bag, a_bag_count, rules, count_the_bags):
	if rules[a_bag] != {}:
		print(a_bag, rules[a_bag], a_bag_count)

		bags_count = (a_bag_count * sum(rules[a_bag].values()))
		print(f"bags_count: {bags_count}")
		count_the_bags += bags_count
		print(f"count_the_bags: {count_the_bags}")

		for k,v in rules[a_bag].items():
			# bags_count = v * a_bag_count
			# print(f"this bag: {bags_count} {k}")

			# count_the_bags += (v * a_bag_count)
			# print(f"count: {count_the_bags}")
			add_child_bags(k, (v * a_bag_count), rules, count_the_bags)

	return count_the_bags

	# print(rules[a_bag])
	# c_bags = sum(rules[a_bag].values()) * a_bag_count
	# print(c_bags)

	# count_the_bags += c_bags
	# print(count_the_bags)

	# for k,v in rules[a_bag].items():
	# 	print(k, '|', v)
	# 	add_child_bags(k, v, rules, count_the_bags)

	# return count_the_bags


	# for k,v in rules[a_bag].items():
	# 	print(a_bag, '|', k, '|', v)
	# 	count_the_bags += (v * a_bag_count)

		# a_bag_count = v
		# print(count_the_bags, a_bag_count)
		# add_child_bags(k, a_bag_count, rules, count_the_bags)

		# count_the_bags += v
		# print(count_the_bags)
		# a_bag_count = a_bag_count * v
		# count_the_bags += a_bag_count
		# print(a_bag_count, count_the_bags)
		# add_child_bags(k, a_bag_count, rules, count_the_bags)

	# return count_the_bags



# rules_file = open_file('day07-example.txt')
rules_file = open_file('day07-input.txt')

rules = parse_input_file(rules_file)
# pprint(rules)

my_bag = "shiny gold bag"
my_inner_bags = 1

# for k,v in rules[my_bag].items():
	# my_inner_bags += v
	# print(v,k)

for k,v in rules[my_bag].items():
	print()
	my_inner_bags += 1
	inner_bags = add_child_bags(k, v, rules, 0)
	my_inner_bags += inner_bags


# my_inner_bags = add_child_bags(my_bag, 1, rules, my_inner_bags)
print()
print(f"total: {my_inner_bags}")

# 127 too low
