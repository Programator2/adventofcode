import re
from collections import defaultdict


with open("3.txt") as f:
    reg = re.compile("#\d* @ (\d*),(\d*): (\d*)x(\d*)\n")
    big_map = defaultdict(int)
    for l in f.readlines():
        res = reg.match(l)
        groups = tuple(map(int, res.group(1, 2, 3, 4)))
        left = groups[0]
        upper = groups[1]
        width = groups[2]
        height = groups[3]
        for x in range(width):
            for y in range(height):
                big_map[(left + x, upper + y)] += 1
    print(len(tuple(filter(lambda x: x > 1, big_map.values()))))
