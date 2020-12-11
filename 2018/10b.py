import sys

# import matplotlib.pyplot as plt
from collections import Counter
from copy import deepcopy

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

max_q = 0
max_c = 0
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
        absolut = abs(max_x - min_x) + abs(max_y - min_y)
        if absolut < prev:
            max_points = deepcopy(points)
            prev = absolut
            max_c = c + 1
        c += 1
        if c % 3000 == 0:
            print(c)
        if c > 999999:
            print("absolut", prev)
            print(max_points)
            print(max_c)
            break
except KeyboardInterrupt:
    print(prev)
    print(max_points)
    sys.exit(0)
