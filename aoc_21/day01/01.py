from aoc_21.advent_of_code import AoCSolution


class Day1(AoCSolution):

    def part_one(self):
        increased_count = -1
        prev = 0
        for depth in self.input_lines:
            curr = int(depth)
            if curr > prev:
                increased_count += 1
            prev = curr
        return increased_count

    def part_two(self):
        increased_count = -1
        prev_window = 0
        depths = list(map(int, self.input_lines))
        for i in range(0, len(depths)):
            if i + 2 >= len(depths):
                return increased_count
            curr_window = sum(depths[i:i + 3])
            if curr_window > prev_window:
                increased_count += 1
            prev_window = curr_window


Day1(1, '01.in').solve()
