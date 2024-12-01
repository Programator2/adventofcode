from aoc import *
from collections import Counter


def main(infi: str):
    inp = lines_stripped(infi)
    le = []
    ri = Counter()
    for a in inp:
        i, j = a.split()
        le.append(int(i))
        ri[int(j)] += 1
    le.sort()
    s = 0
    for a in le:
        s += a * ri[a]
    return s


DAY = 1
FILE_TEST = f"{DAY}_testb.txt"
FILE_EXP = f"{DAY}_exp.txt"
FILE = f"{DAY}.txt"
# test_and_submit(main, FILE_TEST, FILE_EXP, FILE, DAY)
# print(main(FILE_TEST))
print(main(FILE))
