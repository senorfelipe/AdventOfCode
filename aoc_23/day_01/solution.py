from shared.advent_of_code import AoCSolution


class Day01(AoCSolution):
    DIGIT_STRINGS = (
        ("one", "1"),
        ("two", "2"),
        ("three", "3"),
        ("four", "4"),
        ("five", "5"),
        ("six", "6"),
        ("seven", "7"),
        ("eight", "8"),
        ("nine", "9"),
    )

    def part_one(self):
        sum = 0
        for line in self.input_lines:
            first_digit, last_digit = None, None
            for i in range(1, len(line) + 1):
                if line[i - 1].isdigit() and first_digit is None:
                    first_digit = line[i - 1]
                if line[-i].isdigit() and last_digit is None:
                    last_digit = line[-i]
                if first_digit and last_digit:
                    print(f"first: {first_digit} last: {last_digit}")
                    sum += int(first_digit + last_digit)
                    break
        return sum

    def part_two(self):
        sum = 0
        for line in self.input_lines:
            first_digit, last_digit = None, None
            for i in range(1, len(line) + 1):
                if line[-i].isdigit() and last_digit is None:
                    last_digit = line[-i]

                for str, digit in self.DIGIT_STRINGS:
                    if line.find(str, 0, i - 1) != -1 and first_digit is None:
                        first_digit = digit
                    if line.find(str, -i, len(line) + 1) != -1 and last_digit is None:
                        last_digit = digit

                if line[i - 1].isdigit() and first_digit is None:
                    first_digit = line[i - 1]

                if first_digit and last_digit:
                    print(f"first: {first_digit} last: {last_digit}")
                    sum += int(first_digit + last_digit)
                    break
        return sum


Day01(1, "./input.txt").solve()
