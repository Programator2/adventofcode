from aoc import *
from more_itertools import take, peekable
from functools import reduce


def mybin(num: int):
    b = bin(num)[2:]
    b = '0' * ((4 - len(b) % 4) % 4) + b
    return b


def compute(pid: int, param):
    if pid == 0:
        return sum(param)
    elif pid == 1:
        return reduce(operator.mul, param)
    elif pid == 2:
        return min(param)
    elif pid == 3:
        return max(param)
    elif pid == 5:
        if param[0] > param[1]:
            return 1
        else:
            return 0
    elif pid == 6:
        if param[0] < param[1]:
            return 1
        else:
            return 0
    elif pid == 7:
        if param[0] == param[1]:
            return 1
        else:
            return 0


versions = 0
def read_packet(i, first=True, maxnum=0):
    packets = []
    global versions
    while i.peek(False):
        versions += int(''.join(take(3, i)), 2)
        pid = int(''.join(take(3, i)), 2)
        if pid == 4:
            num = ''
            keep = True
            while keep:
                keep = int(''.join(take(1, i)), 2)
                part = ''.join(take(4, i))
                num += part
            packets.append(int(num, 2))
            if maxnum and len(packets) == maxnum:
                return packets
        else:
            lid = int(''.join(take(1, i)), 2)
            if not lid:
                length = int(''.join(take(15, i)), 2)
                subpackets_iter = peekable(''.join(take(length, i)))
                subpackets = read_packet(subpackets_iter, False)
                packets.append(compute(pid, subpackets))
                if maxnum and len(packets) == maxnum or first:
                    return packets
            else: # lid == 1
                number = int(''.join(take(11, i)), 2)
                subpackets = read_packet(i, False, number)
                packets.append(compute(pid, subpackets))
                if maxnum and len(packets) == maxnum or first:
                    return packets
    return packets


def main(input_file: str):
    inp = filerstrip(input_file)
    b = mybin(int(inp, 16))
    i = peekable(b)
    packets = read_packet(i, True)
    return packets[0]


DAY = 16
FILE_TEST = f"{DAY}_test.txt"
FILE_EXP = f"{DAY}_exp.txt"
FILE = f"{DAY}.txt"
# test_and_submit(main, FILE_TEST, FILE_EXP, FILE)
# print(main(FILE_TEST))
print(main(FILE))
