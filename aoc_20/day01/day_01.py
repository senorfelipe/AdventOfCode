def find_etries():
    with open('input.txt', 'r') as input:
        lines = [int(line) for line in input.readlines()]
        for line1 in lines:
            for line2 in lines:
                if line1 + line2 == 2020:
                    return line1 * line2


print(find_etries())


def find_three_etries():
    with open('input.txt', 'r') as input:
        lines = [int(line) for line in input.readlines()]
        i = 0
        for line1 in lines:
            for line2 in lines:
                for line3 in lines:
                    if (line1 + line2 + line3) == 2020:
                        return line1 * line2 * line3


print(find_three_etries())
