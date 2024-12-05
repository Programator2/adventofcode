from aoc import *
from itertools import combinations


def main(infi: str):
    rules, pages = filerstrip(infi).split('\n\n')
    cor_order = defaultdict(set)
    for rule in rules.split('\n'):
        a, b = map(int, rule.split('|'))
        cor_order[a].add(b)
    return sum(
        update[len(update) // 2]
        for update in map(
            lambda line: list(map(int, line.split(','))), pages.split('\n')
        )
        if all(b in cor_order[a] for a, b in combinations(update, 2))
    )
    return s


DAY = 5
FILE_TEST = f"{DAY}_testa.txt"
# FILE_TEST = f"{DAY}_testb.txt"
FILE_EXP = f"{DAY}_exp.txt"
FILE = f"{DAY}.txt"
# test_and_submit(main, FILE_TEST, FILE_EXP, FILE, DAY)
# print(main(FILE_TEST))
print(main(FILE))
