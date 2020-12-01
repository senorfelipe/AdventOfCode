

file = open('./input.txt')
ids = file.read().split('\n')


for id in ids:
    two_chars_equal = 0
    three_chars_equal = 0
    for i in range(0, len(id)):
         x = []