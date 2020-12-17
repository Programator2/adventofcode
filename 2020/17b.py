from aocd import submit
from aoc import *
from collections import defaultdict
import re


FILE = "17_test.txt"
FILE = "17.txt"


def print_slice(cube, z, start, size):
    for i in range(start, start + size):
        for j in range(start, start + size):
            print(cube[(j, i, z)], end="")
        print()
    print()


def around_active(cube, x, y, z, w):
    active = 0
    for i in range(y - 1, y + 2):
        for j in range(x - 1, x + 2):
            for k in range(z - 1, z + 2):
                for l in range(w - 1, w + 2):
                    if i == y and j == x and k == z and l == w:
                        continue
                    if cube[(j, i, k, l)] == "#":
                        active += 1
    return active


def process(cube, start, size):
    new_cube = defaultdict(lambda: ".")
    for i in range(start, start + size):
        for j in range(start, start + size):
            for z in range(start, start + size):
                for w in range(start, start + size):
                    if cube[(j, i, z, w)] == "#" and around_active(
                        cube, j, i, z, w
                    ) in (2, 3):
                        new_cube[(j, i, z, w)] = "#"
                    elif (
                        cube[(j, i, z, w)] == "."
                        and around_active(cube, j, i, z, w) == 3
                    ):
                        new_cube[(j, i, z, w)] = "#"
    return (new_cube, start - 1, size + 2)


def main():
    inp = load_map(FILE)
    cubes = defaultdict(lambda: ".")
    for i, y in enumerate(inp):
        for j, x in enumerate(y):
            cubes[(j, i, 0, 0)] = x
    start = -1
    size = len(inp) + 2
    for x in range(6):
        cubes, start, size = process(cubes, start, size)
    out = len(list(x for x in cubes.values() if x == "#"))
    print(out)
    return
    input()
    print("submitting")
    submit(out)


main()
