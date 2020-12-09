from aocd import submit
import re
from aoc import *


def submitb(answer):
    submit(answer, part='b', day=5, year=2020)


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
    seats = set(range(13, 881))
    m = load_map(FILE)
    out = max(seat(i[:7])*8+seat_last(i[-3:]) for i in m)
    outmin = min(seat(i[:7])*8+seat_last(i[-3:]) for i in m)
    seats.difference_update(seat(i[:7])*8+seat_last(i[-3:]) for i in m)
    print(out, outmin)
    print(seats)
    input()
    print('done')
    submitb(out)


main()
