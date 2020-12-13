from aocd import submit
from aoc import *
from math import lcm


def submita(answer):
    submit(answer, part="a", day=13, year=2020)


def submitb(answer):
    submit(answer, part="b", day=13, year=2020)


FILE = "13_test.txt"
FILE = "13.txt"


# Implementation of Chinese Remainder Theorem from
# https://rosettacode.org/wiki/Chinese_remainder_theorem#Python_3.6
from functools import reduce


def chinese_remainder(n, a):
    sum = 0
    prod = reduce(lambda a, b: a * b, n)
    for n_i, a_i in zip(n, a):
        p = prod // n_i
        sum += a_i * mul_inv(p, n_i) * p
    return sum % prod


def mul_inv(a, b):
    b0 = b
    x0, x1 = 0, 1
    if b == 1:
        return 1
    while a > 1:
        q = a // b
        a, b = b, a % b
        x0, x1 = x1 - q * x0, x0
    if x1 < 0:
        x1 += b0
    return x1


def main():
    inp = lines(FILE)
    out = 0
    minutes = int(inp[0])
    busses_s = inp[1].split(",")
    busses = []
    args = []
    second = []
    for i, b in enumerate(busses_s, 0):
        try:
            a = int(b)
            busses.append((i, a))
            args.append(a)
            second.append(a - i)
        except:
            continue
    out = chinese_remainder(args, second)
    print(out)
    return
    input()
    print("submitting")
    submitb(out)


main()
