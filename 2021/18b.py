from aoc import *
from copy import deepcopy
from math import ceil
from itertools import permutations


def get_depth(a: list, depth: int, stack: list):
    for i, l in enumerate(a):
        if type(l) == list:
            if depth >= 4:
                if type(l[0]) == list or type(l[1]) == list:
                    return get_depth(l, depth + 1, stack + [i])
                return stack + [i]
            if ret := get_depth(l, depth + 1, stack + [i]):
                return ret
    return False


def get_element(a: list, stack: list):
    for i in stack:
        a = a[i]
    return a


def search_rightmost(a: list, stack: list):
    while True:
        e = get_element(a, stack)
        if type(e) == list:
            stack = stack + [1]
        else: return stack


def search_left(a: list, stack: list):
    for i in reversed(range(len(stack))):
        if stack[i] == 1:
            return search_rightmost(a, stack[:i] + [0])
    return []


def search_leftmost(a: list, stack: list):
    while True:
        e = get_element(a, stack)
        if type(e) == list:
            stack = stack + [0]
        else: return stack


def search_right(a: list, stack: list):
    for i in reversed(range(len(stack))):
        if stack[i] == 0:
            return search_leftmost(a, stack[:i] + [1])
    return []


def add(a: list, stack: list, num: int):
    for i in stack[:-1]:
        a = a[i]
    a[stack[-1]] += num


def delete(a: list, stack: list):
    for i in stack[:-1]:
        a = a[i]
    a[stack[-1]] = 0


def reduce(a: list) -> bool:
    if explode := get_depth(a, 1, []):
        to_explode = get_element(a, explode)
        left = search_left(a, explode)
        right = search_right(a, explode)
        # explode
        if left:
            add(a, left, to_explode[0])
        if right:
            add(a, right, to_explode[1])
        delete(a, explode)
        return True
    else:
        return False


def split(a: list):
    for i, l in enumerate(a):
        if type(l) == list:
            if ret := split(l):
                return ret
        elif l > 9:
            a[i] = [l // 2, int(ceil(l / 2))]
            return True
    return False


def add_numbers(a:list, b:list) -> list:
    r = [a, b]
    t = True
    while t:
        t = False
        while reduce(r):
            t = True
        if split(r):
            t = True
    return r


def magnitude(r):
    if type(r[0]) == list:
        a = magnitude(r[0]) * 3
    else:
        a = r[0] * 3
    if type(r[1]) == list:
        b = magnitude(r[1]) * 2
    else:
        b = r[1] * 2
    return a + b

def main(input_file: str):
    inp = load_map(input_file)
    return max(
        magnitude(
            add_numbers(deepcopy(a), deepcopy(b))) for (a, b) in permutations(
                (eval(i) for i in inp), 2))


DAY = 18
FILE_TEST = f"{DAY}_test.txt"
FILE_EXP = f"{DAY}_exp.txt"
FILE = f"{DAY}.txt"
# test_and_submit(main, FILE_TEST, FILE_EXP, FILE)
# print(main(FILE_TEST))
print(main(FILE))
