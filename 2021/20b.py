from aoc import *
from collections import defaultdict


def grow(m, alg, left, right, top, bottom):
    newm = defaultdict(lambda: '.')
    for row in range(top, bottom):
        for col in range(left, right):
            el = ''.join((m[row-1, col-1], m[row-1, col], m[row-1, col+1],
                          m[row, col-1], m[row, col], m[row, col+1],
                          m[row+1, col-1], m[row+1, col], m[row+1, col+1]))
            el = el.replace('#', '1')
            el = el.replace('.', '0')
            elnum = int(el, 2)
            elalg = alg[elnum]
            newm[row, col] = elalg
    return newm


def main(input_file: str):
    print()
    inp = file(input_file).rstrip()
    alg, inp = inp.split('\n\n')
    m = defaultdict(lambda: '.')
    rows = inp.split('\n')
    for row, i in enumerate(rows):
        for ei, e in enumerate(i):
            m[(row, ei)] = e
    left = 0
    right = len(rows[0])
    top = 0
    bottom = len(rows)
    for i in range(50):
        left -= 2
        top -= 2
        bottom += 2
        right += 2
        m.default_factory = (lambda: alg[0]) if i % 2 else (lambda: alg[-1])
        m = grow(m, alg, left, right, top, bottom)
        # for row in range(top, bottom):
            # for col in range(left, right):
                # print(m[row, col], end='')
            # print()
        # print()
    out = sum(1 for el in m.values() if el == '#')
    return out


DAY = 20
FILE_TEST = f"{DAY}_test.txt"
FILE_EXP = f"{DAY}_exp.txt"
FILE = f"{DAY}.txt"
# test_and_submit(main, FILE_TEST, FILE_EXP, FILE)
# print(main(FILE_TEST))
print(main(FILE))
