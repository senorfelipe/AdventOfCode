
def normalize():
    return line.replace(':', '').replace('\n', '').split(' ')


counter_one = 0
for line in open('2.txt').readlines():
    line = normalize()
    limits = list(map(int, line[0].split('-')))
    policy_limits = range(limits[0], limits[1])
    policy_letter = line[1]
    number_of_letters_in_pwd = len([letter for letter in line[2] if letter == policy_letter])
    if policy_limits.start <= number_of_letters_in_pwd <= policy_limits.stop:
        counter_one += 1

# part 1
print(counter_one)

counter_two = 0
for line in open('2.txt').readlines():
    line = normalize()
    policy_idxs = list(map(int, line[0].split('-')))
    policy_letter = line[1]
    pwd = line[2]
    letters_at_idxs = [pwd[policy_idxs[0] - 1], pwd[policy_idxs[1] - 1]]
    if 1 == len([letter for letter in letters_at_idxs if letter == policy_letter]):
        counter_two += 1

# part 2
print(counter_two)
