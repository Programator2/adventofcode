from aoc import *
from itertools import product
from more_itertools import windowed


def main(infi: str):
    inp = lines_stripped(infi)
    s = 0
    for line in inp:
        num, nums = line.split(': ')
        num = int(num)
        twos = list(map(int, nums.split()))
        operations = list(product('+*', repeat=len(twos) - 1))
        for ops in operations:
            res = twos[0]
            for operand, op in zip(twos[1:], ops):
                if op == '+':
                    res += operand
                elif op == '*':
                    res *= operand
            if num == res:
                s += num
                break
    return s


DAY = 7
FILE_TEST = f"{DAY}_testa.txt"
# FILE_TEST = f"{DAY}_testb.txt"
FILE_EXP = f"{DAY}_exp.txt"
FILE = f"{DAY}.txt"
# test_and_submit(main, FILE_TEST, FILE_EXP, FILE, DAY)
# print(main(FILE_TEST))
print(main(FILE))
