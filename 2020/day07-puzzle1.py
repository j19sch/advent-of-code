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

		if contents == "no other bags":
			ruleset[container] = []
		else:
			split_contents = [_.lstrip() for _ in contents.split(',')]
			split_contents = [_[:-1] if _.endswith('s') else _ for _ in split_contents]
			split_contents = [_[2:] for _ in split_contents]
			ruleset[container] = split_contents

	return ruleset


def find_parent_bags(a_bag, rules, get_the_bags):
	for k,v in rules.items():
		if a_bag in v:
			get_the_bags.add(k)
			find_parent_bags(k, rules, get_the_bags)
		else:
			continue
			
	return get_the_bags


rules_file = open_file('day07-input.txt')

rules = parse_input_file(rules_file)
# pprint(rules)

my_bag = "shiny gold bag"


the_bags = set()
the_the_bags = find_parent_bags(my_bag, rules, the_bags)
print(the_the_bags)
print(len(the_bags))
