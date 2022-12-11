# TODO use parent class, fix import error
from advent_of_code import AoCSolution


import os
import sys
import time


class Day1(AoCSolution):

    def __init__(self, day=None, input_file=None):
        if day is None:
            day = self.__class__.__name__[-1]
        self.day = day
        if input_file is not None:
            input_file = os.path.join(sys.path[0], input_file)
            self.input_lines = [el.strip() for el in open(
                r"{}".format(input_file)).readlines()]

    def part_one(self):
        curr = 0
        highest = 0
        for line in self.input_lines:
            if line == "":
                if curr > highest:
                    highest = curr
                curr = 0
            else:
                curr += int(line)
        return highest

    def part_two(self):
        curr = 0
        calories_per_elfe = []
        for line in self.input_lines:
            if line == "":
                calories_per_elfe.append(curr)
                curr = 0
            else:
                curr += int(line)
        calories_per_elfe.sort()
        print(calories_per_elfe)
        return sum(calories_per_elfe[-3:])


Day1(1, '01.in').solve()
