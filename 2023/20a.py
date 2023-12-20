from aoc import *
from collections import defaultdict, deque


def main(input_file: str):
    inp = lines(input_file)
    op = defaultdict(dict)
    state = defaultdict(lambda: 0)
    conj_state = defaultdict(dict)

    def receive(name, sender, inp):
        state[name] = not state[name]
        return state[name]

    def conj(name, sender, inp):
        conj_state[name][sender] = inp
        if all(x for x in conj_state[name].values()):
            return 0
        return 1

    conjunctions = set()
    for l in inp:
        l = l.rstrip()
        left, right = l.split(' -> ')
        if left == 'broadcaster':
            typ = 'broadcaster'
            name = 'broadcaster'
        else:
            typ = left[0]
            name = left[1:]
        outputs = right.split(', ')
        if typ == '&':
            op[name][0] = (conj, outputs)
            op[name][1] = (conj, outputs)
            conjunctions.add(name)
        elif typ == '%':
            op[name][0] = (receive, outputs)
            op[name][1] = (lambda x, y, z: None, [])
        elif typ == 'broadcaster':
            op[name][0] = (lambda x, y, z: 0, outputs)
            op[name][1] = (lambda x, y, z: 1, outputs)
        else:
            raise Exception('BAD')

    # Initialize conjunction inputs
    for sender, pulse in op.items():
        outputs = set(pulse[0][1])
        if common_outputs := conjunctions & outputs:
            for c in common_outputs:
                conj_state[c][sender] = 0

    low = 0
    high = 0
    for i in range(1000):
        # receiver, pulse, sender
        q = deque([('broadcaster', 0, 'button')])
        while q:
            receiver, pulse, sender = q.popleft()
            # print(f'{sender} -{'high' if pulse else 'low'}-> {receiver}')
            if pulse:
                high += 1
            else:
                low += 1
            try:
                fn, outputs = op[receiver][pulse]
            except KeyError:
                continue
            new_pulse = fn(receiver, sender, pulse)
            if new_pulse is not None:
                for o in outputs:
                    q.append((o, new_pulse, receiver))
    return low * high


DAY = 20
FILE_TEST1 = f"{DAY}_test.txt"
FILE_EXP1 = f"{DAY}_expa.txt"
FILE_TEST2 = f"{DAY}_test2.txt"
FILE_EXP2 = f"{DAY}_expa2.txt"
FILE = f"{DAY}.txt"
# test_and_submit(main, FILE_TEST, FILE_EXP, FILE, DAY)
print(main(FILE_TEST1))
print(main(FILE_TEST2))
print(main(FILE))
