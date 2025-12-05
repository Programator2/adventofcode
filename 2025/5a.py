from aoc import *
from operator import itemgetter
from bisect import *


def in_range(starts: list, ends:list, item: int):
    i = bisect_right(starts, item, key=itemgetter(0)) - 1
    ie = bisect_left(ends, item, key=itemgetter(1))
    ileft = ie
    while (ileft >= 0 and ileft < len(ends) and item <= ends[ileft][1]):
        if ends[ileft][0] <= item:
            return True
        ileft -= 1
    while (i < len(starts) and item >= starts[i][0]):
        if item <= starts[i][1]:
            return True
        i += 1
    return False


def main(infi: str):
    inp = filerstrip(infi)
    ranges, ids = inp.split('\n\n')
    ranges = ranges.split('\n')
    ids = [int(x) for x in ids.split('\n')]
    starts = []
    for r in ranges:
        a, b = r.split('-')
        starts.append((int(a), int(b)))
    starts.sort(key=itemgetter(0))
    ends = sorted(starts, key=itemgetter(1))
    return sum([in_range(starts, ends, x) for x in ids])


DAY = 5
FILE_TEST = f"{DAY}_testa.txt"
# FILE_TEST = f"{DAY}_testb.txt"
FILE_EXP = f"{DAY}_exp.txt"
FILE = f"{DAY}.txt"
# test_and_submit(main, FILE_TEST, FILE_EXP, FILE, DAY)
# print(main(FILE_TEST))
print(main(FILE))
