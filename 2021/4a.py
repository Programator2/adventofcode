from aocd import submit
from aoc import *


FILE = "4_test.txt"
FILE = "4.txt"


def load_tables(l):
    tables = []
    i = 0
    while i < len(l):
        table = []
        for j in range(i, i+5):
            row = [int(i) for i in l[j].split()]
            row = [[x, 0] for x in row]
            table.append(row)
        tables.append(table)
        i += 6
    return tables


def select_numbers(l, num):
    for table in l:
        for row in table:
            for el in row:
                if el[0] == num:
                    el[1] = 1


def check_winner(l) -> int:
    for table in l:
        for i in table:
            t = [el[1] for el in i]
            if all(t):
                print(table)
                s = 0
                for row in table:
                    for el in row:
                        if el[1] == 0:
                            s += el[0]
                return s
        for i in range(5):
            t = [el[i][1] for el in table]
            if all(t):
                print(table)
                s = 0
                s = 0
                for row in table:
                    for el in row:
                        if el[1] == 0:
                            s += el[0]
                return s


def main():
    inp = lines(FILE)
    nums = [int(i) for i in inp[0].split(',')]
    inp = inp[2:]
    tables = load_tables(inp)
    for i in nums:
        select_numbers(tables, i)
        if win := check_winner(tables):
            break
    count = win * i
    print(count)
    return
    input()
    print("submitting")
    submit(count)


main()
