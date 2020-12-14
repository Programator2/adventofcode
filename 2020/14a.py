from aocd import submit
from aoc import *
from collections import defaultdict
import re


def submita(answer):
    submit(answer, part="a", day=14, year=2020)


def submitb(answer):
    submit(answer, part="b", day=14, year=2020)


FILE = "14_test.txt"
FILE = "14.txt"


def main():
    inp = lines(FILE)
    mask = 0
    memory = defaultdict(lambda x: 0)
    for l in inp:
        if l[:2] == "ma":
            mask = l[7:]
        elif l[:2] == "me":
            x = re.search("^mem\[(\d+)\] = (\d+)$", l)
            addr = int(x[1])
            val = int(x[2])
            val_b = f"{val:036b}"
            new = ""
            for a, b in zip(mask, val_b):
                if a != "X":
                    new += a
                else:
                    new += b
            memory[addr] = int(new, 2)
    out = sum(memory.values())
    print(out)
    return
    input()
    print("submitting")
    submita(out)


main()
