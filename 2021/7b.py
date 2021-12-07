from aocd import submit
from aoc import *
from functools import cache
from statistics import median


FILE = "7_test.txt"
FILE = "7.txt"


@cache
def nsteps(n):
    return sum(1+i-1 for i in range(1, n+1))


RANGE = 1000


def main():
    inp = load_ints_split(FILE, ',')
    count = int(median(inp))
    ans = min(sum(nsteps(abs(med-x)) for x in inp)
              for med in range(count - RANGE, count + RANGE))
    print(ans)
    return
    input()
    print("submitting")
    submit(ans)


main()
