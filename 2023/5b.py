from aoc import *
from collections import defaultdict, deque, Counter, namedtuple, UserList
from statistics import median, mode
from more_itertools import windowed, take, peekable, chunked, first_true
from heapq import *
from itertools import permutations, product, cycle, accumulate, combinations_with_replacement, chain, batched
from functools import reduce, cache
from math import ceil
import re
from blessed import BlessedList
from copy import deepcopy
import operator
from string import ascii_letters, ascii_lowercase, ascii_uppercase, digits, hexdigits, whitespace
from pprint import pprint as pp
from bisect import *


def find_lt(a, x, key):
    'Find rightmost value less than x'
    i = bisect_left(a, x, key)
    if i:
        return a[i-1]
    raise ValueError


def main(input_file: str):
    inp = filerstrip(input_file)
    seeds, *ranges = inp.split('\n\n')
    seeds = map(int, seeds.split(':')[1].split())
    seeds = [(st, st + lenn) for st, lenn in batched(seeds, n=2)]
    # maps = []
    # key = lambda x: x[1]
    ranges = [sorted([tuple(int(i) for i in x.split()) for x in mapp.split('\n')[1:]], key=operator.itemgetter(1)) for mapp in ranges]
    final = []
    for st, end in seeds:
        converting = [(st, end)]
        new = []
        for mi, m in enumerate(ranges):
           new = []
           print(f'converting using table {mi}:')
           pp(m)
           print('----------')
           for stt, endd in converting:
                i = bisect_right(m, stt, key=operator.itemgetter(1))
                #        [[[...m[i]...
                #        [stt         endd)
                if i == 0:
                    print(f'bisection for {(stt, endd)} is {i}')
                    next_y, next_con, next_conlen = m[i]
                    next_cone = next_con + next_conlen
                    # I1: Searched range is to the right of all translation
                    # ranges. We need to check the last translation range for
                    # overlap. See I5.
                    #   [m[-1] ...
                    #        [stt         endd)
                    # I5:
                    if endd > next_cone:
                        # I5.1: two parts created
                        #                [next_con            . next_cone)
                        #        [stt    .                endd)
                        new.append((stt, next_con))
                        new.append((next_y, (endd - next_con) + next_y))
                        print(f'A from {(stt, endd)} to {(stt, next_con)} and {(next_y, (endd - next_con) + next_y)}')
                        continue
                    elif endd > next_con:
                        # I5.2: three parts created
                        #                [next_con      next_cone)
                        #        [stt    .                       .     endd)
                        new.append((stt, next_con))
                        new.append((next_y, next_y + next_conlen))
                        new.append((next_cone, endd))
                        print(f'B from {(stt, endd)} to {(stt, next_con)}, {(next_y, (endd - next_con) + next_y)} and {(next_cone, endd)}')
                        continue
                    else:
                        print(f'C from {(stt, endd)} to {(stt, endd)}')
                        new.append((stt, endd))
                        continue
                y, con, conlen = m[i-1]
                cone = con + conlen
                con_delta = y - con
                print(f'bisection for {(stt, endd)} is {(con, cone)}')
                if stt < cone:
                    # Aspon jeden prekryv tam je
                    if endd <= cone:
                        new.append((stt + con_delta, endd + con_delta))
                        print(f'D from {(stt, endd)} to {(stt + con_delta, endd + con_delta)}')
                        continue
                    else:
                        # Kusok sa neprekonvertuje, ale poputuje dalej na
                        # konverziu (teoreticky inym konvertovacim rozsahom).
                        new.append((stt + con_delta, endd + con_delta))
                        new.append((cone, endd))
                        print(f'D from {(stt, endd)} to {(stt + con_delta, endd + con_delta)} and leaving {(cone, endd)}')
                        continue
                if endd <= con:
                    # I2:
                    #                         [con cone)
                    #        [stt         endd)
                    print(f'D from {(stt, endd)} to {(stt, endd)}')
                    new.append((stt, endd))
                    continue
                if cone >= endd > con:
                    # I3:
                    #                 [con    .  cone)
                    #        [stt     .   endd)
                    new.append((stt, con))
                    new.append((y, y + endd - con))
                    print(f'E from {(stt, endd)} to {(stt, con)} and {(y, y + endd - con)}')
                    continue
                if endd > cone:
                    # I4:
                    #                 [con   cone)
                    #        [stt     .          .     endd)
                    new.append((stt, con))
                    new.append((y, y + cone - con))
                    new.append((cone, endd))
                    print(f'F from {(stt, endd)} to {(stt, con)}, {(y, y + cone - con)} and {(cone, endd)}')
                    continue
                raise Exception('problem')
           converting = new
        final.extend(converting)
    print(final)
    return
    mapper = maps[0].copy()
    for m in maps[1:]:
        new_mapper = m.copy()
        for r in mapper:
            begin = r[1]
            end = r[1] + r[2] # not included
            a = bisect.bisect(m, begin, key=key)
            b = bisect.bisect_left(m, end, key=key)
            print(begin, end)
            print(m)
            print(a, b)
        return
    mini = 999999999
    for i, s in enumerate(chain(*ranges)):
        for m in maps:
            aaa = bisect.bisect_left(m, s, key=key) - 1
            if aaa+1 < len(m) and s == m[aaa+1][1]:
                aaa += 1
            if aaa < 0:
                continue
            # print(aaa)
            # print(m)
            convert = m[aaa]
            if convert[1] <= s < convert[1] + convert[2]:
                s = s - convert[1] + convert[0]
            # return
        mini = min(mini, s)
        if i % 10000 == 0:
            print('.', end='')
    # print(inp)
    return mini
    return suma


DAY = 5
FILE_TEST = f"{DAY}_test.txt"
FILE_EXP = f"{DAY}_exp.txt"
FILE = f"{DAY}.txt"
# test_and_submit(main, FILE_TEST, FILE_EXP, FILE)
print(main(FILE_TEST))
# print(main(FILE))
