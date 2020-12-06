from aoc import *


def main():
    lines = load_ints('1.txt')
    print(sum(i*j for i in lines for j in lines if i + j == 2020))


main()
