from aoc import *
from more_itertools import flatten
from itertools import batched
import operator
from bisect import *


def main(input_file: str):
    inp = filerstrip(input_file)
    seeds, *ranges = inp.split('\n\n')
    seeds = map(int, seeds.split(':')[1].split())
    seeds = [(st, st + lenn) for st, lenn in batched(seeds, n=2)]
    ranges = [sorted([tuple(int(i) for i in x.split()) for x in mapp.split('\n')[1:]], key=operator.itemgetter(1)) for mapp in ranges]
    for mi, m in enumerate(ranges):
        new_seeds = []
        while seeds:
            st, end = seeds.pop()
            for y, con, conlen in m:
                cone = con + conlen
                con_delta = y - con
                if cone <= st or con >= end:
                    continue
                intersection = (max(con, st) + con_delta, min(end, cone) + con_delta)
                if intersection[1] <= intersection[0]:
                    raise Exception('problem')
                new_seeds.append(intersection)
                rest_begin = (st, con)
                rest_end = (cone, end)
                if rest_begin[0] < rest_begin[1]:
                    seeds.append(rest_begin)
                if rest_end[0] < rest_end[1]:
                    seeds.append(rest_end)
                break
            else:
                new_seeds.append((st, end))
        seeds = new_seeds
    return min(flatten(seeds))


DAY = 5
FILE_TEST = f"{DAY}_test.txt"
FILE_EXP = f"{DAY}_expb.txt"
FILE = f"{DAY}.txt"
# test_and_submit(main, FILE_TEST, FILE_EXP, FILE, 5)
print(main(FILE_TEST))
print(main(FILE))
