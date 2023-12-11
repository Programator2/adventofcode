from aoc import *
from itertools import combinations


def main(input_file: str):
    inp = load_map(input_file)
    new = []
    for i in inp:
        if all(x == '.' for x in i):
            new.append(i)
        new.append(i)
    inp = new
    new = [[] for x in inp]
    for i in range(len(inp[0])):
        if all(x[i] == '.' for x in inp):
            for row, x in enumerate(inp):
                new[row].append('.')
        for row, x in enumerate(inp):
            new[row].append(x[i])
    inp = new

    points = []

    for i, r in enumerate(inp):
        for j, c in enumerate(r):
            if c == '#':
                points.append((i, j))
    return sum(abs(a[0] - b[0]) + abs(a[1] - b[1]) for a, b in combinations(points, 2))


DAY = 11
FILE_TEST = f"{DAY}_test.txt"
FILE_EXP = f"{DAY}_exp.txt"
FILE = f"{DAY}.txt"
# test_and_submit(main, FILE_TEST, FILE_EXP, FILE)
print(main(FILE_TEST))
print(main(FILE))
