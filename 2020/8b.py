from aocd import submit
from aoc import *


def submitb(answer):
    submit(answer, part='b', day=8, year=2020)


FILE = '8_test.txt'
FILE = '8.txt'


def main():
    inp = lines(FILE)
    acc = 0
    ins = set([0])
    ip = 0
    nops = []
    jmps = []
    for n, l in enumerate(inp):
        if inp[n][:3] == 'nop':
            nops.append(n)
        elif inp[n][:3] == 'jmp':
            jmps.append(n)
    terminated = False
    for n in nops:
        ins = set([0])
        ip = 0
        acc = 0
        inp[n] = 'jmp ' + inp[n][4:]
        while True:
            torun = inp[ip][:3]
            print(torun)
            if torun == 'nop':
                ip += 1
                if ip == len(inp):
                    terminated = True
                    break
                ip %= len(inp)
                if ip in ins:
                    break
                ins.add(ip)
            elif torun == 'jmp':
                ip += int(inp[ip][4:])
                if ip == len(inp):
                    terminated = True
                    break
                ip %= len(inp)
                if ip in ins:
                    break
                ins.add(ip)
            elif torun == 'acc':
                acc += int(inp[ip][4:])
                ip += 1
                if ip == len(inp):
                    terminated = True
                    break
                ip %= len(inp)
                if ip in ins:
                    break
                ins.add(ip)
        inp[n] = 'nop ' + inp[n][4:]
        if terminated:
            break
    if not terminated:
        for n in jmps:
            ins = set([0])
            ip = 0
            acc = 0
            inp[n] = 'nop ' + inp[n][4:]
            while True:
                torun = inp[ip][:3]
                print(torun)
                if torun == 'nop':
                    ip += 1
                    if ip == len(inp):
                        terminated = True
                        break
                    ip %= len(inp)
                    if ip in ins:
                        break
                    ins.add(ip)
                elif torun == 'jmp':
                    ip += int(inp[ip][4:])
                    if ip == len(inp):
                        terminated = True
                        break
                    ip %= len(inp)
                    if ip in ins:
                        break
                    ins.add(ip)
                elif torun == 'acc':
                    acc += int(inp[ip][4:])
                    ip += 1
                    if ip == len(inp):
                        terminated = True
                        break
                    ip %= len(inp)
                    if ip in ins:
                        break
                    ins.add(ip)
            inp[n] = 'jmp ' + inp[n][4:]
            if terminated:
                break
    out = acc
    print(out)
    input()
    print('submitting')
    submitb(out)


main()
