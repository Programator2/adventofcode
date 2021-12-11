from aoc import *
from collections import defaultdict


def flash(x, y, octo):
    octo[(x+1, y)][0] += 1
    octo[(x+1, y+1)][0] += 1
    octo[(x, y+1)][0] += 1
    octo[(x, y-1)][0] += 1
    octo[(x-1, y)][0] += 1
    octo[(x-1, y-1)][0] += 1
    octo[(x-1, y+1)][0] += 1
    octo[(x+1, y-1)][0] += 1


def main(input_file: str):
    inp = load_map(input_file)
    octo = defaultdict(lambda: [0, False])
    for r, row in enumerate(inp):
        for ei, e in enumerate(row):
            octo[(ei, r)] = [int(e), False]
    it = 0
    while True:
        for j in range(len(inp)):
            for k in range(len(inp[0])):
                octo[(k, j)][0] += 1
        flashing = True
        while flashing:
            flashing = False
            for j in range(len(inp)):
                for k in range(len(inp[0])):
                    if octo[(k, j)][0] > 9 and not octo[(k, j)][1]:
                        flashing = True
                        octo[(k, j)][1] = True
                        flash(k, j, octo)
        it += 1
        if out == len(inp) * len(inp[0]):
            return it
        for j in range(len(inp)):
            for k in range(len(inp[0])):
                if octo[(k, j)][1]:
                    octo[(k, j)][0] = 0
                    octo[(k, j)][1] = False


DAY = 11
FILE_TEST = f"{DAY}_test.txt"
FILE_EXP = f"{DAY}_exp.txt"
FILE = f"{DAY}.txt"
# test_and_submit(main, FILE_TEST, FILE_EXP, FILE)
print(main(FILE))
