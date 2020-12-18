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


def search_closing_para(tokens, position):
    n_para = 1
    for j in range(position+1, len(tokens)):
        if tokens[j] == '(':
            n_para += 1
        elif tokens[j] == ')':
            n_para -= 1
            if n_para == 0:
                return j


def compute_with_operation(op1, op, op2):
    if op == '*':
        return op1 * op2
    elif op == '+':
        return op1 + op2


def compute2(tokens):
    i = 0
    while i + 1 < len(tokens):
        if i == 0 and tokens[i] == '(':
            j = search_closing_para(tokens, i)

            op1 = compute2(tokens[1:j])
            op = tokens[j+1]

            if tokens[j+2] == '(':
                k = search_closing_para(tokens, j+2)
                op2 = compute2(tokens[j+3:k])
                i = k + 1
            else:
                op2 = tokens[j+2]
                i = j + 3

            op1 = compute_with_operation(op1, op, op2)
            continue
        if i == 0:
            op1 = tokens[i]
            op = tokens[i+1]
            if tokens[i+2] == '(':
                j = search_closing_para(tokens, i+2)
                op2 = compute2(tokens[i+3:j])
                i = j + 1
            else:
                op2 = tokens[i+2]
                i = i + 3
            op1 = compute_with_operation(op1, op, op2)
        else:
            op = tokens[i]
            if tokens[i+1] == '(':
                j = search_closing_para(tokens, i+1)
                op2 = compute2(tokens[i+2:j])
                i = j + 1
            else:
                op2 = tokens[i+1]
                i = i + 2
            op1 = compute_with_operation(op1, op, op2)
    return op1


def main():
    inp = lines(FILE)
    p = 0
    out = 0
    for l in inp:
        l = l.replace(' ', '')
        t = tokenize(l)
        out += compute2(t)
    print(out)
    return
    input()
    print("submitting")
    submit(out)


main()
