#!/usr/bin/env pypy
# Ideally, you should run this with pypy
from itertools import product, chain


def cycle(z, w, p1, p2, p3):
    """One cycle of the MONAD validator.

    The cycle goes like this:
    if z % 26 + p2 = w:
        nz := z // p1
    else:
        nz := (z // p1) * 26 + w + p3

    return: new value of z"""
    x = 0
    x = z % 26
    z = z // p1
    x += p2
    x = int(x != w)

    y = 25
    y = y * x + 1
    z *= y

    y = w
    y += p3
    y *= x
    return z + y


def revcycle(nz, w, p1, p2, p3):
    """Opposite of cycle.

    Return possible z values for nz result."""
    # for the first branch
    solutions = (z for z in range(nz*p1, nz * p1 + p1))
    solutions = (z for z in solutions if z % 26 + p2 == w)

    # for the second branch
    solutions2 = (z for z in range(((-w-p3+nz)//26) * p1, ((-w-p3+nz)//26) * p1 + p1) if (-w-p3+nz)%26 == 0)
    solutions2 = (z for z in solutions2 if z % 26 + p2 != w)

    return chain(solutions, solutions2)


def revcycle_rec(nz_iter: set, w_iter: tuple, p1_iter: tuple, p2_iter: tuple, p3_iter: tuple) -> set:
    """Recursive search.

    nz: iterable with solutions"""
    if not w_iter:
        return nz_iter
    ret = set()
    for nz in nz_iter:
        solutions = revcycle(nz, w_iter[-1], p1_iter[-1], p2_iter[-1], p3_iter[-1])
        ret.update(revcycle_rec(set(solutions), w_iter[:-1], p1_iter[:-1], p2_iter[:-1], p3_iter[:-1]))
    return ret


# This should really be in standard library
def minmax(it):
    n = next(it)
    mmin = n
    mmax = n
    for i in it:
        mmin = min(i, mmin)
        mmax = max(i, mmax)
    return mmin, mmax


def main():
    params = (
        (1,   1,  1,  1, 26,  1,  1,  26,  26,  26, 26,  1, 26,  26),
        (10, 10, 12, 11,  0, 15, 13, -12, -15, -15, -4, 10, -5, -12),
        (12, 10,  8,  4,  3, 10,  6,  13,   8,   1,  7,  6,  9,   9)
    )

    # Search for solutions from the big side, 8 digits
    p = product((9,8,7,6,5,4,3,2,1), repeat=8)
    from_big = set()
    for w_ in p:
        z = 0
        for w, p1, p2, p3 in zip(w_, *params):
            z = cycle(z, w, p1, p2, p3)
        from_big.add(z)
    # print('big:', len(from_big))

    # Search for solution from the little side, 6 digits
    p = product((9,8,7,6,5,4,3,2,1), repeat=6)
    from_little = set()
    for w_ in p:
        solutions = revcycle_rec({0}, w_, params[0][8:], params[1][8:], params[2][8:])
        from_little.update(solutions)
    # print('little:', len(from_little))

    intersection = from_big & from_little
    # print(len(intersection))

    # We have met in the middle and have all solutions. If we had stored the
    # solutions, we could retrieve the result right away, at the cost of memory
    # usage. But now we have to compute it again and store just the good
    # solutions.
    solutions_big = []
    p = product((9,8,7,6,5,4,3,2,1), repeat=8)
    for w_ in p:
        z = 0
        for w, p1, p2, p3 in zip(w_, *params):
            z = cycle(z, w, p1, p2, p3)
        if z in intersection:
            solutions_big.append(w_)

    solutions_little = []
    p = product((9,8,7,6,5,4,3,2,1), repeat=6)
    for w_ in p:
        solutions = revcycle_rec({0}, w_, params[0][8:], params[1][8:], params[2][8:])
        if solutions & intersection:
            solutions_little.append(w_)

    minimum, maximum = minmax(sum(y * 10**i for i, y in enumerate(reversed(list(chain.from_iterable(x)))))
                              for x in product(solutions_big, solutions_little))

    print(f'min={minimum} max={maximum}')


main()
