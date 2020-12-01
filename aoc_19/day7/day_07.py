"""--- Day 7: Amplification Circuit ---"""
from itertools import permutations

from day5.day_05 import *

prog_str = open("input.txt").read().split(",")
prog = [int(val) for val in prog_str]


def output_signal():
    all_outputs = []
    possible_phase_sets = permutations([0, 1, 2, 3, 4])
    for phase_tupel in possible_phase_sets:
        amp_out = 0
        for phase in list(phase_tupel):
            amp_out = get_ouptut([phase, amp_out])
        all_outputs.append(amp_out)

    return max(all_outputs)


def get_ouptut(input):
    return intcode_computer(prog.copy(), input)[0]  # amplifier should continue with his prog until it halts


# awnser 1
print(output_signal())


def feedback_loop():
    outputs = []
    amplifiers = []
    possible_phase_settings = permutations(range(5, 10))
    for phase_setting in possible_phase_settings:
        for phase in list(phase_setting):
            amplifiers.append(Amlifier(phase, prog.copy()))
        amplifiers[0].input.append(0)
        while not amplifiers[-1].finished:
            for idx, amp in enumerate(amplifiers):
                amp.run_opcode()
                amplifiers[(idx + 1) % 5].input.append(amp.signal)
        outputs.append(amplifiers[-1].signal)
        amplifiers.clear()
    return max(outputs)


class Amlifier:

    def __init__(self, input, prog):
        self.input = [input]
        self.prog = prog
        self.prog_idx = 0
        self.input_idx = 0
        self.signal = None
        self.finished = False

    def run_opcode(self):
        outputs = intcode_computer_modified(self.prog, self.input, self.prog_idx, self.input_idx)
        if outputs[0] == "finish":
            self.finished = True
        else:
            self.prog_idx = outputs[0]
            self.input_idx = outputs[1]
            self.signal = outputs[2]


def intcode_computer_modified(prog, input, prog_idx, input_idx):
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
            output = params[0]
            prog_idx += step
            return [prog_idx, input_idx, output]
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
    return ["finish"]


# awnser 2
print(feedback_loop())
