from aoc import *
from collections import defaultdict, Counter


FILE = "24_test.txt"
FILE = "24.txt"


def neighb(posx, posy, tiles):
    """Returns number of black neighbouring tiles"""
    if posy % 2 == 0:
        count = (
            tiles[posx, posy + 1]
            + tiles[posx + 1, posy + 1]
            + tiles[posx, posy - 1]
            + tiles[posx + 1, posy - 1]
        )
    else:
        count = (
            tiles[posx - 1, posy + 1]
            + tiles[posx, posy + 1]
            + tiles[posx - 1, posy - 1]
            + tiles[posx, posy - 1]
        )
    ret = tiles[(posx - 1, posy)] + tiles[(posx + 1, posy)] + count
    return ret


def create_white_neigb(tiles):
    add = []
    for (posx, posy), state in tiles.items():
        if state == 0:
            continue
        if posy % 2 == 0:
            coord = [
                (posx, posy + 1),
                (posx + 1, posy + 1),
                (posx, posy - 1),
                (posx + 1, posy - 1),
            ]
        else:
            coord = [
                (posx - 1, posy + 1),
                (posx, posy + 1),
                (posx - 1, posy - 1),
                (posx, posy - 1),
            ]
        coord.extend([(posx - 1, posy), (posx + 1, posy)])
        for x, y in coord:
            if (x, y) not in tiles:
                add.append((x, y))
    for a in add:
        tiles[a] = 0


def main():
    inp = lines(FILE)
    visited = set()
    c = Counter()
    for l in inp:
        l = l.rstrip()
        posx = 0
        posy = 0
        while l:
            if l.startswith("e"):
                l = l[1:]
                posx += 1
            elif l.startswith("se"):
                l = l[2:]
                if posy % 2 == 0:
                    posx += 1
                posy -= 1
            elif l.startswith("sw"):
                l = l[2:]
                if posy % 2 == 1:
                    posx -= 1
                posy -= 1
            elif l.startswith("w"):
                l = l[1:]
                posx -= 1
            elif l.startswith("nw"):
                l = l[2:]
                if posy % 2 == 1:
                    posx -= 1
                posy += 1
            elif l.startswith("ne"):
                l = l[2:]
                if posy % 2 == 0:
                    posx += 1
                posy += 1
        c.update(((posx, posy),))
    out = 0
    tiles = defaultdict(lambda: 0)
    for coord, i in c.items():
        if i % 2 == 1:
            out += 1
            tiles[coord] = 1
    print(tiles)
    create_white_neigb(tiles)
    for i in range(100):
        new_tiles = tiles.copy()
        iter_tiles = tiles.copy()
        for (posx, posy), state in iter_tiles.items():
            if state == 1:
                n = neighb(posx, posy, tiles)
                if n == 0 or n > 2:
                    new_tiles[posx, posy] = 0
            else:
                n = neighb(posx, posy, tiles)
                if n == 2:
                    new_tiles[posx, posy] = 1
        create_white_neigb(new_tiles)
        tiles = new_tiles
    print(sum(tiles.values()))


main()
