from aocd import submit
from aoc import *


def submita(answer):
    submit(answer, part='a', day=9, year=2020)


FILE = '9_test.txt'
FILE = '9.txt'


def find_sum(s, li):
    for i, a in enumerate(li):
        for j, b in enumerate(li):
            if i == j:
                continue
            if a + b == s:
                return True
    return False


def main():
    inp = load_ints(FILE)
    len_pre = 25
    for i in range(len(inp)-len_pre-2):
        if not find_sum(inp[i+len_pre], inp[i:i+len_pre]):
            out = inp[i+len_pre]
    print(out)
    input()
    print('submitting')
    submita(out)


main()
