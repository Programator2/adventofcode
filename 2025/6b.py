from aoc import *
from operator import mul, add
from functools import reduce


def main(infi: str):
    inp = lines_stripped(infi)
    count = 0
    widths = []
    starts = []
    operators = []
    s = 0
    for i, c in enumerate(inp[-1]):
        if c != ' ':
            widths.append(count)
            count = 0
            starts.append(i)
            if c == '*':
                op = mul
            else:
                op = add
            operators.append(op)
        else:
            count += 1
    widths.append(count + 1)
    widths = widths [1:]
    inp = inp[:-1]
    for width, start, op in zip(widths, starts, operators):
        sub = [row[start:width+start] for row in inp]
        newsub = []
        for i in range(width - 1, -1, -1):
            st = ''
            for row in sub:
                st += row[i]
            newsub.append(int(st))
        s += reduce(op, newsub)
    return s


DAY = 6
FILE_TEST = f"{DAY}_testa.txt"
# FILE_TEST = f"{DAY}_testb.txt"
FILE_EXP = f"{DAY}_expa.txt"
FILE = f"{DAY}.txt"
# test_and_submit(main, FILE_TEST, FILE_EXP, FILE, DAY)
# print(main(FILE_TEST))
print(main(FILE))
# cca 1583   3853  **
