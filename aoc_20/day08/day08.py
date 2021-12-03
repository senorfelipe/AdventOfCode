import time

start = time.process_time()


def create_input():
    instructions = []
    with open("./8.in") as f:
        for i in f.readlines():
            split = i.replace("\n", "").split(" ")
            instructions.append([split[0], int(split[1]), 0])
    return instructions


def acc_value(instrs):
    acc = 0
    idx = 0
    while instrs[idx][2] + 1 <= 1:
        if idx + 1 == len(instrs):
            return acc, True
        instruction = instrs[idx]
        instruction[2] += 1
        if instruction[0] == "jmp":
            idx += instruction[1]
            continue
        idx += 1
        if instruction[0] == "nop":
            continue
        if instruction[0] == "acc":
            acc += instruction[1]
    return acc, False


print("Awnser 1: %d " % (acc_value(create_input())[0]))


def change_instruction(instr_val):
    return "jmp" if instr_val == "nop" else "nop"


def fix_instructions():
    fixed = create_input()
    for instr in fixed:
        instr_val = instr[0]
        if instr_val in ("jmp", "nop"):
            instr[0] = change_instruction(instr_val)
            back = acc_value(fixed)
            res, is_finite = back[0], back[1]
            if not is_finite:
                instr[0] = change_instruction(instr[0])
                for el in fixed:
                    el[2] = 0
            else:
                return res


print("Awnser 2: %d " % (fix_instructions()))

print("took: %f seconds" % (time.process_time() - start))
