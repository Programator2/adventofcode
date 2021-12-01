from aocd import submit
from aoc import *
from more_itertools import windowed


FILE = "1_test.txt"
FILE = "1.txt"


def main():
    inp = load_ints(FILE)
    prev = None
    count = 0
    inp = windowed(inp, 3)
    for i in inp:
        if prev is not None:
            if sum(i) > prev:
                count +=1
        prev = sum(i)
    print(count)
    return
    input()
    print("submitting")
    submit(count)


main()
