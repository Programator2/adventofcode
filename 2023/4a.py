from aoc import *
import re


def main(input_file: str):
    inp = lines(input_file)
    suma = 0
    for i in inp:
        m = re.match(r'^Card +(\d+): (.+)$', i)
        num = int(m[1])
        nums = m[2].split(' | ')
        ns = {int(nn) for nn in nums[0].split()}
        win = {int(nn) for nn in nums[1].split()}
        l = len(ns & win)
        if l:
            suma += 2 ** (l - 1)
    return suma


DAY = 4
FILE_TEST = f"{DAY}_test.txt"
FILE_EXP = f"{DAY}_expa.txt"
FILE = f"{DAY}.txt"
# test_and_submit(main, FILE_TEST, FILE_EXP, FILE)
print(main(FILE_TEST))
print(main(FILE))
