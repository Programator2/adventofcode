from aocd import submit
from aoc import *
from collections import defaultdict
import re
from pprint import pprint
from math import prod


FILE = "16_test.txt"
FILE = "16.txt"


def in_range(ticket, fields):
    error = 0
    for number in ticket:
        valid = False
        for ((a, b), (c, d)) in fields.values():
            if number in range(a, b + 1):
                valid = True
                break
            if number in range(c, d + 1):
                valid = True
                break
        if not valid:
            error += number
    return error


def entry_with_len_1_exists(fields):
    for names in fields.values():
        if len(names) == 1:
            return True
    return False


def main():
    inp = lines(FILE)
    i = 0
    fields = {}
    while inp[i] != "\n":
        m = re.search(r"^(.+): (\d+)-(\d+) or (\d+)-(\d+)$", inp[i])
        fields[m[1]] = ((int(m[2]), int(m[3])), (int(m[4]), int(m[5])))
        i += 1
    i += 1
    i += 1
    my_ticket = [int(i) for i in inp[i].split(",")]
    i += 1
    i += 1
    i += 1
    nearby_tickets = []
    while i < len(inp):
        nearby_tickets.append([int(i) for i in inp[i].rstrip().split(",")])
        i += 1
    out = 0
    valid_tickets = [t for t in nearby_tickets if in_range(t, fields) == 0]
    valid_tickets.append(my_ticket)

    field_values = [*zip(*valid_tickets)]
    possible_type = defaultdict(list)  # int -> [str]
    for i, values in enumerate(field_values):
        for name, ((a, b), (c, d)) in fields.items():
            for number in values:
                if number not in range(a, b + 1):
                    if number not in range(c, d + 1):
                        break
            else:
                possible_type[i].append(name)

    for names in possible_type.values():
        if len(names) == 1:
            for remove_in_this in possible_type.values():
                if len(remove_in_this) > 1:
                    try:
                        remove_in_this.remove(names[0])
                    except ValueError:
                        pass

    change = True
    while change:
        change = False
        for f in fields:
            possibles = [i for i in possible_type.values() if f in i]
            if len(possibles) == 1 and len(possibles[0]) != 1:
                # remove this field from others
                for names in possible_type.values():
                    try:
                        names.remove(f)
                    except ValueError:
                        pass
                # remove others from this field
                possibles[0].clear()
                possibles[0].append(f)
                change = True

    out = prod(
        my_ticket[idx]
        for idx, names in possible_type.items()
        if names[0].startswith("departure")
    )
    print(out)
    return
    input()
    print("submitting")
    submit(out)


main()
