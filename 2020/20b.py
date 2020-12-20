from aocd import submit
from aoc import *
from collections import defaultdict
from itertools import combinations
from pprint import pprint
from math import sqrt


FILE = "20_test.txt"
FILE = "20.txt"


table = {
    0: {0:0, 1:1, 2:2, 3:3, 'V':4, 'H':6},
    1: {0:1, 1:2, 2:3, 3:0, 'V':7, 'H':5},
    2: {0:2, 1:3, 2:0, 3:1, 'V':6, 'H':4},
    3: {0:3, 1:0, 2:1, 3:2, 'V':5, 'H':7},
    4: {0:4, 1:5, 2:6, 3:7, 'V':0, 'H':2},
    5: {0:5, 1:6, 2:7, 3:4, 'V':3, 'H':1},
    6: {0:6, 1:7, 2:4, 3:5, 'V':2, 'H':0},
    7: {0:7, 1:4, 2:5, 3:6, 'V':1, 'H':3},
}


def get(tile, side, reverse=False):
    if side == "T":
        return list(reversed(tile[0])) if reverse else tile[0]
    elif side == "R":
        col = [x[-1] for x in tile]
        return list(reversed(col)) if reverse else col
    elif side == "B":
        return list(reversed(tile[-1])) if reverse else tile[-1]
    elif side == "L":
        col = [x[0] for x in tile]
        return list(reversed(col)) if reverse else col


def get_transform(side: str, side2: str, reverse: bool):
    numa = {"T": 0, "R": 1, "B": 2, "L": 3}
    numb = {"T": 2, "R": 1, "B": 0, "L": 3}
    rot = (numa[side] + numb[side2]) % 4
    flip = 0
    if not reverse:
        if (side2 == "B" and side in ["B", "L"]) or (side2 == "T" and side in ["T", "R"]):
            flip = "V"
        elif (side2 == "L" and side in ["B", "L"]) or (
            side2 == "R" and side in ["T", "R"]
        ):
            flip = "H"
    else:
        if (side2 == "T" and side in ["B", "L"]) or (side2 == "B" and side in ["T", "R"]):
            flip = "V"
        elif (side2 == "R" and side in ["B", "L"]) or (
            side2 == "L" and side in ["T", "R"]
        ):
            flip = "H"
    return flip, rot


def reverse_transform(transform: tuple):
    # This is weid
    return transform[0], transform[1]
    return transform[0], (4 - transform[1]) % 4


def find_neig(tiles):
    neig = defaultdict(dict)  # id -> side -> (ID, transf)
    for a, b in combinations(tiles, 2):
        ma = tiles[a]
        mb = tiles[b]
        options = ("T", "R", "B", "L")
        for oa in options:
            for ob in options:
                for r in (False, True):
                    if get(ma, oa) == get(mb, ob, r):
                        if (a,b) in [(3673,3389), (3389,3673)]:
                            breakpoint()
                        transform = get_transform(oa, ob, r)
                        neig[a][oa] = (b, transform)
                        transform = get_transform(ob, oa, r)
                        neig[b][ob] = (a, transform)
    return neig


def apply_tran(transform, side):
    a = ["B", "L", "T", "R"]
    try:
        index = a.index(side)
    except ValueError:
        breakpoint()
    rotated_index = (index - transform[1]) % 4
    b, l, t, r = "B", "L", "T", "R"
    if transform[0] == "V":
        l, r = "R", "L"
    elif transform[0] == "H":
        t, b = "B", "T"
    return {0: b, 1: l, 2: t, 3: r}[rotated_index]

def sum_tran(tran1, tran2):
    flip = 0
    rot = tran1[1] + tran2[1]
    if tran1[0] == 0 and tran2[0] != 0:
        flip = tran2[0]
    elif tran1[0] != 0 and tran2[0] == 0:
        flip = tran1[0]
    elif tran1[0] == 'V':
        if tran2[0] == 'V':
            flip = 0
        elif tran2[0] == 'H':
            flip = 0
            rot += 2
    elif tran1[0] == 'H':
        if tran2[0] == 'V':
            flip = 0
            rot += 2
        elif tran2[0] == 'H':
            flip = 0
    return flip, rot % 4


def apply_tran_glob(global_, transform, side):
    ret = apply_tran(global_, apply_tran(transform, side))
    # print(ret)
    return ret


def create_map(neig):
    siz = int(sqrt(len(neig)))
    siz_ind = siz - 1
    m = [[(None, (0, 0))] * siz for i in range(siz)]
    # pprint(m)

    # corners = [n for n, v in neig.items() if len(v) == 2]
    # edges = [n for n, v in neig.items() if len(v) == 3]
    # inside = [n for n, v in neig.items() if len(v) == 4]

    row = 0
    col = 0
    edge = [0, siz_ind]

    # This was found by hand in the neig dictionary
    # You just need to find the upper left corner
    # The set the transformation of everything
    # global_transform = (0, 2)
    m[row][col] = (3677, (0, 2))
    while True:
        col += 1
        if col == siz:
            col = 0
            row += 1
            if row == siz:
                break
        if col != 0:
            try:
                left_on_map = m[row][col - 1]
                neighbour_info = neig[left_on_map[0]]
                side = apply_tran(left_on_map[1], "R")
                nex = neighbour_info[side]  # There would be R, but we need to transform it
            except KeyError as err:
                print(err)
                breakpoint()
            m[row][col] = nex[0], sum_tran(m[row][col - 1][1], nex[1])
        else:
            nex = neig[
                m[row - 1][col][0]
            ][  # There would be B, but we need to transform it
                apply_tran(m[row - 1][col][1], "B")
            ]
            # if row==1 and col==0:
                # breakpoint()
            m[row][col] = nex[0], sum_tran(m[row - 1][col][1], nex[1])
    return m


def main():
    inp = file(FILE)
    inp = inp.split("\n\n")
    tiles = {}
    for i in inp:
        i = i.split("\n")
        number = int(i[0][5:-1])
        tiles[number] = list(map(lambda x: list(x.rstrip()), i[1:]))
    neig = find_neig(tiles)
    pprint(neig)
    return
    m = create_map(neig)
    pprint(m)
    # print(len(neig))
    # print(sum(1 for k, v in neig.items() if len(v) == 3))
    out = 0
    print(out)
    return
    input()
    print("submitting")
    submit(out)


main()
