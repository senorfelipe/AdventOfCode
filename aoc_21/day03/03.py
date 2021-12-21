from aoc_21.advent_of_code import AoCSolution


class Day3(AoCSolution):

    def part_one(self):
        lines = self.calc_common_bits(self.input_lines)
        most_common = self.get_most_common(lines)
        least_common = self.get_least_common(lines)
        return int(most_common, 2) * int(least_common, 2)

    @staticmethod
    def calc_common_bits(lines):
        res = [0] * (len(lines[0]))
        for line in lines:
            for i in range(0, len(line) - 1):
                num = int(line[i])
                if num > 0:
                    res[i] += 1
                else:
                    res[i] -= 1
        return res

    @staticmethod
    def get_least_common(lines):
        least_common = ''.join(str(el) for el in
                               [0 if num >= 0 else 1 for num in lines])
        return least_common

    @staticmethod
    def get_most_common(lines):
        most_common = ''.join(
            str(el) for el in [1 if num >= 0 else 0 for num in lines])
        return most_common

    def part_two(self):
        return self.oxygen_gen_rating() * self.c02_scrubber_rating()

    def oxygen_gen_rating(self):
        life_support_rating = self.input_lines.copy()
        most_common = self.get_most_common(self.calc_common_bits(life_support_rating))
        to_remove = []
        for i in range(0, len(most_common) + 1):
            [life_support_rating.remove(x) for x in to_remove]
            if len(life_support_rating) == 1:
                return int(life_support_rating[0], 2)
            most_common = self.get_most_common(self.calc_common_bits(life_support_rating))
            to_remove.clear()
            for j in range(0, len(life_support_rating)):
                if life_support_rating[j][i] != most_common[i]:
                    to_remove.append(life_support_rating[j])

    def c02_scrubber_rating(self):
        life_support_rating = self.input_lines.copy()
        least_common = self.get_least_common(self.calc_common_bits(life_support_rating))
        to_remove = []
        for i in range(0, len(least_common) + 1):
            [life_support_rating.remove(x) for x in to_remove]
            if len(life_support_rating) == 1:
                return int(life_support_rating[0], 2)
            least_common = self.get_least_common(self.calc_common_bits(life_support_rating))
            to_remove.clear()
            for j in range(0, len(life_support_rating)):
                if life_support_rating[j][i] != least_common[i]:
                    to_remove.append(life_support_rating[j])


Day3(3, '03.in').solve()
