def open_file(in_file):
	with open(f'./{in_file}', 'r') as input_file:
		input_list = input_file.readlines()
	return [int(_.rstrip()) for _ in input_list]


# adapters = open_file('day10-example2.txt')
# print(adapters)

adapters = open_file('day10-input.txt')

device_max = max(adapters) + 3
adapters.append(device_max)
# print(device_max)

charging_outlet = 0
prev = charging_outlet
ones = 0
twos = 0
threes = 0

for adapter in sorted(adapters):
	diff = adapter - prev
	if diff == 1:
		ones +=1
	elif diff == 2:
		twos += 1
	elif diff == 3:
		threes += 1
	else:
		print("OH NOES!")

	prev = adapter

print(ones, twos, threes)
print(ones * threes)
