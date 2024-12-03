from aoc import *
import re


# functional solution for mY
def main(inp):
    return sum(
        int(a) * int(b)
        for a, b in re.findall(
            r'mul\((\d+),(\d+)\)',
            re.sub(
                r"don't\(\).*?(do\(\)|$)", '', filerstrip(inp).replace('\n', '')
            ),
        )
    )


# submitted solution follows
def search(inp):
    m = re.findall(r'mul\((\d+),(\d+)\)', inp)
    return sum(int(a) * int(b) for a, b in m)


def orig(infi: str):
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
