# target area: x=29..73, y=-248..-194
x = (29, 73)
y = (-248, -194)
miny = min(y)
maxx = max(x)


def main():
    maxmax = 0
    for _velx in range(1, maxx + 1):
        for vely in range(1, 10000):
            velx = _velx
            posx = 0
            posy = 0
            maxy = posy
            while True:
                posx += velx
                posy += vely
                maxy = max(maxy, posy)
                if velx > 0:
                    velx -= 1
                # elif velx < 0:
                    # velx += 1
                vely -= 1
                if (x[0] <= posx <= x[1]) and (y[0] <= posy <= y[1]):
                    maxmax = max(maxmax, maxy)
                    break
                if velx == 0 and (posx < x[0] or posx > x[1]):
                    break
                if posy < miny or posx > maxx:
                    break
    return maxmax


print(main())
