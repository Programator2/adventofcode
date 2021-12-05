from aocd import submit
from aoc import *
import re
from collections import Counter


FILE = "5_test.txt"
FILE = "5.txt"


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
    count = 0
    print(d)
    for k, v in d.items():
        if v > 1:
            count += 1
    print(count)
    return
    input()
    print("submitting")
    submit(count)


main()
