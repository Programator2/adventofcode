from aoc import *
# from itertools import batched, pairwise, combinations, repeat, product, accumulate, permutations, cycle, combinations_with_replacement
from more_itertools import first_true, flatten, ncycles, first_true, zip_broadcast, windowed, chunked, take, peekable
import re
from blessed import BlessedList
from collections import namedtuple, defaultdict, OrderedDict, Counter, deque, UserList
import operator
from operator import itemgetter
from bisect import *
from functools import reduce, cache, cmp_to_key
import math
from copy import deepcopy
from math import ceil
from heapq import *
import sys
from pprint import pprint as pp
from statistics import mode
from string import ascii_uppercase

dirs = ('U', 'R', 'D', 'L')
newoff = {'U':(-1, 0), 'R':(0, 1), 'D':(1, 0), 'L':(0, -1)}
newdir = {'U':'R', 'R':'D', 'D':'L', 'L':'U'}

def end(i, j, inp, dir, maxi, maxj):
    return ((dir == 'U' and i == 0) or
        (dir == 'D' and i == maxi-1) or
        (dir == 'L' and j == 0) or
        (dir == 'R' and j == maxj-1))

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


def main(infi: str):
    inp = load_map_dd(infi)
    maxi = max(i for i, _ in inp) + 1
    maxj = max(j for _, j in inp) + 1
    pos = None
    for i in range(maxi):
        for j in range(maxj):
            if inp[i,j] == '^':
                inp[i,j] = '.'
                pos = (i,j)
                break
        if pos:
            break
    dir = 'U'
    orig_pos = pos
    obstructions = {(a, b) for a in range(maxi) for b in range(maxj)}
    obstructions.remove(pos)

    s = 0
    for opos in obstructions:
        # obstacles = set()
        if inp[opos] == '#':
            continue
        inp[opos] = '#'

        pos = orig_pos
        dir = 'U'
        coords = {(pos, dir)}
        while not end(*pos, inp, dir, maxi, maxj):
            off = newoff[dir]
            new_pos = pos[0] + off[0], pos[1] + off[1]
            if inp[new_pos] == '#':
                dir = newdir[dir]
                pos = pos[0] + newoff[dir][0], pos[1] + newoff[dir][1]
            else:
                pos = new_pos
            if (pos, dir) in coords:
                s += 1
                inp[opos] = '.'
                # obstacles.add(opos)
                # print_track(inp, coords)
                # print('-'*80)
                break
            coords.add((pos, dir))

        inp[opos] = '.'

    # print(obstacles)
    return s

DAY = 6
FILE_TEST = f"{DAY}_testa.txt"
# FILE_TEST = f"{DAY}_testb.txt"
FILE_EXP = f"{DAY}_exp.txt"
FILE = f"{DAY}.txt"
# test_and_submit(main, FILE_TEST, FILE_EXP, FILE, DAY)
# print(main(FILE_TEST))

# t = Timer()
# t.start()
# ret = main(FILE)
# print(t.end()/1000000000)
# print(ret)

import cProfile
cProfile.run('main(FILE)')
