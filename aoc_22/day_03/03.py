
import string
from shared.advent_of_code import AoCSolution


class Day03(AoCSolution):

    def part_one(self):
        priorities = []
        for line in self.input_lines:
            middle = int(len(line)/2)
            first_comp = line[:middle]
            second_comp = line[middle:]
            item = set(first_comp).intersection(second_comp).pop()
            res = self.calc_priority(item)
            priorities.append(res)
        return sum(priorities)

    def calc_priority(self, item):
        res = ord(item.lower()) - 96
        if item.isupper():
            res += 26
        return res

    def part_two(self):
        priorities = []
        for i in range(0, len(self.input_lines), 3):
            item = set(self.input_lines[i]).intersection(
                self.input_lines[i + 1]).intersection(self.input_lines[i + 2]).pop()
            priorities.append(self.calc_priority(item))
        return sum(priorities)

Day03(3, '03.in').solve()
