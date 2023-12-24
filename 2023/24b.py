from aoc import *
from statistics import median, mode
from more_itertools import windowed, take, peekable, chunked, first_true, split_when, first_true
from heapq import *
# from functools import reduce, cache, cmp_to_key
from functools import cache
from math import ceil
import re
from blessed import BlessedList
from copy import deepcopy
import operator
from string import ascii_letters, ascii_lowercase, ascii_uppercase, digits, hexdigits, whitespace
from pprint import pprint as pp
import bisect
import math
from itertools import pairwise, combinations
import sys
from collections import defaultdict, OrderedDict, deque, Counter
# from ordered_set import OrderedSet
from sympy import *
from sympy.geometry import *


def main(input_file: str):
    inp = lines(input_file)
    points = []
    for l in inp:
        left, right = l.split(' @ ')
        left = tuple(int(x) for x in left.split(', '))
        right = tuple(int(x) for x in right.split(', '))
        points.append((left, right))

    x_min = 200000000000000
    x_max = 400000000000000
    # x_min = 7
    # x_max = 27
    suma = 0
    time = []
    for i in range(1, 4):
        new_points = []
        for (x, y, z), (a, b, c) in points:
            new_points.append((x+a*i, y+b*i, z+c*i))
        time.append(new_points)
    for i1, p1 in enumerate(time[0]):
        for i2, p2 in enumerate(time[1]):
            if i2 == i1:
                continue
            for i3, p3 in enumerate(time[2]):
                if i3 in [i1, i2]:
                    continue
                q = Point(p1)
                w = Point(p2)
                line = Line(q, w)
                if line.intersection(Point(p3)):
                    print(p1, p2, p3)

    # for ((x, y, z), (a, b, c)), ((i, j, k), (d, e, f)) in combinations(points, 2):
    #     q = Point(x, y)
    #     w = Point(x + a, y + b)
    #     # w = Point(a, b)
    #     l1 = Line(q, w)
    #     l1 = Ray(q, w)
    #     r = Point(i, j)
    #     t = Point(i + d, j + e)
    #     # t = Point(d, e)
    #     l2 = Line(r, t)
    #     l2 = Ray(r, t)
    #     inter = intersection(l1, l2)
    #     if inter:
    #         if x_min <= inter[0][0] <= x_max and x_min <= inter[0][1] <= x_max:
    #             suma += 1
    #             # print(f'{((x, y, z), (a, b, c)), ((i, j, k), (d, e, f))}: will cross at {inter}')
    return

DAY = 24
FILE_TEST = f"{DAY}_test.txt"
FILE_EXP = f"{DAY}_expa.txt"
FILE = f"{DAY}.txt"
# test_and_submit(main, FILE_TEST, FILE_EXP, FILE, DAY)
# print(main(FILE_TEST))
print(main(FILE))
