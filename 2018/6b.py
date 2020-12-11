from collections import defaultdict


def mhd(p1, p2, q1, q2):
    return abs(p1 - q1) + abs(p2 - q2)


with open("6.txt") as f:
    l = f.readlines()
    l = map(lambda x: x.rstrip(), l)
    points = []
    code = {}
    for i, s in enumerate(l):
        splited = s.split(", ")
        point = (int(splited[0]), int(splited[1]))
        code[point] = i
        points.append(point)
    min_x = min(map(lambda x: x[0], points))
    min_y = min(map(lambda x: x[1], points))
    max_x = max(map(lambda x: x[0], points))
    max_y = max(map(lambda x: x[1], points))

    # helper set
    points_set = set(points)

    result = 0

    for x in range(min_x - 100, max_x + 100):
        for y in range(min_y - 100, max_y + 100):
            dist_sum = sum((mhd(x, y, *p) for p in points))
            if dist_sum < 10000:
                result += 1

    print(result)
