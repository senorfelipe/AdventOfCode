import re

pass_str = open('4.txt').read().split('\n\n')


def create_passports_dict(passports):
    pass_dicts = []
    for passport in passports:
        passport = passport.replace('\n', ' ')
        k_v_list = [(a, b) for (a, b) in [tuple(p.split(':')) for p in passport.split(' ')]]
        d = {key: val for (key, val) in k_v_list}
        pass_dicts.append(d)
    return pass_dicts


valid_passports = []


def count_valids_one(passports):
    valid = 0
    valid_keys = {'byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'}
    for passport in passports:
        if valid_keys.issubset(set(passport.keys())):
            valid += 1
            valid_passports.append(passport)
    return valid


# part1
print('Valid passports: ' + str(count_valids_one(create_passports_dict(pass_str))))

# ----------------------------------------- #
valid_pass = []


def count_valids_two(passports):
    valid = 0
    validation_rules = {'byr': '^[0-9]{4}$', 'iyr': '^[0-9]{4}$', 'eyr': '^[0-9]{4}$',
                        'hgt': '^([0-9]{3}cm)$|^([0-9]{2}in)$', 'hcl': '^#([0-9a-f]){6}$',
                        'ecl': '^(amb|blu|brn|gry|grn|hzl|oth)$', 'pid': '^([0-9]{9})$'}
    for passport in passports:
        valid_kv = 0
        for key in passport.keys():
            if key == 'cid':
                valid_kv += 1
                continue
            if bool(re.match(validation_rules[key], passport[key])):
                if key == 'byr' and int(passport[key]) not in range(1920, 2003):
                    break
                if key == 'iyr' and int(passport[key]) not in range(2010, 2021):
                    break
                if key == 'eyr' and int(passport[key]) not in range(2020, 2031):
                    break
                if key == 'hgt':
                    if not ((passport[key][-2:] == 'cm' and int(passport[key][:-2]) in range(150, 194)) or (
                            passport[key][-2:] == 'in' and int(passport[key][:-2]) in range(59, 77))):
                        break
                valid_kv += 1
        if valid_kv == len(passport.keys()):
            valid += 1
    return valid


# part 2
print('Valid passports: ' + str(count_valids_two(valid_passports)))
