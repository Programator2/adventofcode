from aocd import submit
from aoc import *
from statistics import median


FILE = "7_test.txt"
FILE = "7.txt"


def main():
    inp = load_ints_split(FILE, ',')
    count = int(median(inp))
    ans = sum(abs(count-x) for x in inp)
    print(ans)
    return
    input()
    print("submitting")
    submit(ans)


main()
