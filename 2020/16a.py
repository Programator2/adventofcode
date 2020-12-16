from aocd import submit
from aoc import *
from collections import defaultdict
import re


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


def main():
    inp = lines(FILE)
    i = 0
    fields = {}
    while inp[i] != '\n':
        m = re.search(r'^(.+): (\d+)-(\d+) or (\d+)-(\d+)$', inp[i])
        fields[m[1]] = ((int(m[2]), int(m[3])), (int(m[4]), int(m[5])))
        i += 1
    i += 1
    i += 1
    my_ticket = [int(i) for i in inp[i].split(',')]
    i += 1
    i += 1
    i += 1
    nearby_tickets = []
    while i < len(inp):
        print(inp[i])
        nearby_tickets.append([int(i) for i in inp[i].rstrip().split(',')])
        i += 1
    out = sum(in_range(t, fields) for t in nearby_tickets)
    print(out)
    # return
    input()
    print("submitting")
    submit(out)


main()
