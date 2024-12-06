#!/usr/bin/env pypy3
from aoc import *


# Run this using pypy, it's a bit more computationally intensive


U = 1
R = 2
D = 3
L = 4
newoff = {U: (-1, 0), R: (0, 1), D: (1, 0), L: (0, -1)}
newdir = {U: R, R: D, D: L, L: U}


# Not part of solution, just for debug
def print_track(inp, track: set[(int, int)]):
    maxi = max(i for i, _ in inp) + 1
    maxj = max(j for _, j in inp) + 1
    for i in range(maxi):
        for j in range(maxj):
            if (i, j) in track:
                print('x', end='')
            else:
                print(inp[i, j], end='')
        print()


def end(i, j, dir, maxi, maxj):
    return (
        (dir == U and i == 0)
        or (dir == D and i == maxi - 1)
        or (dir == L and j == 0)
        or (dir == R and j == maxj - 1)
    )


def main(infi: str):
    inp = load_map_dd(infi)
    maxi = max(i for i, _ in inp) + 1
    maxj = max(j for _, j in inp) + 1
    pos = None
    for i in range(maxi):
        for j in range(maxj):
            if inp[i, j] == '^':
                inp[i, j] = '.'
                pos = (i, j)
                break
        if pos:
            break

    orig_pos = pos
    obstructions = [
        (a, b) for a in range(maxi) for b in range(maxj) if (a, b) != pos
    ]

    s = 0
    for opos in obstructions:
        if inp[opos] == '#':
            continue
        inp[opos] = '#'

        pos = orig_pos
        dir = U
        coords = {(pos, dir)}
        while not end(*pos, dir, maxi, maxj):
            off = newoff[dir]
            new_pos = pos[0] + off[0], pos[1] + off[1]
            if inp[new_pos] == '#':
                dir = newdir[dir]
            else:
                pos = new_pos
            if (pos, dir) in coords:
                s += 1
                break
            coords.add((pos, dir))
        inp[opos] = '.'

    return s


DAY = 6
FILE_TEST = f"{DAY}_testa.txt"
# FILE_TEST = f"{DAY}_testb.txt"
FILE_EXP = f"{DAY}_exp.txt"
FILE = f"{DAY}.txt"
# test_and_submit(main, FILE_TEST, FILE_EXP, FILE, DAY)
# print(main(FILE_TEST))
print(main(FILE))
# import cProfile
# cProfile.run('main(FILE)')
