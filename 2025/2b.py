from aoc import *
import math


def main(infi: str):
    ranges = filerstrip(infi).split(',')
    s = 0
    for r in ranges:
        a, b = r.split('-')
        for x in range(int(a), int(b) + 1):
            digits = int(math.log10(x)) + 1
            # Inneficient
            divisors = [
                n for n in range(1, digits // 2 + 1) if digits % n == 0
            ]
            for d in divisors:
                # d is also size of the sequence
                sequences = digits // d
                numstr = str(x)
                for iseq in range(1, sequences):
                    if numstr[:d] != numstr[iseq * d : (iseq + 1) * d]:
                        break
                else:
                    s += x
                    break
    return s


DAY = 2
FILE_TEST = f"{DAY}_test.txt"
# FILE_TEST = f"{DAY}_testb.txt"
FILE_EXP = f"{DAY}_exp.txt"
FILE = f"{DAY}.txt"
# test_and_submit(main, FILE_TEST, FILE_EXP, FILE, DAY)
# print(main(FILE_TEST))
print(main(FILE))
