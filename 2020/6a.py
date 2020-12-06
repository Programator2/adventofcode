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
        i = f.read()
    i = i.split('\n\n')
    count = 0
    for k in i:
        k = k.replace('\n', '')
        mn = set(k)
        count += len(mn)
    print(count)
    input()
    print('submitting')
    submita(count)


main()
