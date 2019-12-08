"""Day 4: Secure Container"""

range_min = 402328
range_max = 864247


def calc_number_of_pwds():
    valids = 0
    # check validity
    for num in range(range_min, range_max):
        adjacent, increases = False, False
        curr_pwd_list = [int(number) for number in str(num)]
        if curr_pwd_list == sorted(curr_pwd_list):
            increases = True
        else:
            continue
        if len(curr_pwd_list) > len(set(curr_pwd_list)):
            if part2:
                num_dublicates = [curr_pwd_list.count(val) for val in curr_pwd_list]
                adjacent = 2 in num_dublicates
            else: adjacent = True
        if adjacent and increases:
            valids += 1
    return valids


# awnser part1
part2 = False
print("The number of valid passwords is: ", calc_number_of_pwds())

# awnser part2
part2 = True
print("The new number of valid password is: ", calc_number_of_pwds())
