import time

start = time.process_time()

data = []
with open("11.in") as f:
    for line in f.readlines():
        data.append([a for a in line if a != "\n"])


def simulate(curr_state):
    new_state = list(curr_state)
    for i in range(len(curr_state)):
        for j in range(len(curr_state[i])):
            if curr_state[i][j] == ".":
                continue
            elif is_empty([i][j]):
                pass

    return new_state


def is_empty(letter):
    return letter == "L"


def simulate_seating_area():
    while 1:
        simulate()


print(data)

print("took: %lf seconds" % (time.process_time() - start))
