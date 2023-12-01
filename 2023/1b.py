from aoc import *


numbers = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']


def main(input_file: str):
    inp = lines(input_file)
    suma = 0
    for i in inp:
        fin = False
        for x in range(0, len(i)):
            if i[x].isdigit():
                a = i[x]
                break
            for ni, n in enumerate(numbers):
                if i[x:].startswith(n):
                    a = str(ni+1)
                    fin = True
                    break
            if fin:
                break
        fin = False
        for x in range(len(i)-1, -1, -1):
            if i[x].isdigit():
                b = i[x]
                break
            for ni, n in enumerate(numbers):
                if i[x:].startswith(n):
                    b = str(ni+1)
                    fin = True
                    break
            if fin:
                break
        cislo = str(a)+str(b)
        cislo = int(cislo)
        suma += cislo
    return suma


DAY = 1
FILE_TEST = f"{DAY}_testb.txt"
FILE_EXP = f"{DAY}_exp.txt"
FILE = f"{DAY}.txt"
# test_and_submit(main, FILE_TEST, FILE_EXP, FILE)
print(main(FILE_TEST))
print(main(FILE))
