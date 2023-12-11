from aoc import *
from itertools import combinations


def main(input_file: str):
    inp = load_map(input_file)
    new = []
    expansion_rows = set()
    expansion_cols = set()
    for ii, i in enumerate(inp):
        if all(x == '.' for x in i):
            expansion_rows.add(ii)
    for i in range(len(inp[0])):
        if all(x[i] == '.' for x in inp):
            expansion_cols.add(i)

    points = []

    offi, offj = 0, 0
    for i, r in enumerate(inp):
        if i in expansion_rows:
            offi += 999999
            continue
        offj = 0
        for j, c in enumerate(r):
            if j in expansion_cols:
                offj += 999999
                continue
            if c == '#':
                points.append((i + offi, j + offj))
    return sum(abs(a[0] - b[0]) + abs(a[1] - b[1]) for a, b in combinations(points, 2))


DAY = 11
FILE = f"{DAY}.txt"
print(main(FILE))
