from aoc import *
import re
from pprint import pprint as pp
from sympy.solvers.solveset import linsolve
from sympy import symbols, core


def parse_input(infi: str):
    return [
        (
            *map(
                int,
                re.fullmatch(
                    r'Button A: X\+(.*?), Y\+(.*?)', machine.split('\n')[0]
                ).groups(),
            ),
            *map(
                int,
                re.fullmatch(
                    r'Button B: X\+(.*?), Y\+(.*?)', machine.split('\n')[1]
                ).groups(),
            ),
            *map(
                int,
                re.fullmatch(
                    r'Prize: X=(.*?), Y=(.*?)', machine.split('\n')[2]
                ).groups(),
            ),
        )
        for machine in filerstrip(infi).split('\n\n')
    ]


# arithmetic solution for mY
def main_arithmetic(infi: str):
    tokens = 0
    for ax, ay, bx, by, px, py in parse_input(infi):
        a, mod = divmod(
            by * (px + 10**13) - bx * (10**13 + py), ax * by - ay * bx
        )
        if mod == 0 and a > 0:
            b, mod = divmod(py + 10**13 - a * ay, by)
            if mod == 0 and b > 0:
                tokens += 3 * a + b
    return tokens


def main(infi: str):
    tokens = 0
    for ax, ay, bx, by, px, py in parse_input(infi):
        a, b = symbols('a, b', integer=True, positive=True)
        system = (
            ax * a + bx * b - px - 10000000000000,
            ay * a + by * b - py - 10000000000000,
        )
        res = linsolve(system, a, b)
        assert len(res) == 1
        solution = next(iter(res))
        if all(
            type(sol) is core.numbers.Integer and sol > 0 for sol in solution
        ):
            tokens += 3 * solution[0] + solution[1]
    return tokens


DAY = 13
FILE_TEST = f"{DAY}_testa.txt"
# FILE_TEST = f"{DAY}_testb.txt"
FILE_EXP = f"{DAY}_exp.txt"
FILE = f"{DAY}.txt"
# test_and_submit(main, FILE_TEST, FILE_EXP, FILE, DAY)
# print(main(FILE_TEST))
print(main(FILE))
print(main_arithmetic(FILE))
