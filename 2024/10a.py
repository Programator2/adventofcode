from aoc import *


def search(i, j, m, visited, nines, starti, startj):
    starting = m[i, j][0]
    if starting == 9:
        m[starti, startj] = (m[starti, startj][0], m[starti, startj][1] + 1)
        nines.add((i, j))
        return
    visited.add((i, j))
    to_iterate = [
        (i + di, j + dj)
        for di, dj in ((1, 0), (0, 1), (-1, 0), (0, -1))
        if (i + di, j + dj) in m
        and (i + di, j + dj) not in visited
        and m[i + di, j + dj][0] == starting + 1
    ]
    for di, dj in to_iterate:
        search(di, dj, m, visited, nines, starti, startj)


def main(infi: str):
    inp = load_map_dd(infi)
    maxi, maxj = map_dd_size(inp)
    inp = {
        (i, j): (int(inp[i, j]), 0)
        for i, j in product(range(maxi), range(maxj))
    }
    zeros = [
        (i, j)
        for i, j in product(range(maxi), range(maxj))
        if inp[i, j][0] == 0
    ]
    s = 0
    for i, j in zeros:
        nines = set()
        search(i, j, inp, set(), nines, i, j)
        s += len(nines)

    return s


DAY = 10
FILE_TEST = f"{DAY}_testa.txt"
# FILE_TEST = f"{DAY}_testb.txt"
FILE_EXP = f"{DAY}_exp.txt"
FILE = f"{DAY}.txt"
# test_and_submit(main, FILE_TEST, FILE_EXP, FILE, DAY)
# print(main(FILE_TEST))
print(main(FILE))
