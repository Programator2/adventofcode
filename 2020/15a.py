from aocd import submit
from aoc import *
from collections import defaultdict


def submita(answer):
    submit(answer, part="a", day=15, year=2020)


def submitb(answer):
    submit(answer, part="b", day=15, year=2020)


FILE = "15_test.txt"
FILE = "15.txt"


def main():
    inp = file(FILE)
    inp = [int(i) for i in inp.split(',')]
    d = defaultdict(list)
    last_spoken = 0
    for i in range(2020):
        if i < len(inp):
            last_spoken = inp[i]
        elif len(d[last_spoken]) == 2:
            last_spoken = d[last_spoken][1] - d[last_spoken][0]
        else:
            last_spoken = 0
        d[last_spoken].append(i)
        if len(d[last_spoken]) > 2:
            del d[last_spoken][0]
    out = last_spoken
    print(out)
    return
    input()
    print("submitting")
    submita(out)


main()
