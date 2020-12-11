import re
from collections import defaultdict


with open("3.txt") as f:
    reg = re.compile("#(\d*) @ (\d*),(\d*): (\d*)x(\d*)\n")
    big_map = defaultdict(int)
    # id_map = {}
    claims = []
    for l in f.readlines():
        res = reg.match(l)
        groups = tuple(map(int, res.group(1, 2, 3, 4, 5)))
        id_ = groups[0]
        left = groups[1]
        upper = groups[2]
        width = groups[3]
        height = groups[4]
        claims.append((id_, left, upper, width, height))
        for x in range(width):
            for y in range(height):
                big_map[(left + x, upper + y)] += 1
                # id_map[(left+x, upper+y)] = id_
    for id_, left, upper, width, height in claims:
        jump = False
        for x in range(width):
            for y in range(height):
                if big_map[(left + x, upper + y)] > 1:
                    jump = True
                    break
            if jump:
                break
        if jump:
            continue
        print(id_)
