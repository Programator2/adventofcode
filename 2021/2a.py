from aocd import submit
from aoc import *
import re


FILE = "2_test.txt"
FILE = "2.txt"


def main():
    inp = lines(FILE)
    pos = [0, 0]
    for l in inp:
        x = re.search('^(.*) (\d*)$', l)
        if x[1] == 'forward':
            pos[0] += int(x[2])
        if x[1] == 'down':
            pos[1] += int(x[2])
        if x[1] == 'up':
            pos[1] -= int(x[2])
    count = pos[0] * pos[1]
    print(count)
    return
    input()
    print("submitting")
    submit(count)


main()
