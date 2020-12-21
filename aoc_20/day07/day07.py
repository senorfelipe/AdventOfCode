import time
from string import digits

NO_OTHER = "no other"

start = time.process_time()

SHINY_GOLD = "shiny gold"


def create_bags_dict(part=1):
    global bags
    with open("./7.in") as f:
        input = f.readlines()
        bags = {}
        for el in input:
            bag = el.split("contain")
            bag[1] = bag[1].replace(".", "").split(",")
            bag[1] = list(map(lambda s: s.replace("bags", "").replace("bag", ""), bag[1]))
            if part == 1:
                bag[1] = list(map(lambda s: s.translate(str.maketrans("", "", digits)), bag[1]))
            bag[1] = list(map(str.strip, bag[1]))
            bags[bag[0].replace("bags", "").strip()] = bag[1]
        return bags


bags = create_bags_dict(1)


def find_colors_for_shiny_gold(color):
    if SHINY_GOLD in color:
        return True
    else:
        return any(find_colors_for_shiny_gold(color) for color in bags[color] if color != "no other")


print("Awnser part 1: %d" % (sum((find_colors_for_shiny_gold(color) for color in bags.keys())) - 1))


def get_color(bag):
    return bag.split(maxsplit=1)[1]


def get_count(bag):
    return int(bag.split(maxsplit=1)[0])


bags_2 = create_bags_dict(2)
print(bags_2)


def count_bags(color="1 " + SHINY_GOLD):
    return sum(
        get_count(child) + get_count(child) * count_bags(child) for child in bags_2[get_color(color)] if
        NO_OTHER not in child)


print("Awnser part 2: %d" % (count_bags()))

print("took: %f seconds" % (time.process_time() - start))
