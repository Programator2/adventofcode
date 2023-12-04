from aoc import *
import re
from collections import defaultdict


def main(input_file: str):
    inp = lines(input_file)
    suma = 0
    c = defaultdict(lambda: 1)
    for i in inp:
        m = re.match(r'^Card +(\d+): (.+)$', i)
        num = int(m[1])
        nums = m[2].split(' | ')
        ns = {int(nn) for nn in nums[0].split()}
        win = {int(nn) for nn in nums[1].split()}
        l = len(ns & win)
        if l:
            for j in range(num + 1, num + 1 + (l-1) + 1):
                c[j] += c[num]
        if num not in c:
            c[num] = 1
    return sum(c.values())


DAY = 4
FILE_TEST = f"{DAY}_test.txt"
FILE_EXP = f"{DAY}_expb.txt"
FILE = f"{DAY}.txt"
# test_and_submit(main, FILE_TEST, FILE_EXP, FILE)
print(main(FILE_TEST))
print(main(FILE))
