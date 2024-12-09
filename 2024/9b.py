from aoc import *
from collections.abc import Iterable


class File:
    def __init__(self, id, size):
        self.id = id
        self.size = size

    def __repr__(self):
        return f'File({self.id}, {self.size})'

    def __eq__(self, o):
        return self.id == o.id and self.size == o.size


class Space:
    def __init__(self, size):
        self.size = size

    def __repr__(self):
        return f'Space({self.size})'


def print_disk(disk):
    for f in disk:
        match f:
            case File():
                print(str(f.id) * f.size, end='')
            case Space():
                print('.' * f.size, end='')
    print()


def index_from_end(it: Iterable, el):
    for i, item in reversed(list(enumerate(it))):
        if type(item) is not type(el):
            continue
        if item == el:
            return i
    return None


def main(infi: str):
    inp = filerstrip(infi)
    inp = list(map(int, inp))
    disk = []                   # whole disk
    files = []                  # just the files

    # Fill the disk
    for i, f in enumerate(inp):
        if i % 2 == 0:
            file = File(i // 2, f)
            disk.append(file)
            files.append(file)
        else:
            disk.append(Space(f))

    for f in reversed(files):
        for i, space in enumerate(disk):
            if type(space) is File and space.id == f.id:
                break
            if type(space) is not Space:
                continue
            if f.size <= space.size:
                space.size -= f.size
                disk.insert(i, File(f.id, f.size))
                # remove the file from the end, first find it
                fi = index_from_end(disk, f)
                # insert a space instead of it
                disk.insert(fi, Space(f.size))
                # and finally remove the original file on the right side
                disk.pop(fi + 1)
                break
            if f.size == space.size:
                break
    checksum = 0
    pos = 0
    for f in disk:
        match f:
            case File():
                for _ in range(f.size):
                    checksum += f.id * pos
                    pos += 1
                    # print(f.id, end='')
            case Space():
                pos += f.size
                # print('.' * f.size, end='')
    # print()
    return checksum

DAY = 9
FILE_TEST = f"{DAY}_testa.txt"
# FILE_TEST = f"{DAY}_testb.txt"
FILE_EXP = f"{DAY}_exp.txt"
FILE = f"{DAY}.txt"
# test_and_submit(main, FILE_TEST, FILE_EXP, FILE, DAY)
# print(main(FILE_TEST))
print(main(FILE))
