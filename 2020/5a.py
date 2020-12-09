from aocd import submit
import re
from aoc import *


def submita(answer):
    submit(answer, part='a', day=5, year=2020)


FILE = '5_test.txt'
FILE = '5.txt'


def seat(string):
    string = string.replace('B', '1')
    string = string.replace('F', '0')
    out = eval('0b'+string)
    return out


def seat_last(string):
    string = string.replace('R', '1')
    string = string.replace('L', '0')
    out = eval('0b'+string)
    return out


def main():
    m = load_map(FILE)
    out = max(seat(i[:7])*8+seat_last(i[-3:]) for i in m)
    print(out)
    input()
    print('done')
    submita(out)


main()
