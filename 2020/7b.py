from aocd import submit
import re
from aoc import *
from collections import defaultdict


def submita(answer):
    submit(answer, part='a', day=7, year=2020)


def submitb(answer):
    submit(answer, part='b', day=7, year=2020)


FILE = '7_test.txt'
FILE = '7_test2.txt'
FILE = '7.txt'


class Bag:
    def __init__(self):
        self.name = None
        self.parents = set()
        self.children = {}


def downtrack(bag, bags):
    number = 1
    for p, n in bag.children.items():
        print(p, n)
        number += n * downtrack(bags[p], bags)
    return number


def main():
    inp = lines(FILE)
    bags = defaultdict(Bag)
    for l in inp:
        b = re.match(r'(.+ .+) bags contain (.+)\.|(.+ .+) bags contain no other bags\.', l)
        outer_bag = b[1]
        inside = b[2]
        if inside != 'no other bags':
            ins = re.findall(r'(\d+) (.+? .+?) bags?(?:, )?', inside)
            for number, name in ins:
                bags[outer_bag].children[name] = int(number)
                bags[name].parents.add(outer_bag)
    for k, v in bags.items():
        v.name = k
    print('OK')
    out = downtrack(bags['shiny gold'], bags)
    out -= 1
    print(out)
    input()
    print('submitting')
    submitb(out)


main()
