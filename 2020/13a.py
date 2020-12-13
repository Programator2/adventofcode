from aocd import submit
from aoc import *
from math import sqrt


def submita(answer):
    submit(answer, part="a", day=13, year=2020)


def submitb(answer):
    submit(answer, part="b", day=13, year=2020)


FILE = "13_test.txt"
FILE = "13.txt"


def main():
    inp = lines(FILE)
    out = 0
    minutes = int(inp[0])
    busses_s = inp[1].split(",")
    busses = []
    for b in busses_s:
        try:
            a = int(b)
            busses.append(a)
        except:
            continue
    wait = []
    for b in busses:
        how_much_to_wait = b - (minutes + b) % b
        if how_much_to_wait == b:
            how_much_to_wait = 0
        wait.append((b, how_much_to_wait))
        print(wait[-1])
    min_ = min(wait, key=lambda x: x[1])
    out = min_[0] * min_[1]
    print(out)
    return
    input()
    print("submitting")
    submita(out)


main()
