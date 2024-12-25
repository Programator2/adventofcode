from aoc import *
from collections import defaultdict
from functools import reduce
import pickle
from pprint import pprint as pp
import sys


DIRS = ((-1, 0), (0, 1), (1, 0), (0, -1))

# 0 1 2 3
# N E S W


def search(m, i, j, face, score, scorem, prev, fro):
    if (i, j, face) not in scorem:
        scorem[i, j, face] = score
        prev[i, j, face] = {fro}
        if m[i, j] == 'E':
            return
    elif scorem[i, j, face] < score:
        return
    elif scorem[i, j, face] == score:
        prev[i, j, face].add(fro)
        return
    else:
        scorem[i, j, face] = score
        prev[i, j, face] = {fro}
        if m[i, j] == 'E':
            return
    for dir, diff in enumerate(DIRS):
        newpos = (i + diff[0], j + diff[1])
        if m.get(newpos, None) in '.E':
            facediff = abs(face - dir)
            if facediff == 3:
                facediff = 1
            search(
                m,
                *newpos,
                dir,
                score + 1 + facediff * 1000,
                scorem,
                prev,
                (i, j, face),
            )


def dfs(prev, elem: set):
    if not elem:
        return elem
    return (
        reduce(
            lambda x, y: x | y, (dfs(prev, prev.get(e, set())) for e in elem)
        )
        | elem
    )


def main(infi: str):
    sys.setrecursionlimit(100000)
    inp = load_map_dd(infi)
    pos = [(i, j) for (i, j), e in inp.items() if e == 'S'][0]
    face = 1
    score = {}
    # store the previous position for state i, j, face -> set(previous states)
    prev = defaultdict(set)
    end = [(i, j) for (i, j), e in inp.items() if e == 'E'][0]
    # print(list((*end, face, score[(*end, face)]) for face in range(4)))
    # try:
    #     with open('16.pickle', 'rb') as f:
    #         prev = pickle.load(f)
    # except OSError:
    search(inp, *pos, face, 0, score, prev, None)
    #     with open('16.pickle', 'wb') as f:
    #         pickle.dump(prev, f)
    best_paths = dfs(prev, {(1, 139, 1)})
    best_paths.remove(None)
    return len(set((i, j) for i, j, _ in best_paths))


DAY = 16
FILE_TEST = f"{DAY}_testa.txt"
FILE_TEST = f"{DAY}_testb.txt"
FILE_EXP = f"{DAY}_exp.txt"
FILE = f"{DAY}.txt"
# test_and_submit(main, FILE_TEST, FILE_EXP, FILE, DAY)
# print(main(FILE_TEST))
print(main(FILE))
