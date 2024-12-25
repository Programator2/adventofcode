from aoc import *


def main(infi: str):
    inp = filerstrip(infi)
    inputs, rules = inp.split('\n\n')
    values = {}
    for i in inputs.split('\n'):
        name, val = i.split(': ')
        values[name] = bool(int(val))
    rul = []
    for r in rules.split('\n'):
        match = re.fullmatch(r'^(.*?) (.*?) (.*?) -> (.*?)$', r)
        rul.append((match[1], match[2], match[3], match[4]))
    changed = True
    while changed:
        changed = False
        for a, oper, b, c in rul:
            if c not in values and a in values and b in values:
                if oper == 'OR':
                    values[c] = values[a] or values[b]
                elif oper == 'AND':
                    values[c] = values[a] and values[b]
                elif oper == 'XOR':
                    values[c] = values[a] ^ values[b]
                changed = True
    aaa = sorted(
        ((k, c) for k, c in values.items() if k[0] == 'z'),
        key=lambda x: x[0],
        reverse=True,
    )
    number = int(''.join(str(int(c)) for _, c in aaa), base=2)
    return number


DAY = 24
FILE_TEST = f"{DAY}_testa.txt"
# FILE_TEST = f"{DAY}_testb.txt"
FILE_EXP = f"{DAY}_exp.txt"
FILE = f"{DAY}.txt"
# test_and_submit(main, FILE_TEST, FILE_EXP, FILE, DAY)
# print(main(FILE_TEST))
print(main(FILE))
