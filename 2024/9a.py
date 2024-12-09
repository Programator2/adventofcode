from aoc import *


def main(infi: str):
    inp = filerstrip(infi)
    inp = list(map(int, inp))
    blocks = [x for i, x in enumerate(inp) if i % 2 == 0]
    space = [x for i, x in enumerate(inp) if i % 2 == 1]

    # current position in blocks and space from the left
    posstart = 0
    # position from the right, used to get a file to move
    posend = len(blocks) - 1
    # position in the disk, this is used to count checksum
    posreal = 0
    # space left until next file
    spaceleft = space[posstart]
    # how many bytes are left from the file to move
    n_to_write = blocks[posend]
    checksum = 0
    while posend != posstart:
        # count file from left
        for i in range(blocks[posstart]):
            checksum += posstart * posreal
            posreal += 1
        # move as many files from the end to this space as possible
        while True:
            # we can write whole file or as many bytes as possible by filling
            # the space
            howmuch = min(n_to_write, spaceleft)
            for i in range(howmuch):
                checksum += posend * posreal
                posreal += 1
            n_to_write -= howmuch
            spaceleft -= howmuch
            if n_to_write == 0:
                # move to other file to move from right
                posend -= 1
                n_to_write = blocks[posend]
            if spaceleft == 0:
                # move to next file from the left that's on drive
                posstart += 1
                spaceleft = space[posstart]
                break
    # Is there anything left to write?
    if n_to_write:
        for i in range(n_to_write):
            checksum += posend * posreal
            posreal += 1
    return checksum


DAY = 9
FILE_TEST = f"{DAY}_testa.txt"
# FILE_TEST = f"{DAY}_testb.txt"
FILE_EXP = f"{DAY}_exp.txt"
FILE = f"{DAY}.txt"
# test_and_submit(main, FILE_TEST, FILE_EXP, FILE, DAY)
# print(main(FILE_TEST))
print(main(FILE))
