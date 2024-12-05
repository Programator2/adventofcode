from aoc import *
from itertools import combinations


def soort(update: list[int], order):
    return sorted(
        update, key=cmp_to_key(lambda a, b: -1 if b in order[a] else 1)
    )


def main(infi: str):
    rules, bb = filerstrip(infi).split('\n\n')
    cor_order = defaultdict(set)
    for r in rules.split('\n'):
        a, b = map(int, r.split('|'))
        cor_order[a].add(b)
    s = 0
    for update in bb.split('\n'):
        update = [int(x) for x in update.split(',')]
        for a, b in combinations(update, 2):
            if b not in cor_order[a]:
                new = soort(update, cor_order)
                s += new[len(new) // 2]
                break
    return s


DAY = 5
FILE_TEST = f"{DAY}_testa.txt"
# FILE_TEST = f"{DAY}_testb.txt"
FILE_EXP = f"{DAY}_exp.txt"
FILE = f"{DAY}.txt"
# test_and_submit(main, FILE_TEST, FILE_EXP, FILE, DAY)
# print(main(FILE_TEST))
print(main(FILE))
