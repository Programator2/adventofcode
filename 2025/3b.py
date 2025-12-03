from aoc import *


def main(infi: str):
    inp = lines_stripped(infi)
    s = 0
    for a in inp:
        num = 0
        nums = [int(x) for x in a]
        #  looking at these numbers  11 numbers have to stay here
        # |.........................|xxxxxxxxx
        rang = len(nums) - 12 + 1
        for i in range(12):
            # Start looking from the left for the biggest digit in the
            # specified region
            maximum = max(nums[:rang])
            ind = nums.index(maximum)
            # Once found, delete everything until the found digit
            # Shorten the range if necessary
            del nums[: ind + 1]
            rang -= ind
            num = num * 10 + maximum
        s += num
    return s


DAY = 3
FILE_TEST = f"{DAY}_test.txt"
# FILE_TEST = f"{DAY}_testb.txt"
FILE_EXP = f"{DAY}_exp.txt"
FILE = f"{DAY}.txt"
# test_and_submit(main, FILE_TEST, FILE_EXP, FILE, DAY)
# print(main(FILE_TEST))
print(main(FILE))
