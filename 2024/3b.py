from aoc import *
import re


def search(inp):
    m = re.findall(r'mul\((\d{1,3}),(\d{1,3})\)', inp)
    return sum(int(a) * int(b) for a, b in m)


def main(infi: str):
    inp = filerstrip(infi)
    do = "do()"
    dont = "don't()"
    d = inp.split(dont)
    s = 0
    s += search(d[0])
    for ss in d[1:]:
        dd = ss.split(do)
        for sss in dd[1:]:
            s += search(sss)
    return s


DAY = 3
FILE_TEST = f"{DAY}_testa.txt"
FILE_TEST = f"{DAY}_testb.txt"
FILE_EXP = f"{DAY}_exp.txt"
FILE = f"{DAY}.txt"
# test_and_submit(main, FILE_TEST, FILE_EXP, FILE, DAY)
# print(main(FILE_TEST))
print(main(FILE))
