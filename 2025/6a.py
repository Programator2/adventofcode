from aoc import *
from operator import mul, add
from functools import reduce


def main(infi: str):
    inp = lines_stripped(infi)
    return sum(
        reduce(
            mul if op == '*' else add,
            [x[i] for x in [[int(x) for x in a.split()] for a in inp[:-1]]],
        )
        for i, op in enumerate(inp[-1].split())
    )


DAY = 6
FILE_TEST = f"{DAY}_testa.txt"
# FILE_TEST = f"{DAY}_testb.txt"
FILE_EXP = f"{DAY}_expa.txt"
FILE = f"{DAY}.txt"
# test_and_submit(main, FILE_TEST, FILE_EXP, FILE, DAY)
# print(main(FILE_TEST))
print(main(FILE))
