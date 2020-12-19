from aocd import submit
from aoc import *
from collections import defaultdict
from itertools import chain


FILE = "19_test2.txt"
FILE = "19.txt"


def check_rule(string, rules, rule):
    r = rules[rule]
    matched_parts_global = []  # what was matched by this function
    for ri in r:
        cp_string = [string[:]]
        matched_parts_for_rule = [""]
        # founds = []                 # what was matched by called functions
        if type(ri) is str:
            if string.startswith(ri):
                return [ri]
            continue
        for n in ri:
            # Call for every possible cp_string
            found = list(
                chain.from_iterable(check_rule(s, rules, n) for s in cp_string)
            )
            if not found:
                break
            else:
                found = list(set(found))
                matched_parts_for_rule = list(
                    m + f for m in matched_parts_for_rule for f in found
                )
            cp_string = list(c[len(f) :] for c in cp_string for f in found)
        if "" not in matched_parts_for_rule:
            matched_parts_global.extend(matched_parts_for_rule)
    return matched_parts_global


def check_string(string, rules):
    print("checking", string)
    if string in check_rule(string, rules, 0):
        # print(string)
        return True
    return False


def main():
    inp = file(FILE)
    rules = defaultdict(list)
    r, inp = inp.split("\n\n")
    r = r.split("\n")
    inp = inp.split()
    for rule in r:
        number, ruleset = rule.split(":")
        if '"' in ruleset:
            rules[int(number)].append(ruleset[2])
        else:
            if "|" in ruleset:
                left, right = ruleset.split("|")
            else:
                left, right = ruleset, None
            for i in (left, right):
                if i is not None:
                    numbers = i.split()
                    numbers = tuple(int(n) for n in numbers)
                    rules[int(number)].append(numbers)
    out = sum(1 for l in inp if check_string(l, rules))
    print(out)
    return
    input()
    print("submitting")
    submit(out)


main()
