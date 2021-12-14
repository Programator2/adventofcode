from aoc import *
from collections import Counter, deque
from more_itertools import windowed


def main(input_file: str):
    inp = filerstrip(input_file)
    template, rules = inp.split('\n\n')
    d = deque(template)
    rules = rules.split('\n')
    for k in range(10):
        to_insert = deque()
        inserted = 0
        for i, (a, b) in enumerate(windowed(d, 2)):
            for r in rules:
                if (r[0], r[1]) == (a, b):
                    to_insert.append((i+inserted+1, r[6]))
                    inserted += 1
        for r in to_insert:
            d.insert(r[0], r[1])
    c = Counter(d)
    ans = c.most_common()
    return ans[0][1] - ans[-1][1]

DAY = 14
FILE_TEST = f"{DAY}_test.txt"
FILE_EXP = f"{DAY}_exp.txt"
FILE = f"{DAY}.txt"
# test_and_submit(main, FILE_TEST, FILE_EXP, FILE)
# print(main(FILE_TEST))
print(main(FILE))
