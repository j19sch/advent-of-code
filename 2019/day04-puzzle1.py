puzzle_input = "356261-846303"
possibilities = 0

for might_be in range(356261, 846303 + 1):
    str_might_be = str(might_be)
    if str_might_be[0] != str_might_be[1] and str_might_be[1] != str_might_be[2] and str_might_be[2] != str_might_be[3] and \
            str_might_be[3] != str_might_be[4] and str_might_be[4] != str_might_be[5]:
        continue
    if int(str_might_be[0]) > int(str_might_be[1]) or int(str_might_be[1]) > int(str_might_be[2]) or \
            int(str_might_be[2]) > int(str_might_be[3]) or int(str_might_be[3]) > int(str_might_be[4]) or int(str_might_be[4]) > int(str_might_be[5]):
        continue
    possibilities += 1

print(possibilities)
