from calendar import c
from functools import reduce
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
        sum_power = 0
        for game_id, line in enumerate(self.input_lines, 1):
            print(f"Game {game_id}")
            fewest_possible = {"red": 0, "green": 0, "blue": 0}

            for game_set in line.split(": ")[1].split("; "):
                print(game_set)
                for cubes_to_color in game_set.split(", "):
                    n_cubes, col = cubes_to_color.split()
                    if fewest_possible[col] < int(n_cubes):
                        fewest_possible[col] = int(n_cubes)
            
            print(fewest_possible)
            sum_power += reduce(lambda x, y: x * y, list(fewest_possible.values()))
            print("=" * 80)
        return sum_power


Day02(2, "./input.txt").solve(2)
