from aoc_21.advent_of_code import AoCSolution


class Day3(AoCSolution):

    def part_one(self):
        most_common = self.get_most_common()
        least_common = self.get_leat_common()
        return int(most_common, 2) * int(least_common, 2)

    def calc_common_bits(self):
        res = [0] * (len(self.input_lines[0]) - 1)
        for line in self.input_lines:
            for i in range(0, len(line) - 1):
                num = int(line[i])
                if num > 0:
                    res[i] += 1
                else:
                    res[i] -= 1
        return res

    def get_leat_common(self):
        least_common = ''.join(str(el) for el in [0 if num > 0 else 1 for num in self.calc_common_bits()])
        return least_common

    def get_most_common(self):
        most_common = ''.join(str(el) for el in [1 if num > 0 else 0 for num in self.calc_common_bits()])
        return most_common

    def part_two(self):
        leat_common = self.get_leat_common()
        print(self.life_support_rating())

    def life_support_rating(self):
        most_common = self.get_most_common()
        life_support_rating = self.input_lines
        for i in range(0, len(life_support_rating)):
            for j in range(0, len(most_common)):
                if len(life_support_rating) == 1:
                    return int(life_support_rating[0], 2)
                if life_support_rating[i][j] != most_common[j]:
                    life_support_rating.remove(life_support_rating[i])


Day3(3, '03.in').solve()
