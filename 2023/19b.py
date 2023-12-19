from aoc import *
from functools import reduce
import operator
from collections import defaultdict


def intersec(a: tuple[int, int], b: tuple[int, int]):
    start = max(a[0], b[0])
    end = min(a[1], b[1])
    if start < end:
        return (start, end)
    return None


def search(ranges: dict[str, tuple[int, int]], workflow: str, workflows: dict[str, list[tuple]]):
    if workflow == 'R':
        return []
    if workflow == 'A':
        return [ranges]
    out_ranges = []
    for i, (prop, operat, numb, dest) in enumerate(workflows[workflow]):
        if prop is None:
            # This should be the last one
            assert i == len(workflows[workflow]) - 1
            out_ranges.extend(search(ranges, dest, workflows))
            break
        if operat == '<':
            yes_interval = (1, numb)
            no_interval = (numb, 4001)
        elif operat == '>':
            no_interval = (1, numb + 1)
            yes_interval = (numb + 1, 4001)

        new = intersec(ranges[prop], yes_interval)
        if new is not None:
            out_ranges.extend(search(ranges | {prop: new},
                                     dest, workflows))
        # Do the other side
        new = intersec(ranges[prop], no_interval)
        if new is None:
            return out_ranges
        ranges[prop] = new
    return out_ranges


# Very nice puzzle, I enjoyed this one the most so far in 2023.
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

    r = {
        'x': (1, 4001),
        'm': (1, 4001),
        'a': (1, 4001),
        's': (1, 4001),
    }
    ranges = search(r, 'in', workd)
    return sum(reduce(operator.mul, (b - a for a, b in d.values())) for d in ranges)


DAY = 19
FILE_TEST = f"{DAY}_test.txt"
FILE_EXP = f"{DAY}_expb.txt"
FILE = f"{DAY}.txt"
# test_and_submit(main, FILE_TEST, FILE_EXP, FILE, DAY)
print(main(FILE_TEST))
print(main(FILE))
