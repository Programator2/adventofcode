from aoc import *
import re
from itertools import product


def main(infi: str):
    inp = filerstrip(infi)
    machines = []
    for machine in inp.split('\n\n'):
        lines = machine.split('\n')
        a = re.fullmatch(r'Button A: X\+(.*?), Y\+(.*?)', lines[0])
        b = re.fullmatch(r'Button B: X\+(.*?), Y\+(.*?)', lines[1])
        prize = re.fullmatch(r'Prize: X=(.*?), Y=(.*?)', lines[2])
        machines.append(
            (
                (int(a[1]), int(a[2])),
                (int(b[1]), int(b[2])),
                (int(prize[1]), int(prize[2])),
            )
        )
    tokens_needed = 0
    INITIAL = 999999999999999999
    for machine in machines:
        tokens = INITIAL
        for a, b in product(range(1, 101), range(1, 101)):
            x = a * machine[0][0] + b * machine[1][0]
            y = a * machine[0][1] + b * machine[1][1]
            if (x, y) == machine[2]:
                tokens = min(tokens, a * 3 + b * 1)
        if tokens != INITIAL:
            tokens_needed += tokens
    return tokens_needed



DAY = 13
FILE_TEST = f"{DAY}_testa.txt"
# FILE_TEST = f"{DAY}_testb.txt"
FILE_EXP = f"{DAY}_exp.txt"
FILE = f"{DAY}.txt"
# test_and_submit(main, FILE_TEST, FILE_EXP, FILE, DAY)
# print(main(FILE_TEST))
print(main(FILE))
