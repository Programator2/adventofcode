from aoc import *
import re
from more_itertools import flatten


def main(infi: str):
    rul = []
    for r in filerstrip(infi).split('\n\n')[1].split('\n'):
        match = re.fullmatch(r'^(.*?) (.*?) (.*?) -> (.*?)$', r)
        rul.append((match[1], match[2], match[3], match[4]))
    carry_inputs = set(
        flatten([(x, y) for x, oper, y, d in rul if oper == 'OR'])
    )
    ands = {d for x, oper, y, d in rul if oper == 'AND'}
    # Here is my notation of an adder:
    # x XOR y = a   c XOR a = s
    # x AND y = d   a AND c = b   d OR b = c_out
    # By manually inspecting XORs of input values (x.. and y.., grep 'XOR .* ->
    # z' 24.txt | sort -k 5), we can see that z05, z09 and z30 are missing. By
    # inspecting other XOR operations (those that don't output z.., grep 'XOR .*
    # -> [^z]' 24.txt | sort), we can see that nbf, hdt and gbf are outputs
    # XORed fom inputs other than x.. and y...
    #
    # The last two mismatched outputs needed are computed here. We take output
    # from AND operations and compare them with inputs of ORs. Those that don't
    # match are misplaced. jfb is a special case since that one is used to
    # compute carry for the LSB and isn't merged with previous carry, so it's
    # correct.
    return ','.join(
        sorted(list((ands ^ carry_inputs) - {'jfb'}) + ['z05', 'hdt'])
    )


DAY = 24
FILE_TEST = f"{DAY}_testa.txt"
# FILE_TEST = f"{DAY}_testb.txt"
FILE_EXP = f"{DAY}_exp.txt"
FILE = f"{DAY}.txt"
# test_and_submit(main, FILE_TEST, FILE_EXP, FILE, DAY)
# print(main(FILE_TEST))
print(main(FILE))
