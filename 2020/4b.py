from aocd import submit
import re
from aoc import *


def submitb(answer):
    submit(answer, part="b", day=4, year=2020)


FILE = "4_test.txt"
FILE = "4.txt"


def check_hgt(hgt):
    n = int(hgt[1])
    units = hgt[2]
    if units == "cm":
        return 150 <= n <= 193
    if units == "in":
        return 59 <= n <= 76
    return False


def main():
    with open(FILE) as f:
        i = f.read()
    i = i.split("\n\n")
    count = 0
    for k in i:
        if (
            (byr := re.search(r"byr:(\d{4})", k))
            and (iyr := re.search(r"iyr:(\d{4})", k))
            and (eyr := re.search(r"eyr:(\d{4})", k))
            and (hgt := re.search(r"hgt:(\d+)(..)", k))
            and (re.search(r"hcl:#[0-9a-f]{6}", k))
            and (ecl := re.search(r"ecl:(...)", k))
            and (pid := re.search(r"pid:(\d+)", k))
        ):
            if (
                1920 <= int(byr[1]) <= 2002
                and 2010 <= int(iyr[1]) <= 2020
                and 2020 <= int(eyr[1]) <= 2030
                and check_hgt(hgt)
                and ecl[1] in ("amb", "blu", "brn", "gry", "grn", "hzl", "oth")
                and len(pid[1]) == 9
            ):
                count += 1
    print(count)
    input()
    print("done")
    submitb(count)


main()
