import pytest

from day002_puzzle1 import *

test_input = [
	"Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green",
	"Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue",
	"Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red",
	"Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red",
	"Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green"
]



def test_split_on_colons():
	split = split_on_colons(test_input)
	assert split[0] == ["Game 1", "3 blue, 4 red", "1 red, 2 green, 6 blue",
						"2 green"]
	assert split[1] == ["Game 2", "1 blue, 2 green", "3 green, 4 blue, 1 red", "1 green, 1 blue"]


def test_turn_into_dict():
	test_input = [
		["Game 1", "3 blue, 4 red", "1 red, 2 green, 6 blue","2 green"],
		["Game 2", "1 blue, 2 green", "3 green, 4 blue, 1 red", "1 green, 1 blue"]
	]
	mydict = turn_into_dict(test_input)
	assert mydict == {
		"1": ["3 blue, 4 red", "1 red, 2 green, 6 blue","2 green"],
		"2": ["1 blue, 2 green", "3 green, 4 blue, 1 red", "1 green, 1 blue"]}


@pytest.mark.parametrize("test_input, expected", [
		(["3 blue", "4 red"], {"blue": "3", "red": "4"}),
		(["1 red", "2 green", "6 blue"], {"red": "1", "green": "2", "blue": "6"})
	])
def test_create_sample_dict(test_input,expected):
	result = create_sample_dict(test_input)
	assert result == expected

def test_parse_samples():
	test_input = ["3 blue, 4 red", "1 red, 2 green, 6 blue","2 green"]
	result = parse_samples(test_input)
	assert result == [
		{"blue": "3", "red": "4"},
		{"red": "1", "green": "2", "blue": "6"},
		{"green": "2"}
	]

def test_get_max_of_each_color():
	test_input = [
		{"blue": "3", "red": "4"},
		{"red": "1", "green": "2", "blue": "6"},
		{"green": "2"}
	]
	result = get_max_of_each_color(test_input)
	assert result == {"blue": 6, "red": 4, "green": 2}

@pytest.mark.parametrize("test_input, expected", [
	({"blue": 6, "red": 4, "green": 2}, True),
	({"blue": 15, "red": 4, "green": 2}, False)
])
def test_compare_to_bag(test_input, expected):
	# test_input = {"blue": 6, "red": 4, "green": 2}
	bag = {"red": 12, "green": 13, "blue": 14 }
	result = compare_to_bag(test_input, bag)
	assert result is expected