from aocd import submit
from aoc import *


FILE = '9_test.txt'
FILE = '9.txt'


def find_sum2(s, li):
    start = 0
    end = start + 2
    for start in range(0, len(li) - 2):
        if li[start] > s:
            continue
        for end in range(start + 2, len(li)):
            if sum(li[start:end+1]) == s:
                return min(li[start:end+1]) + max(li[start:end+1])


def main():
    inp = load_ints(FILE)
    out = find_sum2(776203571, inp)
    print(out)
    input()
    print('submitting')
    submit(out)


main()
