from aocd import submit
import re
from aoc import *


def submita(answer):
    submit(answer, part="a", day=4, year=2020)


FILE = "4_test.txt"
FILE = "4.txt"


def main():
    with open(FILE) as f:
        i = f.read()
    i = i.split("\n\n")
    count = 0
    for k in i:
        if (
            re.search("byr", k)
            and re.search("iyr", k)
            and re.search("eyr", k)
            and re.search("hgt", k)
            and re.search("hcl", k)
            and re.search("ecl", k)
            and re.search("pid", k)
        ):
            count += 1
    print(count)
    input()
    print("done")
    submita(count)


main()
