from aocd import submit
from aoc import *
import re


FILE = "18_test.txt"
FILE = "18.txt"


def tokenize(s):
    tokens = []
    i = 0
    while i < len(s):
        m = re.search(r'^(\d+)', s[i:])
        if m is not None:
            tokens.append(int(m[1]))
            i += m.end(1)
        elif s[i] in ['+', '*', '(', ')']:
            tokens.append(s[i])
            i += 1
        else:
            i += 1
    return tokens


def compute3(tokens):
    new_tokens = tokens[:]
    # get rid of parantheses
    para_positions = []
    i = 0
    while i < len(new_tokens):
        if new_tokens[i] == '(':
            para_positions.append(i)
        elif new_tokens[i] == ')':
            start = para_positions.pop()
            new_tokens[start:i+1] = [compute3(new_tokens[start+1:i])]
            i = start + 1
            continue
        i += 1
    # add operation
    i = 0
    while i < len(new_tokens):
        if new_tokens[i] == '+':
            new_tokens[i-1:i+2] = [new_tokens[i-1] + new_tokens[i+1]]
        else:
            i += 1
    # multiply operation
    i = 0
    while i < len(new_tokens):
        if new_tokens[i] == '*':
            new_tokens[i-1:i+2] = [new_tokens[i-1] * new_tokens[i+1]]
        else:
            i += 1
    return new_tokens[0]


def main():
    inp = lines(FILE)
    p = 0
    out = 0
    for l in inp:
        l = l.replace(' ', '')
        t = tokenize(l)
        out += compute3(t)
    print(out)
    return
    input()
    print("submitting")
    submit(out)


main()
