
import string
from shared.advent_of_code import AoCSolution


class Day04(AoCSolution):

    def part_one(self) -> int:
        count = 0
        for line in self.input_lines:
            ranges = line.split(",")
            start_1 = int(ranges[0].split("-")[0])
            end_1 = int(ranges[0].split("-")[1])
            start_2 = int(ranges[1].split("-")[0])
            end_2 = int(ranges[1].split("-")[1])
            if (start_1 <= start_2) and (end_1 >= end_2):
                count += 1
            elif (start_2 <= start_1) and (end_2 >= end_1):
                count += 1
        return count

    def part_two(self) -> int:
        count = 0
        for line in self.input_lines:
            ranges = line.split(",")
            start_1 = int(ranges[0].split("-")[0])
            end_1 = int(ranges[0].split("-")[1])
            start_2 = int(ranges[1].split("-")[0])
            end_2 = int(ranges[1].split("-")[1])
            if start_1 >= start_2 and start_1 <= end_2:
                count += 1
            elif start_2 >= start_1 and start_2 <= end_1:
                count += 1
        return count


Day04(4, '04.in').solve()
