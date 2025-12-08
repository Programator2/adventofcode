from aoc import *
import math
from functools import reduce
from operator import itemgetter, mul
from itertools import combinations
from more_itertools import take


def main(infi: str):
    pointers = {}
    for (a, b), length in take(
        1000,
        sorted(
            {
                (i, j): math.dist(i, j)
                for i, j in combinations(
                    [
                        tuple(map(int, a.split(',')))
                        for a in lines_stripped(infi)
                    ],
                    2,
                )
            }.items(),
            key=itemgetter(1),
        ),
    ):
        if a in pointers and b in pointers:
            join = pointers[a] | pointers[b]
            for i in join:
                pointers[i] = join
        if a in pointers:
            pointers[a].add(b)
            pointers[a].add(a)
            if b not in pointers:
                pointers[b] = pointers[a]
        elif b in pointers:
            pointers[b].add(a)
            pointers[b].add(b)
            if a not in pointers:
                pointers[a] = pointers[b]
        else:
            pointers[a] = {a, b}
            pointers[b] = pointers[a]
    return reduce(
        mul,
        [
            len(x)
            for x in sorted(
                set(frozenset(s) for s in pointers.values()),
                key=lambda x: len(x),
                reverse=True,
            )[:3]
        ],
    )


DAY = 8
FILE_EXP = f"{DAY}_testa.txt"
# FILE_TEST = f"{DAY}_testb.txt"
FILE_TEST = f"{DAY}_exp.txt"
FILE = f"{DAY}.txt"
# test_and_submit(main, FILE_TEST, FILE_EXP, FILE, DAY)
# print(main(FILE_TEST))
print(main(FILE))
