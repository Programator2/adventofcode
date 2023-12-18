from aoc import *
import re
import sys


D = {'U': (-1, 0), 'D': (1, 0), 'L': (0, -1), 'R': (0, 1)}


def fill(x: int, y: int, edge: dict, filled: dict):
    for dx, dy in D.values():
        if (x + dx, y + dy) in edge:
            continue
        if (x + dx, y + dy) in filled:
            continue
        filled[(x + dx, y + dy)] = '#'
        fill(x + dx, y + dy, edge, filled)

def main(input_file: str):
    sys.setrecursionlimit(20000)
    inp = lines(input_file)
    d = {}
    start = (0, 0)
    for l in inp:
        m = re.match(r'^(.) (\d+) \(#.+\)$', l)
        di, le = m[1], int(m[2])
        for i in range(le):
            dx, dy = D[di]
            start = (start[0] + dx, start[1] + dy)
            d[start] = '#'
    # Had to determine this point by inspecting the shape (see below)
    start = (-183, -8)
    filled = {start: '#'}
    fill(*start, d, filled)
    return len(d) + len(filled)

    # min_x = min(x for x, _ in d)
    # max_x = max(x for x, _ in d)
    # min_y = min(x for _, x in d)
    # max_y = max(x for _, x in d)
    # for x in range(min_x, max_x + 1):
    #     for y in range(min_y, max_y + 1):
    #         if (x, y) == start:
    #             print('*', end='')
    #             continue
    #         if (x, y) in d or (x, y) in filled:
    #             print('#', end='')
    #         else:
    #             print('.', end='')
    #     print()


DAY = 18
FILE_TEST = f"{DAY}_test.txt"
FILE_EXP = f"{DAY}_exp.txt"
FILE = f"{DAY}.txt"
# test_and_submit(main, FILE_TEST, FILE_EXP, FILE, DAY)
# print(main(FILE_TEST))
print(main(FILE))
