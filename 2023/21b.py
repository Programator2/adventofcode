from aoc import *
from statistics import median, mode
from more_itertools import windowed, take, peekable, chunked, first_true, split_when, first_true
from heapq import *
# from functools import reduce, cache, cmp_to_key
from functools import cache
from math import ceil
import re
from blessed import BlessedList
from copy import deepcopy
import operator
from string import ascii_letters, ascii_lowercase, ascii_uppercase, digits, hexdigits, whitespace
from pprint import pprint as pp
import bisect
import math
from itertools import pairwise, combinations
import sys
from collections import defaultdict, OrderedDict, deque, Counter
# from ordered_set import OrderedSet

S = [(-1, 0), (1, 0), (0, -1), (0, 1)]


def main(input_file: str):
    m = load_map_dd(input_file)
    maxx = max(x for x, y in m)
    sizex = maxx + 1
    sizey = maxy + 1
    maxy = max(y for x, y in m)
    # pp(m)
    @cache
    def step(x, y):
        return {((x + dx),
                 (y + dy)) for dx, dy in S
                if m[((x + dx) % (maxx + 1),
                      (y + dy) % (maxy + 1))] in ['.', 'S']}

    places = {(x, y) for (x, y), c in m.items() if c == 'S'}
    c = Counter()
    c[next(iter(places))] = 1
    steps = 26501365
    size = steps * 2 + 1
    suma = 0
    for i in range(size):
        if i <= size // 2:
            # we are above or in the middle of the rhombus, the width is
            # increasing
            row = i % sizex
            width = i * 2 + 1
            if width <= sizey:
                # take inner size of the rhomboid
                for col in range(sizey // 2 - i, width, 2):
                    if m[i, col] == '.':
                        suma += 1
            else:
                # take outer size of the rhomboid
                full_widths = width // sizey
                remainder = width % sizey
                if remainder <= sizey // 2:
                    # Count the edges
                    # XXX.........XXX
                    pass

                else:
                    # Count the inside
                    # XXXXXX...
                    # ...XXXXXX
                    #    ^^^......counting just these
                    pass
                pass
        else:
            # we are below rhombus, the width is decreasing
            pass
    for i in range(50):
        new_places = set()
        new_counter = Counter()
        for x, y in places:
            # steps_number = c[x, y]
            # c[x, y] = 0
            new_steps = step(x, y)
            new_places.update(new_steps)
            # for nx, ny in new_steps:
                # new_counter[nx, ny] = steps_number
        places = new_places
        c = new_counter
    # pp(m)
    # for ri in range(maxx + 1):
    #     for ci in range(maxy + 1):
    #         if (ri, ci) in places:
    #             print('O', end='')
    #         else:
    #             print(m[(ri, ci)], end='')
    #     print()
    # pp(c)
    return sum(c.values())

DAY = 21
FILE_TEST = f"{DAY}_test.txt"
FILE_EXP = f"{DAY}_expa.txt"
FILE = f"{DAY}.txt"
# test_and_submit(main, FILE_TEST, FILE_EXP, FILE, DAY)
print(main(FILE_TEST))
# print(main(FILE))
