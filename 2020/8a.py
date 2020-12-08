from aocd import submit
from aoc import *


def submita(answer):
    submit(answer, part='a', day=8, year=2020)


FILE = '8_test.txt'
FILE = '8.txt'


def main():
    inp = lines(FILE)
    acc = 0
    ins = set([0])
    ip = 0
    while True:
        torun = inp[ip][:3]
        if torun == 'nop':
            ip += 1
            ip %= len(inp)
            if ip in ins:
                break
            ins.add(ip)
        elif torun == 'jmp':
            ip += int(inp[ip][4:])
            ip %= len(inp)
            if ip in ins:
                break
            ins.add(ip)
        elif torun == 'acc':
            acc += int(inp[ip][4:])
            ip += 1
            ip %= len(inp)
            if ip in ins:
                break
            ins.add(ip)
    out = acc
    print(out)
    input()
    print('submitting')
    submita(out)


main()
