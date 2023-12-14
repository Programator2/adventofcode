from aoc import *


# Copied from 13a.py
def solution(input_file: str):
    inp = filerstrip(input_file).split('\n\n')
    suma = 0
    solutions = {}
    for iii, i in enumerate(inp):
        m = i.split('\n')
        #rows
        for ri in range(len(m)-1):
            original = ri
            opposite = ri + 1
            while ri >= 0 and opposite < len(m):
                if m[ri] != m[opposite]:
                    break
                ri -= 1
                opposite += 1
            else:
                suma += 100 * (original + 1)
                solutions[(iii, 'row')] = original
                break
        #cols
        i_trans = ['' for _ in m[0]]
        for r in m:
            for ii, c in enumerate(r):
                i_trans[ii] += c
        for ri in range(len(i_trans)-1):
            original = ri
            opposite = ri + 1
            while ri >= 0 and opposite < len(i_trans):
                if i_trans[ri] != i_trans[opposite]:
                    break
                ri -= 1
                opposite += 1
            else:
                solutions[(iii, 'col')] = original
                suma += original + 1
                break
    return solutions


def main(input_file: str):
    solutions = solution(input_file)
    inp = filerstrip(input_file).split('\n\n')
    suma = 0
    # print(inp)
    for iii, i in enumerate(inp):
        m = i.split('\n')
        found = False
        for new_ri, new_r in enumerate(m):
            for new_ci, new_c in enumerate(new_r):
                # Create a new matrix
                m_new = []
                for row_i, r in enumerate(m):
                    if row_i == new_ri:
                        m_new.append(m[row_i][:new_ci] +
                                     ('#' if m[row_i][new_ci] == '.' else '.') +
                                     (m[row_i][new_ci+1:] if new_ci + 1 < len(m[row_i]) else ''))
                    else:
                        m_new.append(m[row_i])
                found = False
                #rows
                for ri in range(len(m_new)-1):
                    original = ri
                    opposite = ri + 1
                    while ri >= 0 and opposite < len(m_new):
                        if m_new[ri] != m_new[opposite]:
                            break
                        ri -= 1
                        opposite += 1
                    else:
                        if solutions.get((iii, 'row'), None) == original:
                            continue
                        suma += 100 * (original + 1)
                        found = True
                        break
                if found:
                    break
                #cols
                i_trans = ['' for _ in m_new[0]]
                for r in m_new:
                    for ii, c in enumerate(r):
                        i_trans[ii] += c
                for ri in range(len(i_trans)-1):
                    original = ri
                    opposite = ri + 1
                    while ri >= 0 and opposite < len(i_trans):
                        if i_trans[ri] != i_trans[opposite]:
                            break
                        ri -= 1
                        opposite += 1
                    else:
                        if solutions.get((iii, 'col'), None) == original:
                            continue
                        suma += original + 1
                        found = True
                        break
                if found:
                    break
            if found:
                break
    return suma


DAY = 13
FILE_TEST = f"{DAY}_test.txt"
FILE_EXP = f"{DAY}_expb.txt"
FILE = f"{DAY}.txt"
# test_and_submit(main, FILE_TEST, FILE_EXP, FILE)
print(main(FILE_TEST))
print(main(FILE))
