from aoc import *
import re
from pprint import pprint as pp
from sympy.solvers.solveset import linsolve
from sympy import symbols, core


def main(infi: str):
    inp = filerstrip(infi)
    tokens = 0
    for machine in inp.split('\n\n'):
        lines = machine.split('\n')
        ax, ay = map(
            int,
            re.fullmatch(r'Button A: X\+(.*?), Y\+(.*?)', lines[0]).groups(),
        )
        bx, by = map(
            int,
            re.fullmatch(r'Button B: X\+(.*?), Y\+(.*?)', lines[1]).groups(),
        )
        px, py = map(
            int, re.fullmatch(r'Prize: X=(.*?), Y=(.*?)', lines[2]).groups()
        )
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
