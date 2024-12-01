from aoc import *
from itertools import batched, pairwise, combinations, repeat, product, accumulate, permutations, cycle, combinations_with_replacement
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

def main(infi: str):
    inp = lines_stripped(infi)
    le = []
    ri = []
    ri = Counter()
    for a in inp:
        i, j = a.split()
        le.append(int(i))
        ri[int(j)] += 1
        # ri.append(int(j))
    le.sort()
    s = 0
    for a in le:
        s += a * ri[a]
    return s

DAY = 1
FILE_TEST = f"{DAY}_testa.txt"
FILE_TEST = f"{DAY}_testb.txt"
FILE_EXP = f"{DAY}_exp.txt"
FILE = f"{DAY}.txt"
test_and_submit(main, FILE_TEST, FILE_EXP, FILE, DAY)
print(main(FILE_TEST))
print(main(FILE))
