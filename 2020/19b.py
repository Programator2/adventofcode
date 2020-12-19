from aocd import submit
from aoc import *
from collections import defaultdict
from itertools import chain


FILE = "19_test2.txt"
FILE = "19_2.txt"


def check_rule(string, rules, rule, special_r=None):
    if rule in [8, 11]:
        # repeating 42 42 42 ... 31 31 31, the same number
        matched_parts_for_rule = set()
        i = 1
        while found := list(
            chain.from_iterable((check_rule(string, rules, None, [(42,) * i]),))
        ):
            mcopy = matched_parts_for_rule.copy()
            matched_parts_for_rule.update(found)
            if mcopy == matched_parts_for_rule:
                break
            i += 1

        if rule == 8:
            ret = [m for m in matched_parts_for_rule if string.startswith(m)]
            return ret

        matched_parts_for_rule = set()
        i -= 1
        while (i >= 1) and (
            found := list(
                chain.from_iterable(
                    (check_rule(string, rules, None, [(42,) * i + (31,) * i]),)
                )
            )
        ):
            mcopy = matched_parts_for_rule.copy()
            matched_parts_for_rule.update(found)
            if mcopy == matched_parts_for_rule:
                break
            i -= 1
        ret = [m for m in matched_parts_for_rule if string.startswith(m)]
        return ret

    r = rules[rule] if special_r is None else special_r
    matched_parts_global = []  # what was matched by this function
    for ri in r:
        cp_string = [string[:]]
        matched_parts_for_rule = [""]
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
                matched_parts_for_rule = [""]
                break
            else:
                found = list(set(found))
                matched_parts_for_rule = list(
                    m + f
                    for m in matched_parts_for_rule
                    for f in found
                    if string.startswith(m + f)
                )
            cp_string = list(
                c[len(f) :] for c in cp_string for f in found if c.startswith(f)
            )
        if matched_parts_for_rule != [""]:
            matched_parts_global.extend(matched_parts_for_rule)
    ret = list(set(matched_parts_global))
    ret = [r for r in ret if string.startswith(r)]
    return ret


def check_string(string, rules):
    print(f"Checking {string}: ", end="")
    i = check_rule(string, rules, 0)
    if string in i:
        print(f"MATCH with {i}")
        return True
    print("NO")
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
