from aoc import *
from itertools import combinations
from collections import defaultdict


def main(infi: str):
    sets = set()
    connections = defaultdict(set)
    computers = set()
    for l in lines_stripped(infi):
        left, right = l.split('-')
        connections[left].add(right)
        connections[right].add(left)
        computers.add(left)
        computers.add(right)
    for a, b, c in combinations(computers, 3):
        if b in connections[a] and b in connections[c] and c in connections[a]:
            sets.add((a, b, c))
    return sum(1 for a, b, c in sets if any(pc[0] == 't' for pc in (a, b, c)))


DAY = 23
FILE_TEST = f"{DAY}_testa.txt"
# FILE_TEST = f"{DAY}_testb.txt"
FILE_EXP = f"{DAY}_exp.txt"
FILE = f"{DAY}.txt"
# test_and_submit(main, FILE_TEST, FILE_EXP, FILE, DAY)
# print(main(FILE_TEST))
print(main(FILE))
