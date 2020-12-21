from aoc import *
from collections import defaultdict
from itertools import combinations
from pprint import pprint
from math import sqrt
import re


FILE = "21_test.txt"
FILE = "21.txt"


def main():
    inp = lines(FILE)
    data = {}
    all_allergens = set()
    # This was recovered after running lower part of the code.
    # These are 8 ingredients corresponding to all 8 allergens.
    # Rest of the challenge was done using grep and paper
    found_allergens = {'ljvx', 'kllgt', 'hbfnkq', 'hfdxb', 'gnbxs', 'zxstb', 'jrnqx', 'mhtc'}
    count = 0
    for l in inp:
        m = re.match(r'^(.*) \(contains (.*)\)$', l)
        allergens = m[2].split(', ')
        allergens = frozenset(allergens)
        print(f'allergens: {allergens} ', end='')
        all_allergens.update(allergens)
        ingredients = m[1].split()
        for i in ingredients:
            if i not in found_allergens:
                count += 1
            else:
                print(i, end=', ')
        print()
        ingredients = frozenset(ingredients)
        data[allergens] = ingredients
    definitely_allergens_ing = set()
    print(count)
    return
    for a in all_allergens:
        # All data sets that contain allergen a
        t = [(k, v) for k, v in data.items() if a in k]
        al = t[0][0]
        ing = t[0][1]
        for k, v in t[1:]:
            al = al.intersection(k)
            ing = ing.intersection(v)
        definitely_allergens_ing.update(ing)
        print(f'allergen {a}: {al} is in {ing}')
    print(f'={definitely_allergens_ing}')
    count = 0
    for al, ing in data.items():
        a = ing - definitely_allergens_ing
        # print(a)
        count += len(a)
    out = count
    print(out)


main()
