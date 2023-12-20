from aoc import *
import math
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

    i = 0
    gt_cycle, xd_cycle, ms_cycle, zt_cycle = 0, 0, 0, 0
    while True:
        # receiver, pulse, sender
        q = deque([('broadcaster', 0, 'button')])
        i += 1
        while q:
            receiver, pulse, sender = q.popleft()
            try:
                fn, outputs = op[receiver][pulse]
            except KeyError:
                continue
            new_pulse = fn(receiver, sender, pulse)
            if new_pulse is not None:
                for o in outputs:
                    q.append((o, new_pulse, receiver))

            # See below for explanation
            if not gt_cycle and all(
                state[x]
                for x in ('jr', 'qh', 'hv', 'lt', 'bv', 'nz', 'bx', 'kt')
            ):
                gt_cycle = i
            if not xd_cycle and all(
                state[x]
                for x in (
                    'mv',
                    'dp',
                    'zq',
                    'mf',
                    'xl',
                    'bj',
                    'kx',
                )
            ):
                xd_cycle = i
            if not ms_cycle and all(
                state[x]
                for x in (
                    'zm',
                    'xj',
                    'ts',
                    'bs',
                    'vt',
                    'fr',
                    'hz',
                )
            ):
                ms_cycle = i
            if not zt_cycle and all(
                state[x]
                for x in (
                    'mq',
                    'hr',
                    'tz',
                    'cb',
                    'xp',
                    'sj',
                    'vl',
                    'pd',
                    'hg',
                    'jf',
                )
            ):
                zt_cycle = i
            if all((gt_cycle, xd_cycle, ms_cycle, zt_cycle)):
                return math.lcm(gt_cycle, xd_cycle, ms_cycle, zt_cycle)


# I have found the following dependencies in the input:
#
#  rx <-LOW-- bb
# &bb <-HIGH- ct, kp, ks, xc
# ---------------------
# &ct <-LOW-- &gt <-HIGH- jr, qh, hv, lt, bv, nz, bx, kt
# &kp <-LOW-- &xd <-HIGH- mv, dp, zq, mf, xl, bj, kx
# &ks <-LOW-- &ms <-HIGH- zm, xj, ts, bs, vt, fs, hz
# &xc <-LOW-- &zt <-HIGH- mq, hr, tz, cb, xp, sj, vl, pd, hg, jf
#
# Modules on the right side in the last four rows are flip-flops. Looking at the
# dependencies and pulses needed (rx requires low pulse; to achieve this, bb
# requires high pulse and so on...), if state of all flip flops in one group is
# high, that means a high pulse was sent to the next module in the dependency
# graph.
#
# The current number of button presses when a high pulse was sent from all
# modules in a flip-flop group determines the cycle length of a particular
# group. Computing LCM of the cycle lengths determines the number of button
# presses needed to send a low pulse to the rx module.


DAY = 20
FILE = f"{DAY}.txt"
print(main(FILE))
