from aoc import *
from itertools import combinations
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

    # For test input
    # x_min = 7
    # x_max = 27

    suma = 0
    for ((x, y, z), (a, b, c)), ((i, j, k), (d, e, f)) in combinations(points, 2):
        q = Point(x, y)
        w = Point(x + a, y + b)
        l1 = Line(q, w)
        l1 = Ray(q, w)
        r = Point(i, j)
        t = Point(i + d, j + e)
        l2 = Line(r, t)
        l2 = Ray(r, t)
        inter = intersection(l1, l2)
        if inter:
            if x_min <= inter[0][0] <= x_max and x_min <= inter[0][1] <= x_max:
                suma += 1
    return suma

DAY = 24
FILE_TEST = f"{DAY}_test.txt"
FILE_EXP = f"{DAY}_expa.txt"
FILE = f"{DAY}.txt"
# test_and_submit(main, FILE_TEST, FILE_EXP, FILE, DAY)
# print(main(FILE_TEST))
print(main(FILE))
