from aoc import *
from collections import defaultdict
from itertools import combinations
from pprint import pprint
from math import sqrt


FILE = "20_test.txt"
FILE = "20.txt"


def get(tile, side, reverse=False):
    if side == 'T':
        return list(reversed(tile[0])) if reverse else tile[0]
    elif side == 'R':
        col = [x[-1] for x in tile]
        return list(reversed(col)) if reverse else col
    elif side == 'B':
        return list(reversed(tile[-1])) if reverse else tile[-1]
    elif side == 'L':
        col = [x[0] for x in tile]
        return list(reversed(col)) if reverse else col


def get_transform(side: str, side2: str, reverse: bool):
    numa = {'T': 0, 'R': 1, 'B': 2, 'L': 3}
    numb = {'T': 2, 'R': 1, 'B': 0, 'L': 3}
    rot = (numa[side] + numb[side2]) % 4
    flip = 0
    if not reverse:
        if (numb == 'B' and numa in ['B', 'L']) or (numb == 'T' and numa in ['T', 'R']):
            flip = 'V'
        elif (numb == 'L' and numa in ['B', 'L']) or (numb == 'R' and numa in ['T', 'R']):
            flip = 'H'
    else:
        if (numb == 'T' and numa in ['B', 'L']) or (numb == 'B' and numa in ['T', 'R']):
            flip = 'V'
        elif (numb == 'R' and numa in ['B', 'L']) or (numb == 'L' and numa in ['T', 'R']):
            flip = 'H'
    return flip, rot


def reverse_transform(transform: tuple):
    # This is not correct, see 20b.py for correct alternative
    return transform[0], (4 - transform[1]) % 4


def find_neig(tiles):
    neig = defaultdict(dict)                   # id -> side -> (ID, transf)
    for a, b in combinations(tiles, 2):
        ma = tiles[a]
        mb = tiles[b]
        options = ('T', 'R', 'B', 'L')
        for oa in options:
            for ob in options:
                for r in (False, True):
                    if get(ma, oa) == get(mb, ob, r):
                        transform = get_transform(oa, ob, r)
                        neig[a][oa] = (b, *transform)
                        reverse_t = reverse_transform(transform)
                        neig[b][ob] = (a, *reverse_t)
    return neig


def main():
    inp = file(FILE)
    inp = inp.split('\n\n')
    tiles = {}
    for i in inp:
        i = i.split('\n')
        number = int(i[0][5:-1])
        tiles[number] = list(map(lambda x: list(x.rstrip()), i[1:]))
    neig = find_neig(tiles)
    print(len(neig))


main()
