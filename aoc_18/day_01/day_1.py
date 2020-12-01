
file = open('./input.txt')
input = file.read().split('\n')


def get_freq():
    curr_freq = 0
    for freq_change in input:
        curr_freq += int(freq_change)
    return curr_freq

def get_first_reached_twice():
    freqs = set()
    curr_freq = 0
    while 1:
        for freq_change in input:
            freqs.add(curr_freq)
            curr_freq += int(freq_change)
            if curr_freq in freqs:
                return curr_freq


# solution 1
print(get_freq())

# solution 2
print(get_first_reached_twice())
