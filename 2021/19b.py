from aoc import *
from collections import defaultdict, Counter
from itertools import product, permutations


transform = [
    lambda x, y, z: (x, y, z),
    lambda x, y, z: (-y, x, z),
    lambda x, y, z: (-x, -y, z),
    lambda x, y, z: (y, -x, z),
    lambda x, y, z: (-z, y, x),
    lambda x, y, z: (-y, -z, x),
    lambda x, y, z: (z, -y, x),
    lambda x, y, z: (y, z, x),
    lambda x, y, z: (-x, y, -z),
    lambda x, y, z: (-y, -x, -z),
    lambda x, y, z: (x, -y, -z),
    lambda x, y, z: (y, x, -z),
    lambda x, y, z: (z, y, -x),
    lambda x, y, z: (-y, z, -x),
    lambda x, y, z: (-z, -y, -x),
    lambda x, y, z: (y, -z, -x),
    lambda x, y, z: (x, -z, y),
    lambda x, y, z: (z, x, y),
    lambda x, y, z: (-x, z, y),
    lambda x, y, z: (-z, -x, y),
    lambda x, y, z: (x, z, -y),
    lambda x, y, z: (-z, x, -y),
    lambda x, y, z: (-x, -z, -y),
    lambda x, y, z: (z, -x, -y),
]


def sub(x, y):
    return (x[0] - y[0], x[1] - y[1], x[2] - y[2])


def manhattan(x, y):
    return abs(x[0] - y[0]) + abs(x[1] - y[1]) + abs(x[2] - y[2])


def search_transform(fro, to, tran, visited) -> list:
    if fro in visited:
        return []
    visited.add(fro)
    if to in tran[fro]:
        return [to]
    for inter in tran[fro]:
        if path := search_transform(inter, to, tran, visited):
            return [inter] + path
    return []


def do_transform(fro, to, trans_indirect, trans_ins, beacon):
    if fro == to:
        return beacon
    for ins in trans_indirect[(fro, to)]:
        beacon = transform[trans_ins[fro][ins][0]](*beacon)
        beacon = sub(beacon, trans_ins[fro][ins][1])
        fro = ins
    return beacon


def main(input_file: str):
    inp = file(input_file).rstrip()
    raw = inp.split('\n\n')
    res = []
    for i, r in enumerate(raw):
        scans = r.split('\n')[1:]
        res.append([])
        for s in scans:
            pos = tuple(int(x) for x in s.split(','))
            res[i].append(pos)
    transform_map = defaultdict(set)
    trans_ins = defaultdict(dict)
    for it, t in enumerate(transform):
        for (ia, a), (ib, b) in permutations(enumerate(res), 2):
            a_transformed = [t(*p) for p in a]
            c = Counter()
            for ela, elb in product(a_transformed, b):
                c[sub(ela, elb)] += 1
            if (xxx := c.most_common(1))[0][1] >= 12:
                # We have a match!
                transform_map[ia].add(ib) # we can transform ia into ib
                trans_ins[ia][ib] = (it, xxx[0][0]) # these are the instructions
                                                    # to transform: [0] is a
                                                    # number of the
                                                    # transformation and [1] is
                                                    # the offset
                # print(f'tranformation {it}: from {ia} to {ib} with offset {xxx[0]}')
    # Find a fixed point: I don't know if it's possible to transform into every
    # beacon, so let's check it.
    trans_indirect = {}         # Dict [from, to] = [1, 2,...] of scanner
                                # numbers to transform a beacon position from
                                # scanner `from` to scanner `to`
    for fro in range(len(res)):
        for to in range(len(res)):
            if fro == to:
                trans_indirect[(fro, to)] = []
                continue
            if to in transform_map[fro]:
                trans_indirect[(fro, to)] = [to]
                continue
            trans_indirect[(fro, to)] = search_transform(fro, to, transform_map, set())

    out = max(manhattan(a, b) for a, b in permutations(
        [(0, 0, 0)] + [do_transform(i, 0, trans_indirect, trans_ins, (0, 0, 0)) for i in range(1, len(res))]
        , 2))
    return out


DAY = 19
FILE_TEST = f"{DAY}_test.txt"
FILE_EXP = f"{DAY}_exp.txt"
FILE = f"{DAY}.txt"
# test_and_submit(main, FILE_TEST, FILE_EXP, FILE)
# print(main(FILE_TEST))
print(main(FILE))
