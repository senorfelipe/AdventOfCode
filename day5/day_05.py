"""Day 5: Sunny with a Chance of Asteroids"""

diag_prog_str = open("input.txt").read().split(",")
# diag_prog_str = "1002,4,3,4,33".split(",")
diag_prog = [int(val) for val in diag_prog_str]
print(diag_prog)


def opcode_program():
    instruction = get_instruction([diag_prog[0]])
    step = get_step(instruction)
    i = 0
    while i + step <= len(diag_prog) and (diag_prog[i] != 99):
        instruction = get_instruction([diag_prog[i]])[0]
        step = get_step(instruction)
        res_idx = diag_prog[i + step - 1]
        param_modes = get_param_modes(diag_prog[i], step)
        params = get_params(i, param_modes)
        if instruction == 3:
            input = 1
            diag_prog[res_idx] = input
        elif instruction == 1:
            diag_prog[res_idx] = params[0] + params[1]
        elif instruction == 2:
            diag_prog[res_idx] = params[0] * params[1]
        elif instruction == 4:
            print(params[0])
        i += step


def get_step(instruction):
    if instruction == 3 or instruction == 4:
        return 2
    else:
        return 4


def get_instruction(number_with_instr):
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



# awser part1
print(get_param_modes(1101, 4))
print(opcode_program())
