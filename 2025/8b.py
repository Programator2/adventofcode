from aoc import *
import math
from operator import itemgetter


def main(infi: str):
    inp = lines_stripped(infi)
    num = []
    for a in inp:
        x, y, z = a.split(',')
        num.append((int(x), int(y), int(z)))
    dists = {}
    for i in range(len(num)):
        for j in range(i + 1, len(num)):
            d = math.dist(num[i], num[j])
            dists[i, j] = d
    it = sorted(dists.items(), key=itemgetter(1))
    pointers = {}
    for i, ((a, b), length) in enumerate(it):
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
            return num[a][0] * num[b][0]


DAY = 8
FILE_TEST = f"{DAY}_testa.txt"
# FILE_TEST = f"{DAY}_testb.txt"
FILE_EXP = f"{DAY}_exp.txt"
FILE = f"{DAY}.txt"
# test_and_submit(main, FILE_TEST, FILE_EXP, FILE, DAY)
# print(main(FILE_TEST))
print(main(FILE))
