from aocd import submit
from aoc import *
from math import sqrt


def submita(answer):
    submit(answer, part="a", day=12, year=2020)


def submitb(answer):
    submit(answer, part="b", day=12, year=2020)


FILE = "12_test.txt"
FILE = "12.txt"


def main():
    inp = lines(FILE)
    cur_dir = 0
    directions = ["E", "N", "W", "S"]
    x = 0
    y = 0
    for i in inp:
        dire = i[0]
        val = int(i[1:])
        if dire == "F":
            dire = directions[cur_dir]
        if dire == "N":
            y += val
        elif dire == "S":
            y -= val
        elif dire == "E":
            x += val
        elif dire == "W":
            x -= val
        elif dire == "L":
            cur_dir = (cur_dir + val // 90) % len(directions)
        elif dire == "R":
            cur_dir = (cur_dir - val // 90) % len(directions)
        print(x, y)
    out = abs(x) + abs(y)
    print(out)
    input()
    print("submitting")
    submita(out)


main()
