from aoc import *
from collections import defaultdict, Counter
from more_itertools import windowed


def main(input_file: str):
    inp = filerstrip(input_file)
    template, rules = inp.split('\n\n')
    sets = defaultdict(int)
    for a, b in windowed(template, 2):
        sets[(a, b)] += 1
    rules = rules.split('\n')
    counter = Counter(template)
    for k in range(40):
        new_sets = sets.copy()
        for a, b in sets.keys():
            if sets[(a, b)] == 0:
                continue
            for r in rules:
                if (r[0], r[1]) == (a, b):
                    new_sets[(a, b)] -= sets[(a, b)]
                    new_sets[(a, r[6])] += sets[(a, b)]
                    new_sets[(r[6], b)] += sets[(a, b)]
                    counter[r[6]] += sets[(a, b)]
        sets = new_sets
    ans = counter.most_common()
    return ans[0][1] - ans[-1][1]


DAY = 14
FILE_TEST = f"{DAY}_test.txt"
FILE_EXP = f"{DAY}_exp.txt"
FILE = f"{DAY}.txt"
# test_and_submit(main, FILE_TEST, FILE_EXP, FILE)
# print(main(FILE_TEST))
print(main(FILE))
