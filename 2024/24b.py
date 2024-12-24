from aoc import *
from itertools import pairwise, combinations, repeat, product, accumulate, permutations, cycle, combinations_with_replacement
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
import random

def incorrect_z(s: int, n: int) -> [str]:
    i = 0
    incorrect = []
    while s or n:
        a = s % 2
        b = n % 2
        s //= 2
        n //= 2
        if a != b:
            incorrect.append(f'z{i:02}')
        i += 1
    return incorrect

def first_incorrect_z(s: int, n: int) -> str:
    i = 0
    while s or n:
        a = s % 2
        b = n % 2
        s //= 2
        n //= 2
        if a != b:
            return f'z{i:02}'
        i += 1

def random_number() -> int:
    return random.randrange(2**44, 2**45)
    return random.randrange(2**45)

def find_all_deps(dependencies, wire, current_set):
    if dependencies[wire][0][0] not in 'xy':
        current_set.add(dependencies[wire][0])
        find_all_deps(dependencies, dependencies[wire][0], current_set)
    if dependencies[wire][1][0] not in 'xy':
        current_set.add(dependencies[wire][1])
        find_all_deps(dependencies, dependencies[wire][1], current_set)

def to_values(num: int, letter: str, values: dict):
    for i in range(45):
        a = num % 2
        num //= 2
        values[f'{letter}{a:02}'] = bool(a)


def compute(x: int, y: int, swap) -> int:
    values = {}
    to_values(x, 'x', values)
    to_values(y, 'y', values)
    changed = True
    while changed:
        changed = False
        for a, oper, b, c in rul:
            # print(a, oper, b, c)
            a = swap[a]
            b = swap[b]
            c = swap[c]
            if c not in values and a in values and b in values:
                if oper == 'OR':
                    values[c] = values[a] or values[b]
                elif oper == 'AND':
                    values[c] = values[a] and values[b]
                elif oper == 'XOR':
                    values[c] = values[a] ^ values[b]
                else:
                    print('BAD')
                changed = True
    # print(rul)
    # print(values)
    ooo = sorted(((k, c) for k, c in values.items() if k[0] == 'z'), key=lambda x: x[0], reverse=True)
    # print(ooo)
    return int(''.join(str(int(c)) for _, c in ooo), base=2)

def first_bad(swap):
    x = random_number()
    y = random_number()
    n = x+y
    computed = compute(x, y, swap)
    if n == computed:
        return None
    return first_incorrect_z(n, computed)

def main(infi: str):
    inp = filerstrip(infi)
    inputs, rules = inp.split('\n\n')
    values = {}
    for i in inputs.split('\n'):
        name, val = i.split(': ')
        values[name] = bool(int(val))
    # print(values)
    global rul
    rul = []
    # print(rules)
    dependencies = {}
    possible_outputs = set()
    for r in rules.split('\n'):
        # print(r)
        match = re.fullmatch(r'^(.*?) (.*?) (.*?) -> (.*?)$', r)
        rul.append((match[1], match[2], match[3], match[4]))
        dependencies[match[4]] = (match[1], match[3])
        possible_outputs.add(match[4])
        possible_outputs.add(match[1])
        possible_outputs.add(match[3])
    basic_swapper = {k: k for k in possible_outputs}
    # print([(k, c) for k, c in values.items() if k[0] == 'z'])
    # print(sorted(((k, c) for k, c in values.items() if k[0] == 'z'), key=lambda x: x[0], reverse=True))
    # ooo = sorted(((k, c) for k, c in values.items() if k[0] == 'z'), key=lambda x: x[0], reverse=True)
    # aaa = sorted(((k, c) for k, c in values.items() if k[0] == 'x'), key=lambda x: x[0], reverse=True)
    # bbb = sorted(((k, c) for k, c in values.items() if k[0] == 'y'), key=lambda x: x[0], reverse=True)
    # number = int(''.join(str(int(c)) for _, c in ooo), base=2)
    # x = int(''.join(str(int(c)) for _, c in aaa), base=2)
    # y = int(''.join(str(int(c)) for _, c in bbb), base=2)
    # print(bin(x+y))
    # print(bin(number))

    # deps = incorrect_z(x+y, number)
    # print(deps)
    # sets = []
    # for dep in deps:
    #     dep_set = set()
    #     find_all_deps(dependencies, dep, dep_set)
    #     # print(dep_set)
    #     sets.append(dep_set)
    # print(reduce(operator.and_, sets))
    # return
    # [find_all_deps(dependencies, dep, dep_set) for dep in deps]
    # comb = list(combinations(dep_set, 2))
    # # for c in combinations(comb, 4):
    # #     if len(set(flatten(c))) != 8:
    # #         continue
    # #     print(c)
    # print(dep_set)

    active_swapper = basic_swapper.copy()
    while True:
        first_incorrect = first_bad(active_swapper)
        print('at', first_incorrect)
        if first_incorrect is None:
            print(active_swapper)
            break
        dep_set = set()
        find_all_deps(dependencies, first_incorrect, dep_set)
        for a, b in combinations(dep_set, 2):
            new_swapper = active_swapper.copy()
            new_swapper[a] = b
            new_swapper[b] = a
            if any(int(first_bad(new_swapper)[1:]) <= int(first_incorrect[1:]) for i in range(100)):
                continue
            else:
                active_swapper = new_swapper
                break

    return

DAY = 24
FILE_TEST = f"{DAY}_testa.txt"
# FILE_TEST = f"{DAY}_testb.txt"
FILE_EXP = f"{DAY}_exp.txt"
FILE = f"{DAY}.txt"
# test_and_submit(main, FILE_TEST, FILE_EXP, FILE, DAY)
# print(main(FILE_TEST))
print(main(FILE))
