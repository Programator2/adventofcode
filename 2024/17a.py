from aoc import *


def main(infi: str):
    inp = filerstrip(infi)
    registers, program = inp.split('\n\n')
    a, b, c = map(
        lambda x: int(x[len('Register A: ') :]), registers.split('\n')
    )

    def combo(op):
        if 0 <= op <= 3:
            return op
        elif op == 4:
            return a
        elif op == 5:
            return b
        elif op == 6:
            return c
        raise RuntimeError('combo')

    prog = list(map(int, program[len('Program: ') :].split(',')))
    ip = 0
    out = []
    while 0 <= ip < len(prog):
        if prog[ip] == 0:
            a = a // (2 ** combo(prog[ip + 1]))
        elif prog[ip] == 1:
            b = b ^ prog[ip + 1]
        elif prog[ip] == 2:
            b = combo(prog[ip + 1]) % 8
        elif prog[ip] == 3:
            if a:
                ip = prog[ip + 1]
                continue
        elif prog[ip] == 4:
            b = b ^ c
        elif prog[ip] == 5:
            out.append(combo(prog[ip + 1]) % 8)
            # print(out[-1])
        elif prog[ip] == 6:
            b = a // (2 ** combo(prog[ip + 1]))
        elif prog[ip] == 7:
            c = a // (2 ** combo(prog[ip + 1]))
        ip += 2
    return ','.join(map(str, out))


DAY = 17
FILE_TEST = f"{DAY}_testa.txt"
# FILE_TEST = f"{DAY}_testb.txt"
FILE_EXP = f"{DAY}_exp.txt"
FILE = f"{DAY}.txt"
# test_and_submit(main, FILE_TEST, FILE_EXP, FILE, DAY)
# print(main(FILE_TEST))
print(main(FILE))
