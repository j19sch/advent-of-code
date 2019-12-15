from pprint import pprint


def add_item_to_dictionary(the_dict, the_key, the_item):
    for k, v in the_dict.items():
        if k == the_key:
            the_dict[the_key] = {**the_dict[the_key], **the_item}
            break
        elif v != {}:
            add_item_to_dictionary(v, the_key, the_item)


def add_item_to_dictionary_and_return_depth(the_dict, the_key, the_item, this_depth=1):
    # ToDo: make it work :-)
    for k, v in the_dict.items():
        if k == the_key:
            the_dict[the_key] = {**the_dict[the_key], **the_item}
            print(f"Depth {this_depth} for {the_item} with key {the_key} ")
            break
        elif v != {}:
            this_depth += 1
            print('recursing time')
            return add_item_to_dictionary(v, the_key, the_item, this_depth=this_depth)

    return this_depth


orbit_map = ['COM)B', 'B)C', 'C)D', 'D)E', 'E)F', 'B)G', 'G)H', 'D)I', 'E)J', 'J)K', 'K)L']

orbits = {}

for orbit in orbit_map:
    p, m = orbit.split(')')
    # print(f"\norbit: {p} ) {m}")
    if orbits == {}:
        orbits[p] = {m: {}}
    else:
        add_item_to_dictionary(orbits, p, {m: {}})

print("\n")
pprint(orbits)
