# lessons learned:
# - break is not continue

# puzzle_input = "356261-846303"
possibilities = []

for might_be in range(356261, 846303 + 1):
    str_might_be = str(might_be)
    if str_might_be[0] != str_might_be[1] and str_might_be[1] != str_might_be[2] and str_might_be[2] != str_might_be[
        3] and \
            str_might_be[3] != str_might_be[4] and str_might_be[4] != str_might_be[5]:
        continue
    if int(str_might_be[0]) > int(str_might_be[1]) or int(str_might_be[1]) > int(str_might_be[2]) or \
            int(str_might_be[2]) > int(str_might_be[3]) or int(str_might_be[3]) > int(str_might_be[4]) or int(
        str_might_be[4]) > int(str_might_be[5]):
        continue
    possibilities.append(might_be)

possib_2 = []

for possib in possibilities:
    str_possib = str(possib)

    if (str_possib[0] == str_possib[1] and str_possib[0] != str_possib[2]) or \
            (str_possib[4] == str_possib[5] and str_possib[4] != str_possib[3]) or \
            any((str_possib[n] == str_possib[n+1] and str_possib[n] != str_possib[n-1] and str_possib[n] != str_possib[n+2]) for n in range(1, 4)):
        possib_2.append(possib)

print(f"possibilities: {len(possib_2)} out of {len(possibilities)}")
