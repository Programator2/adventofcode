"""Plotting code is in 10a_plot.py"""
import sys

# import matplotlib.pyplot as plt
from collections import Counter
from copy import deepcopy


def search_up(x, y, coordinates):
    if (x, y + 1) in coordinates:
        return 1 + search_up(x, y + 1, coordinates)
    return 0


def search_down(x, y, coordinates):
    if (x, y - 1) in coordinates:
        return 1 + search_up(x, y - 1, coordinates)
    return 0


def get_constellation_quality(points):
    coordinates = {(x, y) for x, y, a, b in points}

    quality = 0
    for x, y in coordinates:
        quality += search_up(x, y, coordinates)
        quality += search_down(x, y, coordinates)

    return quality


def compute_price(p):
    count_x = Counter(map(lambda x: x[0], p))
    s = 0
    for v in count_x.values():
        if v > 10:
            s += v
    return s


with open("10.txt") as f:
    l = f.read().splitlines()

points = []

for p in l:
    x = int(p[10:16])
    y = int(p[18:24])
    x_vel = int(p[36:38])
    y_vel = int(p[40:42])
    point = [x, y, x_vel, y_vel]
    points.append(point)

c = 0
prev = 999999
#
# CLOCK = 10238
#
# for p in points:
#     p[0] += CLOCK*p[2]
#     p[1] += CLOCK*p[3]
#     plt.scatter(p[0], p[1])
#
# plt.show()

max_q = 0
max_points = None

try:
    while True:
        for p in points:
            p[0] += p[2]
            p[1] += p[3]
        max_x = max(points, key=lambda x: x[0])[0]
        min_x = min(points, key=lambda x: x[0])[0]
        max_y = max(points, key=lambda x: x[1])[1]
        min_y = min(points, key=lambda x: x[1])[1]
        # absolut = sum(map(abs, (max_x, min_x, max_y, min_y)))
        absolut = abs(max_x - min_x) + abs(max_y - min_y)
        # print(compute_price(points))
        if absolut < prev:
            max_points = deepcopy(points)
            prev = absolut
            # break
        # prev = absolut
        # q = get_constellation_quality(points)
        # print(q)
        # if q > max_q:
        # max_q = q
        # max_points = points.copy()
        # max_q = max(q, max_q)
        c += 1
        if c % 3000 == 0:
            # print(c, max_q)
            print(c)
        if c > 999999:
            print("absolut", prev)
            print(max_points)
            break
except KeyboardInterrupt:
    print(prev)
    print(max_points)
    sys.exit(0)
