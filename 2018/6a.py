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

    # {point: area}
    area = defaultdict(int)

    # {coordinate tuple: point or None}
    board = {}

    # helper set
    points_set = set(points)

    # add points to the board
    for p in points:
        board[p] = p

    for x in range(min_x, max_x + 1):
        for y in range(min_y, max_y + 1):
            if (x, y) in points_set:
                continue
            min_dist = 999999
            min_point = None
            double_minimum = False
            for p in points:
                dist = mhd(x, y, *p)
                if dist == min_dist:
                    double_minimum = True
                elif dist < min_dist:
                    double_minimum = False
                    min_dist = dist
                    min_point = p
            else:
                if double_minimum:
                    board[(x, y)] = None
                else:
                    board[(x, y)] = min_point
                    area[min_point] += 1

    # Check edges for infinite
    infinity_set = set()
    for x in range(min_x, max_x + 1):
        infinity_set.add(board[(x, min_y)])
        infinity_set.add(board[(x, max_y)])
    for y in range(min_y, max_y + 1):
        infinity_set.add(board[(min_x, y)])
        infinity_set.add(board[(max_x, y)])

    areas = []
    for point, area in area.items():
        if point in infinity_set:
            continue
        areas.append(area)

    # Treba pripocitat este jednotku, lebo neberiem do uvahy samotny bod, od
    # ktoreho pocitam vzdialenost
    #
    # Add one because the actual point from which the distance is computed was
    # not included
    print(max(areas) + 1)

    # print()
    # for x in range(min_x, max_x + 1):
    #     for y in range(min_y, max_y + 1):
    #         point = board[(x, y)]
    #         if point:
    #             print(code[point], end='')
    #         else:
    #             print('.', end='')
    #     print()
