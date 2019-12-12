"""Day 5: Sunny with a Chance of Asteroids"""

diag_prog_str = open("input.txt").read().split(",")
diag_prog = [int(val) for val in diag_prog_str]


def opcode_program():
    i = 0
    while diag_prog[i] != 99:
        opcode = get_opcode([diag_prog[i]])[0]
        step = get_step(opcode)
        res_idx = diag_prog[i + step - 1]
        param_modes = get_param_modes(diag_prog[i], step)
        params = get_params(i, param_modes)
        if opcode == 3:
            input = 5
            diag_prog[res_idx] = input
        elif opcode == 1:
            diag_prog[res_idx] = params[0] + params[1]
        elif opcode == 2:
            diag_prog[res_idx] = params[0] * params[1]
        elif opcode == 4:
            print(params[0])
        elif opcode == 5:
            if params[0]:
                step = params[1] - i
        elif opcode == 6:
            if params[0] == 0:
                step = params[1] - i
        elif opcode == 7:
            if params[0] < params[1]:
                diag_prog[res_idx] = 1
            else:
                diag_prog[res_idx] = 0
        elif opcode == 8:
            if params[0] == params[1]:
                diag_prog[res_idx] = 1
            else:
                diag_prog[res_idx] = 0
        i += step


def get_step(opcode):
    if opcode == 3 or opcode == 4:
        return 2
    elif opcode == 5 or opcode == 6:
        return 3
    else:
        return 4


def get_opcode(number_with_instr):
    if any(c in number_with_instr for c in (1, 2, 3, 4)):
        return number_with_instr
    else:
        return [int(str(number_with_instr)[-2:-1])]


def get_param_modes(number_with_param_modes, step):
    ret = []
    for i in range(step - 1):
        ret += [0]
    num_list = str(number_with_param_modes)[:-2]
    for j, val in enumerate(num_list[::-1]):
        ret[j] = int(val)
    return ret


def get_params(curr_idx, param_modes):
    params = []
    for i, val in enumerate(param_modes):
        if param_modes[i] == 0:
            params += [diag_prog[diag_prog[curr_idx + i + 1]]]
        else:
            params += [diag_prog[curr_idx + i + 1]]
    return params


# awser part1 / part2
opcode_program()
