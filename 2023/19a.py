from aoc import *
import re
from collections import defaultdict


def main(input_file: str):
    inp = filerstrip(input_file)
    workflows, parts = inp.split('\n\n')
    workflows = workflows.split('\n')
    parts = parts.split('\n')
    workd = defaultdict(list)
    for i in workflows:
        workflow, instructions = i[:-1].split('{')
        instructions = instructions.split(',')
        for ins in instructions[:-1]:
            prop = ins[0]
            operat = ins[1]
            numb, dest = ins[2:].split(':')
            numb = int(numb)
            workd[workflow].append((prop, operat, numb, dest))
        workd[workflow].append((None, None, None, instructions[-1]))
    partsl = []
    for p in parts:
        m = re.match(r'^{x=(\d+),m=(\d+),a=(\d+),s=(\d+)}$', p)
        partsl.append({
            'x': int(m[1]),
            'm': int(m[2]),
            'a': int(m[3]),
            's': int(m[4]),
        })
    suma = 0
    for p in partsl:
        work = 'in'
        while True:
            for prop, operat, numb, dest in workd[work]:
                if prop is None:
                    work = dest
                    break
                if operat == '<':
                    if p[prop] < numb:
                        work = dest
                        break
                elif p[prop] > numb:
                    work = dest
                    break

            if work == 'A':
                suma += sum(p.values())
                break
            elif work == 'R':
                break

    return suma


DAY = 19
FILE_TEST = f"{DAY}_test.txt"
FILE_EXP = f"{DAY}_expa.txt"
FILE = f"{DAY}.txt"
# test_and_submit(main, FILE_TEST, FILE_EXP, FILE, DAY)
print(main(FILE_TEST))
print(main(FILE))
