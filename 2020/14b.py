from aocd import submit
from aoc import *
from collections import defaultdict
import re
from itertools import product


def submita(answer):
    submit(answer, part="a", day=14, year=2020)


def submitb(answer):
    submit(answer, part="b", day=14, year=2020)


FILE = "14_test2.txt"
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
            addr_b = f"{addr:036b}"
            val = int(x[2])
            new = ""
            x_positions = []
            for i, (a, b) in enumerate(zip(mask, addr_b)):
                if a == "0":
                    new += b
                elif a == "1":
                    new += "1"
                elif a == "X":
                    x_positions.append(35 - i)
                    new += "0"
            new_addr = int(new, 2)
            for p in product("01", repeat=len(x_positions)):
                produced_address = new_addr
                for bit, pos in zip(p, x_positions):
                    if bit == "1":
                        produced_address += 2 ** pos
                memory[produced_address] = int(val)
    out = sum(memory.values())
    print(out)
    return
    input()
    print("submitting")
    submitb(out)


main()
