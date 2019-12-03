
# one = "R8,U5,L5,D3".split(',')
# two = "U7,R6,D4,L4".split(',')

# one = "R75,D30,R83,U83,L12,D49,R71,U7,L72".split(',')
# two = "U62,R66,U55,R34,D71,R55,D58,R83".split(',')

# one = "R98,U47,R26,D63,R33,U87,L62,D20,R33,U53,R51".split(',')
# two = "U98,R91,D20,R16,D67,R40,U7,R15,U6,R7".split(',')

def determine_path(instructions):
    path = [(0,0)]

    for instruction in instructions:
        direction = instruction[0]
        steps = int(instruction[1:])

        for step in range(1, steps + 1):
            if direction == 'L':
                new_position = (path[-1][0]-1, path[-1][1])
            elif direction == 'R':
                new_position = (path[-1][0]+1, path[-1][1])
            elif direction == 'U':
                new_position = (path[-1][0], path[-1][1]+1)
            elif direction == 'D':
                new_position = (path[-1][0], path[-1][1]-1)
            path.append(new_position)

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