from aocd import submit
from aoc import *
from functools import cache


FILE = "6_test.txt"
FILE = "6.txt"


@cache
def compute2(time):
    if time <= 0:
        return 1
    return 1 + sum(compute2(time-i) for i in range(9, time+1, 7))


def compute_start(time, left):
    if time <= 0:
        return 1
    return 1 + sum(compute2(time-i) for i in range(left + 1, time+1, 7))


def main():
    inp = load_ints_split(FILE, ',')
    count = sum(compute_start(256, i) for i in inp)
    print(count)
    return
    input()
    print("submitting")
    submit(count)


main()
