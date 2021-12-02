from aocd import submit
from aoc import *
import re


FILE = "2_test.txt"
FILE = "2.txt"


def main():
    inp = lines(FILE)
    pos = [0, 0]
    aim = 0
    for l in inp:
        x = re.search('^(.*) (\d*)$', l)
        if x[1] == 'forward':
            pos[0] += int(x[2])
            pos[1] += aim*int(x[2])
        if x[1] == 'down':
            aim += int(x[2])
        if x[1] == 'up':
            aim -= int(x[2])
    result = pos[0] * pos[1]
    print(result)
    return
    input()
    print("submitting")
    submit(result)


main()
