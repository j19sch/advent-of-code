# lessons learned:
# - sets and keeping track of current position is way faster than lists and retrieving current postition from list

file_name = './day03-input.txt'

with open(file_name, 'r') as input_file:
    lines = input_file.readlines()

one = lines[0].split(',')
two = lines[1].split(',')


def determine_path(instructions):
    current_pos = (0,0)
    path = {(0,0)}

    for instruction in instructions:
        direction = instruction[0]
        steps = int(instruction[1:])

        for step in range(1, steps + 1):
            if direction == 'L':
                new_position = (current_pos[0]-1, current_pos[1])
            elif direction == 'R':
                new_position = (current_pos[0]+1, current_pos[1])
            elif direction == 'U':
                new_position = (current_pos[0], current_pos[1]+1)
            elif direction == 'D':
                new_position = (current_pos[0], current_pos[1]-1)
            path.add(new_position)
            current_pos = new_position

    return path

path_one = determine_path(one)
path_two = determine_path(two)

intersections = [coord for coord in path_one if coord in path_two  and coord != (0,0)]
print(intersections)

shortest_distance = None
shortest_coord = (0,0)

for intersection in intersections:
    distance = abs(intersection[0]) + abs(intersection[1])
    if shortest_distance is None or distance < shortest_distance:
        shortest_distance = distance
        shortest_coord = intersection

print(shortest_distance)
print(shortest_coord)