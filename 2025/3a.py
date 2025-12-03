from aoc import *
from itertools import combinations


def main(infi: str):
    inp = lines_stripped(infi)
    s = 0
    for a in inp:
        s += max([int(''.join(x)) for x in combinations(a, 2)])
    return s


DAY = 3
FILE_TEST = f"{DAY}_test.txt"
# FILE_TEST = f"{DAY}_testb.txt"
FILE_EXP = f"{DAY}_exp.txt"
FILE = f"{DAY}.txt"
# test_and_submit(main, FILE_TEST, FILE_EXP, FILE, DAY)
# print(main(FILE_TEST))
print(main(FILE))
