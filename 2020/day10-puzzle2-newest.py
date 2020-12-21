import itertools

def open_file(in_file):
	with open(f'./{in_file}', 'r') as input_file:
		input_list = input_file.readlines()
	return [int(_.rstrip()) for _ in input_list]


# adapters = open_file('day10-example.txt')  # 8
adapters = open_file('day10-example2.txt')  # 10368 -> 19208
# adapters = open_file('day10-input.txt')


device_max = max(adapters) + 3
adapters.append(device_max)  # in or out?

charging_outlet = 0
adapters.append(charging_outlet)  # in or out?

the_dict = {k: [] for k in adapters}

for k,v in the_dict.items():
	if k + 1 in adapters:
		v.append(k+1)
	if k + 2 in adapters:
		v.append(k+2)
	if k + 3 in adapters:
		v.append(k+3)

print(the_dict)
from pprint import pprint
pprint(sorted(the_dict.items(), key=lambda t: t[0]))

nodes = []

for keeh in sorted(the_dict.keys()):  # sorted not needed
	# print(keeh)
	jump = False
	if len(the_dict[keeh]) > 1:
		jump = True
	elif keeh - 1 in the_dict.keys():
		for _ in the_dict[keeh - 1]:
			if _ > keeh:
				# print("jump")
				jump = True
	elif keeh - 2 in the_dict.keys():
		for _ in the_dict[keeh - 2]:
			if _ >	 keeh:
				# print("jump")
				jump = True
	elif keeh - 3 in the_dict.keys():
		for _ in the_dict[keeh - 3]:
			if _ >	 keeh:
				# print("jump")
				jump = True

	if jump is False:
		nodes.append(keeh)
		# print(keeh, 'node')

# print(nodes)


the_total = 1
tmp_counter = 1


for keeh in sorted(the_dict.keys()):
	if keeh in nodes:
		the_total *= tmp_counter
		tmp_counter = 1
		continue
	else:
		tmp_counter += len(the_dict[keeh]) - 1

print(the_total)




# ends = list(itertools.chain(*the_dict.values()))
# nodes = []
# nodes = [_ for _ in ends if ends.count(_) == 1]
# print(sorted(nodes)

# nodes = []
# for adapter in adapters:
# 	count = 0
# 	[_.values() for _ in the_dict




# from pprint import pprint
# pprint(sorted(the_dict.items(), key=lambda t: t[0]))

# sol_counter = 1

# for keeh in sorted(the_dict.keys()):
# 	print(keeh)
# 	nexts = the_dict[keeh]
# 	if len(nexts) == 1:
# 		print('next!')
# 	else:
# 		print(nexts)

# 	print()