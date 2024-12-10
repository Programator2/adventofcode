from aoc import *


def search(i, j, m):
    return (
        1
        if m[i, j] == 9
        else (
            sum(
                search(di, dj, m)
                for di, dj in (
                    (i + di, j + dj)
                    for di, dj in ((1, 0), (0, 1), (-1, 0), (0, -1))
                    if (i + di, j + dj) in m
                    and m[i + di, j + dj] == m[i, j] + 1
                )
            )
        )
    )


def main(infi: str):
    inp = load_map_dd(infi, init=int)
    return sum(
        search(i, j, inp)
        for i, j in [(i, j) for (i, j), num in inp.items() if num == 0]
    )


DAY = 10
FILE_TEST = f"{DAY}_testa.txt"
# FILE_TEST = f"{DAY}_testb.txt"
FILE_EXP = f"{DAY}_exp.txt"
FILE = f"{DAY}.txt"
# test_and_submit(main, FILE_TEST, FILE_EXP, FILE, DAY)
# print(main(FILE_TEST))
print(main(FILE))
