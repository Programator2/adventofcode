from aocd import submit
from aoc import *


def submita(answer):
    submit(answer, part="a", day=12, year=2020)


def submitb(answer):
    submit(answer, part="b", day=12, year=2020)


FILE = "12_test.txt"
FILE = "12.txt"


def main():
    inp = lines(FILE)
    x = 0
    y = 0
    wx = 10
    wy = 1
    for i in inp:
        dire = i[0]
        val = int(i[1:])
        if dire == "F":
            x += wx * val
            y += wy * val
        if dire == "N":
            wy += val
        elif dire == "S":
            wy -= val
        elif dire == "E":
            wx += val
        elif dire == "W":
            wx -= val
        elif dire == "L":
            for _ in range(val // 90):
                wx, wy = wy * -1, wx
        elif dire == "R":
            for _ in range(val // 90):
                wx, wy = wy, wx * -1
    out = abs(x) + abs(y)
    print(out)
    return
    input()
    print("submitting")
    submitb(out)


main()
