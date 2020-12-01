"""Day 5: Sunny with a Chance of Asteroids"""

prog_str = open("input.txt").read().split(",")
prog = [int(val) for val in prog_str]


def intcode_computer(prog, input):
    prog_idx = 0
    input_idx = 0
    output = []
    while prog[prog_idx] != 99:
        opcode = get_opcode([prog[prog_idx]])[0]
        step = get_step(opcode)
        res_idx = prog[prog_idx + step - 1]
        param_modes = get_param_modes(prog[prog_idx], step)
        params = get_params(prog, prog_idx, param_modes)
        if opcode == 3:  # stores input on address res_idx
            prog[res_idx] = input[input_idx]
            input_idx = input_idx + 1
        elif opcode == 1:
            prog[res_idx] = params[0] + params[1]
        elif opcode == 2:
            prog[res_idx] = params[0] * params[1]
        elif opcode == 4:
            output.append(params[0])
        elif opcode == 5:
            if params[0]:
                step = params[1] - prog_idx
        elif opcode == 6:
            if params[0] == 0:
                step = params[1] - prog_idx
        elif opcode == 7:
            if params[0] < params[1]:
                prog[res_idx] = 1
            else:
                prog[res_idx] = 0
        elif opcode == 8:
            if params[0] == params[1]:
                prog[res_idx] = 1
            else:
                prog[res_idx] = 0
        prog_idx += step
    return output


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


def get_params(prog, curr_idx, param_modes):
    params = []
    for i, val in enumerate(param_modes):
        if param_modes[i] == 0:
            params += [prog[prog[curr_idx + i + 1]]]
        else:
            params += [prog[curr_idx + i + 1]]
    return params


# awser part1 / part2
print(intcode_computer(prog, [5]))
