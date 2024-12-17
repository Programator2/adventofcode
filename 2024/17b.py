from aoc import *


def solve(ae, out):
    if not out:
        return ae
    # For the first iteration (lowest search depth), the range should be (1, 8).
    # But it doesn't matter, since the result is found anyway.
    for rem in range(0, 8):
        astart = ae * 8 + rem
        b1 = rem
        b2 = b1 ^ 5
        c1 = astart // 2**b2
        b3 = b2 ^ c1
        b4 = b3 ^ 6
        oute = b4 % 8
        if oute == out[0]:
            if (ret := solve(astart, out[1:])) is not None:
                return ret


def main(infi: str):
    out = list(
        reversed(
            list(
                map(
                    int,
                    filerstrip(infi)
                    .split('\n\n')[1][len('Program: ') :]
                    .split(','),
                )
            )
        )
    )

    return solve(0, out)


DAY = 17
FILE_TEST = f"{DAY}_testa.txt"
# FILE_TEST = f"{DAY}_testb.txt"
FILE_EXP = f"{DAY}_exp.txt"
FILE = f"{DAY}.txt"
# test_and_submit(main, FILE_TEST, FILE_EXP, FILE, DAY)
# print(main(FILE_TEST))
print(main(FILE))
