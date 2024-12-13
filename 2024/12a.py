from aoc import *


def search(i, j, m, visited, grouped: set):
    visited.add((i, j))
    plant = m[i, j]
    [
        search(di, dj, m, visited, grouped)
        for di, dj in [
            (i + di, j + dj)
            for di, dj in ((1, 0), (0, 1), (-1, 0), (0, -1))
            if (i + di, j + dj) in m
            and (i + di, j + dj) not in visited
            and m[i + di, j + dj] == plant
        ]
    ]
    grouped.update(visited)
    return visited


def main(infi: str):
    inp = load_map_dd(infi)
    values = {v for v in inp.values()}
    grouped = set()
    groups = [
        search(i, j, inp, set(), grouped)
        for (i, j), plant in inp.items()
        if (i, j) not in grouped
    ]
    return sum(
        len(g)
        * sum(
            1
            for _, _ in [
                (i + di, j + dj)
                for i, j in g
                for di, dj in ((1, 0), (0, 1), (-1, 0), (0, -1))
                if (i + di, j + dj) not in g
            ]
        )
        for g in groups
    )


DAY = 12
FILE_TEST = f"{DAY}_testa.txt"
# FILE_TEST = f"{DAY}_testb.txt"
FILE_EXP = f"{DAY}_exp.txt"
FILE = f"{DAY}.txt"
# test_and_submit(main, FILE_TEST, FILE_EXP, FILE, DAY)
# print(main(FILE_TEST))
print(main(FILE))
