"""Day 6: Universal Orbit Map"""

input = open("input.txt").read()

input_list = input.split("\n")
tuple_list = [(el.split(')')[0], el.split(')')[1]) for el in input_list]


def get_orbit_map():
    orbit_map = {0: [('COM', 'COM')]}
    level = 1
    curr_level = get_childs_of('COM')
    next_level = []
    while True:
        if len(curr_level) == 0:
            break
        orbit_map[level] = curr_level
        for elem in curr_level:
            next_level += get_childs_of(elem[1])
        curr_level = list(next_level)
        next_level.clear()
        level += 1
    return orbit_map


def get_childs_of(orbit):
    next_level = []
    for elem in tuple_list:
        if orbit == elem[0]:
            next_level.append(elem)
    return next_level


def count_orbit_number():
    total = 0
    for level in orbit_map:
        total += level * len(orbit_map[level])
    return total


def count_transfers():
    san = get_parent_of('SAN')
    start_you = you = get_parent_of('YOU')
    step_you, step_san = 0, 0
    if san[0] > you[0]:
        you, san = san, you
    while True:
        if san[1][0] == you[1][0]:
            return step_san + step_you
        if you[1][0] == 'COM':
            san = get_parent_of(san[1][0])
            you = start_you
            step_you = 0
            step_san += 1
        you = get_parent_of(you[1][0])
        step_you += 1


def get_parent_of(orbit):
    for level in orbit_map:
        for orb in orbit_map[level]:
            if orb[1] == orbit:
                return [level, orb]


orbit_map = get_orbit_map()
# part1
print(count_orbit_number())
# part2
print(count_transfers())
