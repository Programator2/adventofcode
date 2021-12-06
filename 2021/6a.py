from aocd import submit
from aoc import *


FILE = "6_test.txt"
FILE = "6.txt"


def main():
    inp = load_ints_split(FILE, ',')
    for g in range(80):
        new = []
        for ind, i in enumerate(inp):
            i -= 1
            if i == -1:
                new.append(8)
                inp[ind] = 6
            else:
                inp[ind] = i
        inp.extend(new)
    count = len(inp)
    print(count)
    return
    input()
    print("submitting")
    submit(count)


main()
