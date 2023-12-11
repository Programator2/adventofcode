from aoc import *
from itertools import pairwise


def main(input_file: str):
    inp = lines(input_file)
    inp = [[int(i) for i in x.split()] for x in inp]
    suma = 0
    for i in inp:
        a = [i]
        while not all(x == 0 for x in a[-1]):
            new = []
            for c, d in pairwise(a[-1]):
                new.append(d - c)
            a.append(new)
        first = 0
        for x in reversed(a[:-1]):
            first = x[0] - first
        suma += first
    return suma


DAY = 9
FILE_TEST = f"{DAY}_test.txt"
FILE_EXP = f"{DAY}_exp.txt"
FILE = f"{DAY}.txt"
# test_and_submit(main, FILE_TEST, FILE_EXP, FILE)
print(main(FILE_TEST))
print(main(FILE))
