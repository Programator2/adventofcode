from aoc import *
from operator import mul, add
from functools import reduce


def main(infi: str):
    inp = lines_stripped(infi)
    nums = []
    s = 0
    for a in inp[:-1]:
        nums.append([int(x) for x in a.split()])
    for i, op in enumerate(inp[-1].split()):
        if op == '*':
            op = mul
        else:
            op = add
        s += reduce(op, [x[i] for x in nums])
    return s


DAY = 6
FILE_TEST = f"{DAY}_testa.txt"
# FILE_TEST = f"{DAY}_testb.txt"
FILE_EXP = f"{DAY}_expa.txt"
FILE = f"{DAY}.txt"
# test_and_submit(main, FILE_TEST, FILE_EXP, FILE, DAY)
# print(main(FILE_TEST))
print(main(FILE))
