from aocd import submit
from aoc import *
import re
from collections import Counter
from copy import deepcopy


FILE = "5_test.txt"
FILE = "5.txt"


def my_range(start, stop):
    # stop is included
    s = start
    while True:
        yield s
        if stop < start:
            s -= 1
        else:
            s += 1
        if s == stop:
            yield s
            return


def main():
    inp = lines(FILE)
    d = Counter()
    for l in inp:
        a = re.match('^(\d+),(\d+) -> (\d+),(\d+)$', l)
        x1, y1, x2, y2 = int(a[1]), int(a[2]), int(a[3]), int(a[4])
        if x1 == x2:
            for y in range(min(y1, y2), max(y1, y2)+1):
                d[(x1, y)] += 1
        elif y1 == y2:
            for x in range(min(x1, x2), max(x1, x2)+1):
                d[(x, y1)] += 1
        else:
            for x, y in zip(my_range(x1, x2), my_range(y1, y2)):
                d[(x, y)] += 1
            # Originally, I used this:
            # x = x1
            # y = y1
            # while True:
            #     # print(f'{x}, {y}')
            #     d[(x, y)] += 1
            #     if x == x2:
            #         break
            #     if x1 > x2:
            #         x -= 1
            #     else:
            #         x += 1
            #     if y1 > y2:
            #         y -= 1
            #     else:
            #         y += 1


    count = 0
    for k, v in d.items():
        if v > 1:
            count += 1
    print(count)
    return
    input()
    print("submitting")
    submit(count)


main()
