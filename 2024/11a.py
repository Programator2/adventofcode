from aoc import *


def main(infi: str):
    inp = load_ints_split(infi, ' ')
    for j in range(25):
        i = 0
        while i < len(inp):
            if inp[i] == 0:
                inp[i] = 1
            elif (lennum := len(strnum := str(inp[i]))) % 2 == 0:
                inp.insert(i, int(strnum[: lennum // 2]))
                i += 1
                inp[i] = int(strnum[lennum // 2 :])
            else:
                inp[i] *= 2024
            i += 1
    return len(inp)


DAY = 11
FILE_TEST = f"{DAY}_testa.txt"
# FILE_TEST = f"{DAY}_testb.txt"
FILE_EXP = f"{DAY}_exp.txt"
FILE = f"{DAY}.txt"
# test_and_submit(main, FILE_TEST, FILE_EXP, FILE, DAY)
# print(main(FILE_TEST))
print(main(FILE))
