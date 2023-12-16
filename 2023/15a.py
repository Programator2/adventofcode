from aoc import *


def main(input_file: str):
    inp = filerstrip(input_file)
    inp = inp.split(',')
    full = 0
    for l in inp:
        val = 0
        for i in l:
            if i in ['\n']:
                continue
            val = ((val + ord(i)) * 17) % 256
        full += val
    return full


DAY = 15
FILE_TEST = f"{DAY}_test.txt"
FILE_EXP = f"{DAY}_expa.txt"
FILE = f"{DAY}.txt"
# test_and_submit(main, FILE_TEST, FILE_EXP, FILE)
print(main(FILE_TEST))
print(main(FILE))
