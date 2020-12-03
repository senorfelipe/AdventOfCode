trees = 0
x, y = 0, 0
for line in open('input.txt').readlines():
    line = line.replace('\n', '')
    if line[x] == '#' and y != 0:
        trees += 1
    y += 1
    x += 3
    if x >= len(line):
        x = x % len(line)

print('Answer part 1: ' + str(trees))

# ------------------------------------------------- #

slopes = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
data = []
for line in open('input.txt').readlines():
    data.append([a for a in line if a != '\n'])

results = []
for slope in slopes:
    trees = 0
    x = slope[0]
    for y in range(slope[1], len(data), slope[1]):
        if data[y][x] == '#':
            trees += 1
        x += slope[0]
        if x >= len(data[y]):
            x = x % len(data[y])
    results.append(trees)

result = 1
for i in range(0, len(results)):
    result *= results[i]

print('Answer part 2: ' + str(result))
