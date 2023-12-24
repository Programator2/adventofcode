from aoc import *
from sympy import symbols
from sympy.solvers.polysys import solve_poly_system


# Geometrical representation: H is a set of lines (more precisely rays, but this
# doesn't matter in this task) that represent the trajectories of hailstones. We
# have to find line l (trajectory of our stone) that intersects all lines in H.
#
# This can be represented analytically as a system of equations (they aren't
# linear as there is a multiplication of two unknowns).
#
# As line is defined by two points, if we find a unique line that intersects
# three lines from H, it should also intersect all other lines (considering the
# input is correct).
#
# Many people on r/adventofcode used Z3. I wanted to use a Python solution and
# since I used sympy for part one, this post was a good inspiration for me:
# https://www.reddit.com/r/adventofcode/comments/18pnycy/comment/kepmry2/?utm_source=share&utm_medium=web2x&context=3
def main(input_file: str):
    inp = lines(input_file)
    points = []
    system = []
    x, y, z, vx, vy, vz = symbols('x y z vx vy vz')
    ts = []
    # Three lines (points) is enough. It will define the throw line for all
    # other hailstones.
    for i, l in enumerate(inp[:3]):
        left, right = l.split(' @ ')
        left = tuple(int(j) for j in left.split(', '))
        right = tuple(int(j) for j in right.split(', '))
        points.append((left, right))
        t = symbols(f't{i}')
        ts.append(t)
        system.append(x + vx * t - left[0] - right[0] * t)
        system.append(y + vy * t - left[1] - right[1] * t)
        system.append(z + vz * t - left[2] - right[2] * t)

    return sum(solve_poly_system(system, x, y, z, vx, vy, vz, *ts)[0][:3])


DAY = 24
FILE_TEST = f"{DAY}_test.txt"
FILE_EXP = f"{DAY}_expa.txt"
FILE = f"{DAY}.txt"
# test_and_submit(main, FILE_TEST, FILE_EXP, FILE, DAY)
print(main(FILE_TEST))
print(main(FILE))
