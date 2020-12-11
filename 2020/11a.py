from aocd import submit
from aoc import *
from collections import Counter
from copy import deepcopy


def submita(answer):
    submit(answer, part="a", day=11, year=2020)


def submitb(answer):
    submit(answer, part="b", day=11, year=2020)


FILE = "11_test.txt"
FILE = "11.txt"


def print_map(li):
    return
    for i in range(1, len(li) - 1):
        for j in range(1, len(li[0]) - 1):
            print(li[i][j], end="")
        print()


def check_coord(li):
    new_li = deepcopy(li)
    changed = 0
    for i in range(1, len(li) - 1):
        for j in range(1, len(li[0]) - 1):
            if li[i][j] == "L":
                around = Counter(
                    (
                        li[i - 1][j - 1],
                        li[i - 1][j],
                        li[i - 1][j + 1],
                        li[i][j - 1],
                        li[i][j + 1],
                        li[i + 1][j - 1],
                        li[i + 1][j],
                        li[i + 1][j + 1],
                    )
                )
                if "#" not in around:
                    new_li[i][j] = "#"
                    changed += 1
            if li[i][j] == "#":
                around = Counter(
                    (
                        li[i - 1][j - 1],
                        li[i - 1][j],
                        li[i - 1][j + 1],
                        li[i][j - 1],
                        li[i][j + 1],
                        li[i + 1][j - 1],
                        li[i + 1][j],
                        li[i + 1][j + 1],
                    )
                )
                if around.get("#", 0) >= 4:
                    new_li[i][j] = "L"
                    changed += 1
    return new_li, changed


def main():
    inp = load_map_ll(FILE)
    out = 0
    inp.insert(0, ["."] * len(inp[0]))
    inp.append(["."] * len(inp[0]))
    for l in inp:
        l.insert(0, ".")
        l.append(".")
    changed = 1
    while changed != 0:
        print_map(inp)
        inp, changed = check_coord(inp)
    print_map(inp)
    c = Counter()
    for i in range(1, len(inp) - 1):
        for j in range(1, len(inp[0]) - 1):
            c.update(inp[i][j])
    print(c["#"])
    input()
    print("submitting")
    submita(c["#"])


main()
