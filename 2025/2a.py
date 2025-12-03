from aoc import *
from math import ceil


def main(infi: str):
    ranges = filerstrip(infi).split(',')
    s = 0
    for r in ranges:
        a, b = r.split('-')
        for x in range(int(a), int(b) + 1):
            digits = int(math.log10(x)) + 1
            if digits % 2 == 0:
                numstr = str(x)
                if numstr[: len(numstr) // 2] == numstr[len(numstr) // 2 :]:
                    s += x
    return s


DAY = 2
FILE_TEST = f"{DAY}_test.txt"
# FILE_TEST = f"{DAY}_testb.txt"
FILE_EXP = f"{DAY}_exp.txt"
FILE = f"{DAY}.txt"
# test_and_submit(main, FILE_TEST, FILE_EXP, FILE, DAY)
# print(main(FILE_TEST))
print(main(FILE))
