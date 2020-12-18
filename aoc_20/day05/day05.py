import time

start = time.process_time()

input = open("5.in").read().split("\n")


def calc_row(row):
    first, last = 0, 127
    for letter in row:
        diff = (last - first) // 2
        if diff == 0: return first if letter == "F" else last
        if letter == "F":
            last = first + diff
        if letter == "B":
            first = last - diff


def calc_col(col):
    first, last = 0, 7
    for letter in col:
        diff = (last - first) // 2
        if diff == 0: return first if letter == "L" else last
        if letter == "L":
            last = first + diff
        if letter == "R":
            first = last - diff


def highest_id():
    highest = 0
    for seat in input:
        row = calc_row(seat[0:7])
        col = calc_col(seat[7:])
        seat_id = (row * 8) + col
        highest = seat_id if seat_id > highest else highest
    return highest


def find_my_seat():
    missing_seats = {}
    seats = {k: [] for k in range(0, 127)}
    for seat in input:
        seats[calc_row(seat[0:7])].append(calc_col(seat[7:]))
    for row in seats.keys():
        if len(seats[row]) != 8 and len(seats[row]) != 0:
            missing_seats[row] = seats[row]
    return [(row * 8) + col[0] for (row, col) in missing_seats.items() if
            row not in [min(missing_seats.keys()), max(missing_seats.keys())] and col not in range(0, 7)][0]


print("Awnser 1: %d" % highest_id())

print("Awnser 2: %s" % (find_my_seat()))

print("took: %f seconds" % (time.process_time() - start))
