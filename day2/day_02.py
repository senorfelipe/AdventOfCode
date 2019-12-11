"""Day 2: 1202 Program Alarm"""

test_data = [2, 3, 0, 3, 99]

input_data = [1, 12, 2, 3, 1, 1, 2, 3, 1, 3, 4, 3, 1, 5, 0, 3, 2, 10, 1, 19, 1, 5, 19, 23, 1, 23, 5, 27, 1, 27, 13, 31,
              1, 31, 5, 35, 1, 9, 35, 39, 2, 13, 39, 43, 1, 43, 10, 47, 1, 47, 13, 51, 2, 10, 51, 55, 1, 55, 5, 59, 1,
              59, 5, 63, 1, 63, 13, 67, 1, 13, 67, 71, 1, 71, 10, 75, 1, 6, 75, 79, 1, 6, 79, 83, 2, 10, 83, 87, 1, 87,
              5, 91, 1, 5, 91, 95, 2, 95, 10, 99, 1, 9, 99, 103, 1, 103, 13, 107, 2, 10, 107, 111, 2, 13, 111, 115, 1,
              6, 115, 119, 1, 119, 10, 123, 2, 9, 123, 127, 2, 127, 9, 131, 1, 131, 10, 135, 1, 135, 2, 139, 1, 10, 139,
              0, 99, 2, 0, 14, 0]

raw_input_data = list(input_data)


def intcode_program(input):
    for i in range(0, len(input), 4):
        if (i + 4) <= len(input) and (input[i] != 99):
            idx_1 = input[i + 1]
            idx_2 = input[i + 2]
            res_idx = input[i + 3]
        else:
            return
        if input[i] == 1:
            input[res_idx] = input[idx_1] + input[idx_2]
        elif input[i] == 2:
            input[res_idx] = input[idx_1] * input[idx_2]


intcode_program(input_data)
print("result of part one is: ", input_data[0])


def get_noun_and_verb():
    for i in range(0, 100):
        for j in range(0, 100):
            raw_input = raw_input_data.copy()
            raw_input[1:3] = [i, j]
            intcode_program(raw_input)
            if raw_input[0] == 19690720:
                return [i, j]


noun_and_verb = get_noun_and_verb()
print("Noun and verb are: ", noun_and_verb)
print("100 * noun + verb: ", 100 * noun_and_verb[0] + noun_and_verb[1])
