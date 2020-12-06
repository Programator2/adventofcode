from aocd import submit
import re
from aoc import *


def submita(answer):
    submit(answer, part='a', day=6, year=2020)


def submitb(answer):
    submit(answer, part='b', day=6, year=2020)


FILE = '6_test.txt'
FILE = '6.txt'


def main():
    with open(FILE) as f:
        i = f.read().rstrip()
    i = i.split('\n\n')
    s = 0
    for k in i:
        k = k.split('\n')
        for i, b in enumerate(k):
            if i == 0:
                mn = set(b)
            else:
                mn = mn.intersection(set(b))
        s += len(mn)
    print(s)
    input()
    print('submitting')
    submitb(s)


main()
