from aoc import *
import math
from operator import itemgetter


def main(infi: str):
    num = [tuple(map(int, a.split(','))) for a in lines_stripped(infi)]
    pointers = {}
    for (a, b), length in sorted(
        {
            (i, j): math.dist(i, j)
            for i, j in combinations(
                num,
                2,
            )
        }.items(),
        key=itemgetter(1),
    ):
        if a in pointers and b in pointers:
            join = pointers[a] | pointers[b]
            for x in join:
                pointers[x] = join
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

        if len(pointers[a]) == len(num):
            return a[0] * b[0]


DAY = 8
FILE_TEST = f"{DAY}_testa.txt"
# FILE_TEST = f"{DAY}_testb.txt"
FILE_EXP = f"{DAY}_exp.txt"
FILE = f"{DAY}.txt"
# test_and_submit(main, FILE_TEST, FILE_EXP, FILE, DAY)
# print(main(FILE_TEST))
print(main(FILE))
