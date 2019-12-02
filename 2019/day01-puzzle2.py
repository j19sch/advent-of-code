from math import floor

filename = 'day01-input.txt'


def recurse_the_thing(mass):
    fuel = floor(mass/3) - 2

    if fuel <= 0:
        return 0
    else:
        return fuel + recurse_the_thing(fuel)


with open(filename, 'r') as input_file:
    the_masses = [int(_) for _ in input_file.readlines()]

    fuel_req = sum([recurse_the_thing(mass) for mass in the_masses])
    print(fuel_req)
