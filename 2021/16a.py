from aoc import *
from pprint import pprint as pp
from more_itertools import take, peekable


def mybin(num: int):
    b = bin(num)[2:]
    b = '0' * ((4 - len(b) % 4) % 4) + b
    return b


versions = 0
def read_packet(i, read, padding=True, maxnum=0):
    packets = []
    global versions
    while True:
        try:
            version = int(''.join(take(3, i)), 2)
        except ValueError:
            return read, packets
        versions += version
        read += 3
        try:
            pid = int(''.join(take(3, i)), 2)
        except ValueError:
            return read, packets
        print(f'{version=} {pid=}')
        read += 3
        out = version
        if pid == 4:
            num = ''
            keep = True
            while keep:
                keep = int(''.join(take(1, i)), 2)
                part = ''.join(take(4, i))
                print(f'{keep=} {part=}')
                read += 5
                num += part
            print(f'literal cislo {int(num, 2)}, verzia {version}')
            packets.append(int(num, 2))
            if maxnum and len(packets) == maxnum:
                return read, packets
        else:
            try:
                lid = int(''.join(take(1, i)), 2)
            except ValueError:
                return read, packets
            print(f'{lid=}')
            read += 1
            if not lid:
                try:
                    length = int(''.join(take(15, i)), 2)
                except ValueError:
                    return read, packets
                read += 15
                subpackets_iter = peekable(''.join(take(length, i)))
                print(f'operator typu dlzka, verzia {version}')
                read, subpackets = read_packet(subpackets_iter, read, False)
                packets.append((pid, subpackets))
                if maxnum and len(packets) == maxnum:
                    return read, packets
            else: # lid == 1
                number = int(''.join(take(11, i)), 2)
                read += 11
                print(f'operator typu pocet, verzia {version}')
                read, subpackets = read_packet(i, read, False, number)
                packets.append((pid, subpackets))
                if maxnum and len(packets) == maxnum:
                    return read, packets


def main(input_file: str):
    inp = filerstrip(input_file)
    b = mybin(int(inp, 16))
    print(b)
    i = peekable(b)
    packets = read_packet(i, 0)
    pp(packets)
    return versions


DAY = 16
FILE_TEST = f"{DAY}_test.txt"
FILE_EXP = f"{DAY}_exp.txt"
FILE = f"{DAY}.txt"
# test_and_submit(main, FILE_TEST, FILE_EXP, FILE)
# print(main(FILE_TEST))
print(main(FILE))
