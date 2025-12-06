from aoc import *
from operator import mul, add
from functools import reduce


def main(infi: str):
    inp = lines_stripped(infi)
    count = 0
    widths = []
    starts = []
    operators = []
    for i, c in enumerate(inp[-1]):
        if c != ' ':
            widths.append(count)
            count = 0
            starts.append(i)
            operators.append(mul if c == '*' else add)
        else:
            count += 1
    widths.append(count + 1)
    widths = widths[1:]
    inp = inp[:-1]
    return sum(
        reduce(
            op,
            [
                int(
                    ''.join(
                        row[i]
                        for row in [row[start : width + start] for row in inp]
                    )
                )
                for i in range(width - 1, -1, -1)
            ],
        )
        for width, start, op in zip(widths, starts, operators)
    )


DAY = 6
FILE_TEST = f"{DAY}_testa.txt"
# FILE_TEST = f"{DAY}_testb.txt"
FILE_EXP = f"{DAY}_expa.txt"
FILE = f"{DAY}.txt"
# test_and_submit(main, FILE_TEST, FILE_EXP, FILE, DAY)
# print(main(FILE_TEST))
print(main(FILE))
# cca 1583   3853  **
