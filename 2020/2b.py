import re


FILE = "2_test.txt"
FILE = "2.txt"


def main():
    inp = []
    valid = 0
    invalid = 0
    with open(FILE) as f:
        lines = f.readlines()
        for l in lines:
            x = re.search(r"^(\d*)-(\d*) (.): (.*)$", l)
            inp.append((int(x[1]), int(x[2]), x[3], x[4]))
            low = int(x[1]) - 1
            high = int(x[2]) - 1
            c = x[4]
            if (c[low] == x[3] and c[high] != x[3]) or (
                c[low] != x[3] and c[high] == x[3]
            ):
                valid += 1
            else:
                invalid += 1
    print(valid)


main()
