from aoc import *
from collections import defaultdict


def count_paths(a, b, cave, visited, av):
    if a.islower():
        visited[a] += 1
    if a == b:
        return 1
    s = 0
    orig_av = av
    for neig in cave[a]:
        if neig == 'start':
            continue
        if visited[neig] < 1 or not av:
            if visited[neig] == 1:
                av = True
            s += count_paths(neig, b, cave, visited.copy(), av)
        av = orig_av
    return s


def main(input_file: str):
    inp = load_map(input_file)
    cave = defaultdict(list)
    for l in inp:
        a, b = l.split('-')
        cave[a].append(b)
        cave[b].append(a)
    visited = defaultdict(int)
    already_visited = False
    out = count_paths('start', 'end', cave, visited, already_visited)
    return out


DAY = 12
FILE_TEST = f"{DAY}_test.txt"
FILE_EXP = f"{DAY}_exp.txt"
FILE = f"{DAY}.txt"
# test_and_submit(main, FILE_TEST, FILE_EXP, FILE)
print(main(FILE))
