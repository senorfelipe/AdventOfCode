from aoc_21.advent_of_code import AoCSolution


class Day2(AoCSolution):

    def part_one(self):
        pos = [0, 0]  # [horizontal pos, depth]
        for command in self.input_lines:
            command = command.split(" ")
            amount = int(command[1])
            direction = command[0]
            if direction == "forward":
                pos[0] += amount
            if direction == "up":
                pos[1] -= amount
            if direction == "down":
                pos[1] += amount
        return pos[0] * pos[1]

    def part_two(self):
        pos = [0, 0, 0]  # [horizontal pos, depth, aim]
        for command in self.input_lines:
            command = command.split(" ")
            amount = int(command[1])
            direction = command[0]
            if direction == "forward":
                pos[0] += amount
                pos[1] += pos[2] * amount
            if direction == "up":
                pos[2] -= amount
            if direction == "down":
                pos[2] += amount
        return pos[0] * pos[1]


Day2(2, '02.in').solve()
