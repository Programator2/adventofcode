from aoc import *
import re
from shapely.geometry import Polygon


D = {'U': (-1, 0), 'D': (1, 0), 'L': (0, -1), 'R': (0, 1)}
HEX_TO_D = ['R', 'D', 'L', 'U']


# Inspiration from https://www.reddit.com/r/adventofcode/comments/18l0qtr/comment/kduu02z/?utm_source=share&utm_medium=web2x&context=3
# Tip for the shapely library: https://stackoverflow.com/a/24468019/4739767
def main(input_file: str):
    inp = lines(input_file)
    start = (0, 0)
    edgelen = 0
    points = []
    for l in inp:
        m = re.match(r'^(.) (\d+) \(#(.+)\)$', l)
        le = int(m[3][:5], base=16)
        di = HEX_TO_D[int(m[3][5])]
        edgelen += le
        dx, dy = D[di]
        start = (start[0] + dx * le, start[1] + dy * le)
        points.append(start)
    polygon = Polygon(points)
    # Uses Pick's theorem: https://en.wikipedia.org/wiki/Pick's_theorem
    return int(polygon.area - edgelen / 2 + 1) + edgelen


DAY = 18
FILE_TEST = f"{DAY}_test.txt"
FILE_EXP = f"{DAY}_expb.txt"
FILE = f"{DAY}.txt"
# test_and_submit(main, FILE_TEST, FILE_EXP, FILE, DAY)
print(main(FILE_TEST))
print(main(FILE))
