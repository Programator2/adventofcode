from aocd import submit
import re
from aoc import *
from collections import defaultdict


def submita(answer):
    submit(answer, part='a', day=7, year=2020)


def submitb(answer):
    submit(answer, part='b', day=7, year=2020)


FILE = '7_test.txt'
FILE = '7.txt'


class Bag:
    def __init__(self):
        self.name = None
        self.parents = set()
        self.children = {}


def backtrack(bag, s, bags, depth):
    for p in bag.parents:
        if p not in s:
            s.add(p)
            backtrack(bags[p], s, bags, depth+1)


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
    contain_gold = set()
    backtrack(bags['shiny gold'], contain_gold, bags, 1)
    out = len(contain_gold)
    print(out)
    input()
    print('submitting')
    submita(out)


main()
