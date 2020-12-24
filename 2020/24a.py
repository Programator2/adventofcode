from aocd import submit
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
            tiles[posx + 1, posy + 1]
            + tiles[posx, posy + 1]
            + tiles[posx - 1, posy - 1]
            + tiles[posx, posy - 1]
        )
    return tiles[(posx - 1, posy)] + tiles[(posx + 1, posy)] + count


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
    for i in c.values():
        if i % 2 == 1:
            out += 1
    # print(c)
    print(out)
    return
    input()
    print("submitting")
    submit(out)


main()
