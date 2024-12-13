from aoc import *
from collections import Counter


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
    maxi, maxj = map_dd_size(inp)
    grouped = set()
    groups = [
        search(i, j, inp, set(), grouped)
        for (i, j), plant in inp.items()
        if (i, j) not in grouped
    ]
    pos_to_groupid = {
        (i, j): gid for (gid, g) in enumerate(groups) for (i, j) in g
    }

    fences = 0
    c = Counter()
    for i in range(-1, maxi):
        prevstate = (inp[i, 0], inp[i + 1, 0])
        if not (prevstate[0] == prevstate[1]):
            c[pos_to_groupid.get((i, 0), None)] += 1
            c[pos_to_groupid.get((i + 1, 0), None)] += 1
            # print(
            #     'counting between', inp.get((i, 0)), 'and', inp.get((i + 1, 0))
            # )
        for j in range(1, maxj):
            if (state := (inp[i, j], inp[i + 1, j])) != prevstate and state[
                0
            ] != state[1]:
                # Upper plant changed, add fence for it
                if state[0] != prevstate[0] or prevstate[0] == prevstate[1]:
                    c[pos_to_groupid.get((i, j), None)] += 1
                    # print('UP adding to', inp.get((i, j)), f'between {inp[i, j], inp[i + 1, j]}')
                # Lower plant changed, add fence for it
                if state[1] != prevstate[1] or prevstate[0] == prevstate[1]:
                    c[pos_to_groupid.get((i + 1, j), None)] += 1
                    # print('DOWN adding to', inp.get((i + 1, j)), f'between {inp[i, j], inp[i + 1, j]}')
            prevstate = state
    # print('horizontal')
    for j in range(-1, maxj):
        prevstate = (inp[0, j], inp[0, j + 1])
        if not (prevstate[0] == prevstate[1]):
            c[pos_to_groupid.get((0, j), None)] += 1
            c[pos_to_groupid.get((0, j + 1), None)] += 1
            # print(
            #     'counting between', inp.get((0, j)), 'and', inp.get((0, j + 1))
            # )
        for i in range(1, maxi):
            if (state := (inp[i, j], inp[i, j + 1])) != prevstate and state[
                0
            ] != state[1]:
                # Left plant changed, add fence for it
                if state[0] != prevstate[0] or prevstate[0] == prevstate[1]:
                    c[pos_to_groupid.get((i, j), None)] += 1
                    # print('LEFT adding to', inp.get((i, j)), f'between {inp[i, j], inp[i, j + 1]}')
                # Right plant changed, add fence for it
                if state[1] != prevstate[1] or prevstate[0] == prevstate[1]:
                    c[pos_to_groupid.get((i, j + 1), None)] += 1
                    # print('RIGHT adding to', inp.get((i, j + 1)), f'between {inp[i, j], inp[i, j + 1]}')
            prevstate = state
    return sum(len(g) * c[gid] for gid, g in enumerate(groups))


DAY = 12
FILE_TEST = f"{DAY}_testa.txt"
FILE_TEST = f"{DAY}_testb.txt"
FILE_TEST = f"{DAY}_testc.txt"
FILE_TEST = f"{DAY}_testd.txt"
FILE_EXP = f"{DAY}_exp.txt"
FILE = f"{DAY}.txt"
# test_and_submit(main, FILE_TEST, FILE_EXP, FILE, DAY)
# print(main(FILE_TEST))
print(main(FILE))
