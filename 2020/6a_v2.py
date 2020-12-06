import re
from aoc import *


FILE = "6_test.txt"
FILE = "6.txt"


def main():
    with open(FILE) as f:
        i = f.read()
    count = sum(len(set(k.replace("\n", ""))) for k in i.split("\n\n"))
    print(count)


main()
