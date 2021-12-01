from aocd import submit
from aoc import *


FILE = "1_test.txt"
FILE = "1.txt"


def main():
    inp = load_ints(FILE)
    prev = None
    count = 0
    for i in inp:
        if prev is not None:
            if i > prev:
                count +=1
        prev = i
    print(count)
    return
    input()
    print("submitting")
    submit(count)


main()
