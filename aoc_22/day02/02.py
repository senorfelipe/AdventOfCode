import os
import sys
import time

# TODO use parent class, fix import error
from advent_of_code import AoCSolution


class Day2(AoCSolution):

    shape_map = {"X": "A", "Y": "B", "Z": "C"}
    shape_scores = {"A": 1, "B": 2, "C": 3}
    loses = ["AC", "BA", "CB"]

    win_lose_dict = {"A": "CB", "B": "AC", "C": "BA"}

    def part_one(self):
        score = 0
        for line in self.input_lines:
            opponent = line[0]
            myself = self.shape_map[line[2]]
            score += self.shape_scores[myself] + \
                self.calc_round_points(opponent, myself)
        return score

    def calc_round_points(self, opponent, myself):
        if opponent == myself:
            return 3
        if self.loses.count(opponent + myself) > 0:
            return 0
        else:
            return 6

    def part_two(self):
        score = 0
        for line in self.input_lines:
            opponent = line[0]
            strategy = line[2]
            if strategy == "Y":
                score += 3 + self.shape_scores[opponent]
            elif strategy == "X":
                score += self.shape_scores[self.win_lose_dict[opponent][0]]
            elif strategy == "Z":
                score += 6 + self.shape_scores[self.win_lose_dict[opponent][1]]
        return score


Day2(1, '02.in').solve()
