from aoc import *
from collections import defaultdict


def count_paths(a, b, cave, visited):
    if a.islower():
        visited.add(a)
    if a == b:
        return 1
    s = 0
    for neig in cave[a]:
        if neig not in visited:
            s += count_paths(neig, b, cave, visited.copy())
    return s


def main(input_file: str):
    inp = load_map(input_file)
    cave = defaultdict(list)
    for l in inp:
        a, b = l.split('-')
        cave[a].append(b)
        cave[b].append(a)
    visited = set()
    out = count_paths('start', 'end', cave, visited)
    return out


DAY = 12
FILE_TEST = f"{DAY}_test.txt"
FILE_EXP = f"{DAY}_exp.txt"
FILE = f"{DAY}.txt"
# test_and_submit(main, FILE_TEST, FILE_EXP, FILE)
print(main(FILE))
