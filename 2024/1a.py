from aoc import *


def main(infi: str):
    inp = lines_stripped(infi)
    le = []
    ri = []
    for a in inp:
        i, j = a.split()
        le.append(int(i))
        ri.append(int(j))
    le.sort()
    ri.sort()
    s = 0
    for a, b in zip(le, ri):
        s += abs(a - b)
    return s


DAY = 1
FILE_TEST = f"{DAY}_testa.txt"
# FILE_TEST = f"{DAY}_testb.txt"
FILE_EXP = f"{DAY}_exp.txt"
FILE = f"{DAY}.txt"
# test_and_submit(main, FILE_TEST, FILE_EXP, FILE, DAY)
# print(main(FILE_TEST))
print(main(FILE))
