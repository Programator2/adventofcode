from aoc import *
from collections import defaultdict, deque, Counter, namedtuple, UserList
from statistics import median, mode
from more_itertools import windowed, take, peekable, chunked, first_true
from heapq import *
from itertools import permutations, product, cycle, accumulate, combinations_with_replacement
from functools import reduce, cache
from math import ceil
import re
from blessed import BlessedList
from copy import deepcopy
import operator
from string import ascii_letters, ascii_lowercase, ascii_uppercase, digits, hexdigits, whitespace
from pprint import pprint as pp
import bisect


def main(input_file: str):
    inp = filerstrip(input_file)
    inp = inp.split('\n\n')
    seeds = [int(x) for x in inp[0][7:].split()]
    maps = []
    key = lambda x: x[1]
    for i in range(1, 8):
        m = inp[i].split('\n')
        n = []
        for x in m[1:]:
            bisect.insort(n, tuple(int(y) for y in x.split()), key=lambda x: x[1])
            # n.append((int(y) for y in x.split()))
        maps.append(n)
    # print(maps)
    mini = 999999999
    for s in seeds:
        print(s, end=', ')
        for m in maps:
            aaa = bisect.bisect_left(m, s, key=key) - 1
            if aaa < 0:
                continue
            # print(aaa)
            # print(m)
            convert = m[aaa]
            if convert[1] <= s < convert[1] + convert[2]:
                s = s - convert[1] + convert[0]
            # return
            print(s, end=', ')
        mini = min(mini, s)
        print()
    # print(inp)
    return mini
    return suma


DAY = 5
FILE_TEST = f"{DAY}_test.txt"
FILE_EXP = f"{DAY}_exp.txt"
FILE = f"{DAY}.txt"
test_and_submit(main, FILE_TEST, FILE_EXP, FILE)
# print(main(FILE_TEST))
# print(main(FILE))
