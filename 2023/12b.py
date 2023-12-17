from aoc import *
from more_itertools import ncycles
from heapq import *
from itertools import repeat


# Inspiration from https://www.reddit.com/r/adventofcode/comments/18ge41g/comment/kd03uf3/?utm_source=share&utm_medium=web2x&context=3
@cache
def count(condition: str, groups: tuple[int], cur_grp_len: int):
    if not condition:
        if not groups and not cur_grp_len:
            return 1
        else:
            return 0
    if condition[0] == '.':
        if cur_grp_len:
            return 0
        return count(condition[1:], groups, cur_grp_len)
    if condition[0] == '#':
        if not groups:
            return 0
        cur_grp_len += 1
        if cur_grp_len == groups[0]:
            if len(condition) > 1:
                if condition[1] == '#':
                    # We are ending a group, the next one can't be #
                    return 0
                elif condition[1] == '?':
                    # We are ending a group, the next one has to be a .
                    condition = condition[0] + '.' + condition[2:]
            groups = groups[1:]
            cur_grp_len = 0
        return count(condition[1:], groups, cur_grp_len)
    if condition[0] == '?':
        return (count('.' + condition[1:], groups, cur_grp_len) +
                count('#' + condition[1:], groups, cur_grp_len))
    raise Exception('END')


def main(input_file: str):
    inp = lines(input_file)
    records = []
    for x in inp:
        x = x.split()
        records.append((x[0], tuple(int(y) for y in x[1].split(','))))
    return sum(count(
        '?'.join(repeat(springs, 5)),
        tuple(ncycles(nums, 5)), 0) for springs, nums in records)


DAY = 12
FILE_TEST = f"{DAY}_test.txt"
FILE_EXP = f"{DAY}_expb.txt"
FILE = f"{DAY}.txt"
# test_and_submit(main, FILE_TEST, FILE_EXP, FILE, 12)
print(main(FILE_TEST))
print(main(FILE))
