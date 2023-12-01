# from aocd import submit
from aoc import *
from more_itertools import first_true


def main(input_file: str):
    inp = lines(input_file)
    suma = 0
    for i in inp:
        i = i.rstrip()
        a = first_true(i, pred=lambda x: x.isdigit())
        b = first_true(i[::-1], pred=lambda x: x.isdigit())
        cislo = a+b
        cislo = int(cislo)
        suma += cislo
    return suma


DAY = 1
FILE_TEST = f"{DAY}_testa.txt"
FILE_EXP = f"{DAY}_exp.txt"
FILE = f"{DAY}.txt"
# test_and_submit(main, FILE_TEST, FILE_EXP, FILE)
print(main(FILE_TEST))
print(main(FILE))
