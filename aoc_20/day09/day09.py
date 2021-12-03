import time

start = time.process_time()

with open("9.in") as f:
    data = []
    for number in f.readlines():
        data.append(int(number.replace("\n", "")))


def check_rule(preamble, to_check):
    for a in preamble:
        for b in preamble:
            if a > to_check or b > to_check:
                continue
            if a + b == to_check:
                return True
    return False


def find_first_rule_breaker():
    idx = 0
    while 1:
        preamble = data[idx:(idx + 25)]
        to_check = data[idx + 25]
        if not check_rule(preamble, to_check):
            return to_check
        idx += 1


breaker = find_first_rule_breaker()
print("Awnser 1: %d" % breaker)


def find_contiguous_set():
    num = breaker
    start_idx = 0
    while 1:
        for steps in range(1, len(data)):
            sum1 = sum(data[start_idx:start_idx + steps])
            if sum1 == num:
                return min(data[start_idx:start_idx + steps]) + max(data[start_idx:start_idx + steps])
            if sum1 > num:
                break
        start_idx += 1


print("Awnser 2: %d" % (find_contiguous_set()))

print("took: %lf seconds" % (time.process_time() - start))
