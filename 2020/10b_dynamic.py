from aoc import *
import functools


FILE = '10_test.txt'
FILE = '10.txt'
# FILE = '10_test0.txt'


@functools.cache
def how_many(value: int, nset: frozenset):
    cnt = 0
    if value + 1 in nset:
        cnt += how_many(value + 1, nset)
    if value + 2 in nset:
        cnt += how_many(value + 2, nset)
    if value + 3 in nset:
        cnt += how_many(value + 3, nset)
    if cnt == 0:
        return 1
    return cnt


def main():
    inp = load_ints(FILE)
    inp.sort()
    inp.insert(0, 0)
    inp.append(inp[-1]+3)
    nset = frozenset(inp)
    out = how_many(0, nset)
    print(out)


main()
