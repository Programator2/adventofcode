from aocd import submit
from aoc import *


FILE = "3_test.txt"
FILE = "3.txt"


def most_common(pos, l):
    jedn = []
    nul = []
    velkost = len(l[0])
    pocet_j = 0
    pocet_n = 0
    for i in l:
        if i[pos] == '1':
            pocet_j += 1
            jedn.append(i)
        else:
            pocet_n += 1
            nul.append(i)
    if pocet_j >= pocet_n:
        return jedn
    else:
        return nul


def least_common(pos, l):
    jedn = []
    nul = []
    velkost = len(l[0])
    pocet_j = 0
    pocet_n = 0
    for i in l:
        if i[pos] == '1':
            pocet_j += 1
            jedn.append(i)
        else:
            pocet_n += 1
            nul.append(i)
    if pocet_j < pocet_n:
        return jedn
    else:
        return nul


def to_decimal(l):
    ret = ''
    for i in l:
        ret = ret + str(i)
    return int(ret, 2)


def main():
    inp = load_map_ll(FILE)
    oxy = inp.copy()
    pos = 0
    while(len(oxy) != 1):
        oxy = most_common(pos, oxy)
        pos += 1
    oxy = to_decimal(oxy[0])
    co = inp.copy()
    pos = 0
    while(len(co) != 1):
        co = least_common(pos, co)
        pos += 1
    co = to_decimal(co[0])
    count = oxy * co
    print(count)
    return
    input()
    print("submitting")
    submit(count)


main()
