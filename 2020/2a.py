import re


FILE = '2_test.txt'
FILE = '2.txt'

def main():
    inp = []
    valid = 0
    invalid = 0
    with open(FILE) as f:
        lines = f.readlines()
        for l in lines:
            x = re.search('^(\d*)-(\d*) (.): (.*)$', l)
            inp.append((int(x[1]), int(x[2]), x[3], x[4]))
            vyskyt = 0
            for c in x[4]:
                if c == x[3]:
                    vyskyt +=1
            if int(x[1]) <= vyskyt <= int(x[2]):
                valid += 1
            else:
                invalid += 1
    print(valid)


main()
