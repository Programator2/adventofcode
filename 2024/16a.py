from aoc import *
from itertools import (
    pairwise,
    combinations,
    repeat,
    product,
    accumulate,
    permutations,
    cycle,
    combinations_with_replacement,
)
from more_itertools import (
    first_true,
    flatten,
    ncycles,
    first_true,
    zip_broadcast,
    windowed,
    chunked,
    take,
    peekable,
)
import re
from blessed import BlessedList
from collections import (
    namedtuple,
    defaultdict,
    OrderedDict,
    Counter,
    deque,
    UserList,
)
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


DIRS = ((-1, 0), (0, 1), (1, 0), (0, -1))

# 0 1 2 3
# N E S W


# TODO: Very inefficient. I have to rewrite it using Dijkstra.
def search(m, i, j, face, score, scorem):
    if (i, j, face) not in scorem:
        scorem[i, j, face] = score
    elif scorem[i, j, face] <= score:
        return
    else:
        scorem[i, j, face] = score
        if m[i, j] == 'E':
            return
    for dir, diff in enumerate(DIRS):
        newpos = (i + diff[0], j + diff[1])
        if m.get(newpos, None) in '.E':
            facediff = abs(face - dir)
            if facediff == 3:
                facediff = 1
            search(m, *newpos, dir, score + 1 + facediff * 1000, scorem)


def main(infi: str):
    sys.setrecursionlimit(100000)
    inp = load_map_dd(infi)
    pos = [(i, j) for (i, j), e in inp.items() if e == 'S'][0]
    face = 1
    score = {}
    search(inp, *pos, face, 0, score)
    end = [(i, j) for (i, j), e in inp.items() if e == 'E'][0]
    return min(
        x[3]
        for x in list(
            (*end, face, score.get((*end, face), None)) for face in range(4)
        )
        if x[3] is not None
    )


DAY = 16
FILE_TEST = f"{DAY}_testa.txt"
FILE_TEST = f"{DAY}_testb.txt"
FILE_EXP = f"{DAY}_exp.txt"
FILE = f"{DAY}.txt"
# test_and_submit(main, FILE_TEST, FILE_EXP, FILE, DAY)
# print(main(FILE_TEST))
print(main(FILE))
