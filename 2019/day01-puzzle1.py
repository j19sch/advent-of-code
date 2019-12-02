from math import floor

filename = 'day01-input.txt'

with open(filename, 'r') as input_file:
    the_masses = [int(_) for _ in input_file.readlines()]
    fuel_req = sum(floor(mass/3) - 2 for mass in the_masses)
    print(fuel_req)
