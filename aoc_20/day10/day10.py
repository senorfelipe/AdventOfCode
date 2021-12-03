import time

start = time.process_time()

with open("10.in") as f:
    data = set()
    for number in f.readlines():
        data.add(int(number.replace("\n", "")))


def part_one():
    jolt_differences = {k: 0 for k in map(str, range(1, 4))}
    last = 0
    for i in range(1, max(data) + 1):
        if i in data:
            jolt_differences[str(i - last)] += 1
            last = i
    jolt_differences["3"] += 1
    return jolt_differences["1"] * jolt_differences["3"]


print("Awnser 1: %d" % (part_one()))

adapters = list(data)
adapters.extend([0, max(data) + 3])
adapters.sort()
checked = {}


def calc_paths(pos):
    if pos == len(adapters) - 1:
        return 1
    if pos in checked:
        return checked[pos]
    total = 0
    for i in range(pos + 1, pos + 4):
        if i < len(adapters) and adapters[i] - adapters[pos] <= 3:
            total += calc_paths(i)
    checked[pos] = total
    return total


print("Awnser 2: %d" % (calc_paths(0)))

print("took: %lf seconds" % (time.process_time() - start))
