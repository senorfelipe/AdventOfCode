from calendar import c
from shared.advent_of_code import AoCSolution


class Day02(AoCSolution):
    RULES = {"red": 12, "green": 13, "blue": 14}

    def part_one(self):
        sum = 0
        for game_id, line in enumerate(self.input_lines, 1):
            valid_game = True
            print(f"Game {game_id}")
            for game_set in line.split(": ")[1].split("; "):
                print(game_set)
                for colors in game_set.split(", "):
                    cubes = colors.strip().split(" ")
                    if self.RULES[cubes[1]] < int(cubes[0]):
                        valid_game = False
            print("=" * 80)
            if valid_game:
                sum += game_id
        return sum

    def part_two(self):
        return super().part_two()


Day02(2, "./input.txt").solve()
