# lessons learned:
# - doing a fast thing multiple times is still faster than doing a slow thing once
# - code below undoubtedbly can be optimized and cleaned up, but took me long enough already

file_name = './day03-input.txt'

with open(file_name, 'r') as input_file:
    lines = input_file.readlines()

one = lines[0].split(',')
two = lines[1].split(',')


def determine_path(instructions):
    current_pos = (0, 0)
    path = {(0, 0)}

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

intersections = [coord for coord in path_one if coord in path_two and coord != (0, 0)]
print(f"intersections ({len(intersections)} --- {intersections}")

intersections_with_steps = {}

current_pos = (0, 0)
distance = 0
for instruction in one:
    direction = instruction[0]
    steps = int(instruction[1:])

    for step in range(1, steps + 1):
        distance += 1
        if direction == 'L':
            new_position = (current_pos[0]-1, current_pos[1])
        elif direction == 'R':
            new_position = (current_pos[0]+1, current_pos[1])
        elif direction == 'U':
            new_position = (current_pos[0], current_pos[1]+1)
        elif direction == 'D':
            new_position = (current_pos[0], current_pos[1]-1)
        current_pos = new_position

        if current_pos in intersections:
            intersections_with_steps[f"{current_pos[0]}X{current_pos[1]}"] = distance


current_pos = (0, 0)
distance = 0
for instruction in two:
    direction = instruction[0]
    steps = int(instruction[1:])

    for step in range(1, steps + 1):
        distance += 1
        if direction == 'L':
            new_position = (current_pos[0]-1, current_pos[1])
        elif direction == 'R':
            new_position = (current_pos[0]+1, current_pos[1])
        elif direction == 'U':
            new_position = (current_pos[0], current_pos[1]+1)
        elif direction == 'D':
            new_position = (current_pos[0], current_pos[1]-1)
        current_pos = new_position

        if current_pos in intersections:
            intersections_with_steps[f"{current_pos[0]}X{current_pos[1]}"] += distance


print(intersections_with_steps)
print(min(intersections_with_steps.values()))
