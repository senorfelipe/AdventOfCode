import os
import sys
import time


class AoCSolution:
    def __init__(self, day=None, input_file=None):
        self.solution_one = None
        self.solution_two = None
        if day is None:
            day = self.__class__.__name__[-1]
        self.day = day
        if input_file is not None:
            self.input_lines = [
                el.strip()
                for el in open(os.path.join(sys.path[0], input_file)).readlines()
            ]

    def part_one(self):
        pass

    def part_two(self):
        pass

    def solve(self, part=None):
        start_one = time.time()
        self.solution_one = self.part_one()
        duration_one = time.time() - start_one

        if part is None or part == 1:
            self.print_solution(1, self.solution_one, duration_one)

        start_two = time.time()
        self.solution_two = self.part_two()
        duration_two = time.time() - start_two

        if part is None or part == 2:
            self.print_solution(2, self.solution_two, duration_two)

    def print_solution(self, part, solution, duration):
        print()
        if solution is None:
            print(
                f"Solution day {str(self.day)} (part {part}): Not correctly solved yet."
            )
        else:
            print(f"Solution day {self.day} (part {part}): {str(solution)}")
            print("--- %.5f milliseconds ---" % (duration * 1000))
        print()
