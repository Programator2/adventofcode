from aoc import *
from more_itertools import windowed


def is_safe(nums: list[int]) -> bool:
    twos = list(windowed(nums, 2))
    inc = [a > b for a, b in twos]
    dec = [a < b for a, b in twos]
    check = any([all(inc), all(dec)])
    if not check:
        return False
    diffs = [abs(a - b) for a, b in twos]
    t = max(diffs)
    if t > 3:
        return False
    else:
        return True


def main(infi: str):
    inp = lines_stripped(infi)
    safe = 0
    for l in inp:
        a = l.split()
        nums = [int(num) for num in a]
        twos = list(windowed(nums, 2))
        inc = [a > b for a, b in twos]
        dec = [a < b for a, b in twos]
        check = any([all(inc), all(dec)])
        if not check:
            for i, _ in enumerate(nums):
                new_l = nums[:i] + nums[i+1:]
                if is_safe(new_l):
                    safe += 1
                    break
            continue
        diffs = [abs(a - b) for a, b in twos]
        t = max(diffs)
        if t > 3:
            for i, _ in enumerate(nums):
                new_l = nums[:i] + nums[i+1:]
                if is_safe(new_l):
                    safe += 1
                    break
            continue
        else:
            safe += 1
    return safe

DAY = 2
# FILE_TEST = f"{DAY}_testa.txt"
# FILE_TEST = f"{DAY}_testb.txt"
# FILE_EXP = f"{DAY}_exp.txt"
FILE = f"{DAY}.txt"
# test_and_submit(main, FILE_TEST, FILE_EXP, FILE, DAY)
# print(main(FILE_TEST))
print(main(FILE))
