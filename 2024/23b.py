from aoc import *
from functools import reduce
from collections import defaultdict
import operator


def main(infi: str):
    connections = defaultdict(set)
    pairs = set()
    networks = set()
    for l in lines_stripped(infi):
        left, right = l.split('-')
        connections[left].add(right)
        connections[right].add(left)
        pairs.add(frozenset((left, right)))

    done = set()

    def create_networks(pair):
        fpair = frozenset(pair)
        if fpair in done:
            return
        done.add(fpair)

        while newpcs := reduce(operator.and_, (connections[pc] for pc in pair)):
            if len(newpcs) > 1:
                for newpc in newpcs:
                    create_networks(pair | set((newpc,)))
                return
            pair.update(newpcs)
        networks.add(frozenset(pair))

    for pair in pairs:
        pair = set(pair)
        create_networks(pair)

    return ','.join(sorted(list(max(networks, key=lambda x: len(x)))))


DAY = 23
FILE_TEST = f"{DAY}_testa.txt"
# FILE_TEST = f"{DAY}_testb.txt"
FILE_EXP = f"{DAY}_exp.txt"
FILE = f"{DAY}.txt"
# test_and_submit(main, FILE_TEST, FILE_EXP, FILE, DAY)
# print(main(FILE_TEST))
print(main(FILE))
