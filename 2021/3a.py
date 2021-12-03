from aocd import submit
from aoc import *
from blessed import BlessedList


FILE = "3_test.txt"
FILE = "3.txt"


def get_binary_str(l):
    ret = ''
    for i in l.data:
        ret = ret + str(i)
    return ret


def main():
    inp = load_map_ll(FILE)
    length = len(inp[0])
    num_j = [0] * length
    num_n = [0] * length
    for i in inp:
        for d, j in enumerate(i):
            if j == '1':
                num_j[d] += 1
            else:
                num_n[d] += 1
    gamma = BlessedList()
    for j in reversed(range(length)):
        if num_j[j] > num_n[j]:
            gamma[j] = 1
        else:
            gamma[j] = 0
    gamma = int(get_binary_str(gamma), 2)
    epsilon = BlessedList()
    for j in reversed(range(length)):
        if num_j[j] < num_n[j]:
            epsilon[j] = 1
        else:
            epsilon[j] = 0
    epsilon = int(get_binary_str(epsilon), 2)
    count = gamma * epsilon
    print(count)
    return
    input()
    print("submitting")
    submit(count)


main()
