class AoCSolution:

    def __init__(self, day, input_file=None):
        self.day = day
        if input_file is not None:
            self.input_lines = open(input_file).readlines()

    def part_one(self):
        pass

    def part_two(self):
        pass

    def solve(self):
        sol1 = self.part_one()
        sol2 = self.part_two()
        if sol1 is None:
            print('Solution day ' + str(self.day) + ' (part 1): Not correctly solved yet.')
        else:
            print('Solution day ' + str(self.day) + ' (part 1): ' + str(sol1))
        if sol2 is None:
            print('Solution day ' + str(self.day) + ' (part 2): Not correctly solved yet.')
        else:
            print('Solution day ' + str(self.day) + ' (part 2): ' + str(sol2))
