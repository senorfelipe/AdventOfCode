import os
import sys
import time


class AoCSolution:

    def __init__(self, day=None, input_file=None):
        if day is None:
            day = self.__class__.__name__[-1]
        self.day = day
        if input_file is not None:
            input_file = os.path.join(sys.path[0], input_file)
            self.input_lines = [el.strip() for el in open(
                r"{}".format(input_file)).readlines()]

    def part_one(self):
        pass

    def part_two(self):
        pass

    def solve(self):
        start_one = time.time()
        sol1 = self.part_one()
        duration_one = time.time() - start_one

        start_two = time.time()
        sol2 = self.part_two()
        duration_two = time.time() - start_two

        if sol1 is None:
            print()
            print('Solution day ' + str(self.day) +
                  ' (part 1): Not correctly solved yet.')
            print()
        else:
            print()
            print('Solution day ' + str(self.day) + ' (part 1): ' + str(sol1))
            print('--- %.5f milliseconds ---' % (duration_one * 1000))
            print()
        if sol2 is None:
            print('Solution day ' + str(self.day) +
                  ' (part 2): Not correctly solved yet.')
            print()
        else:
            print('Solution day ' + str(self.day) + ' (part 2): ' + str(sol2))
            print('--- %.5f milliseconds ---' % (duration_two * 1000))
            print()
