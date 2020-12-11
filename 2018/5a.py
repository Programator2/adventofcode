def polymerize(polymer):
    l = polymer[:]
    i = 1
    changed = False
    while True:
        first = l[i - 1]
        second = l[i]
        if first == second.swapcase():
            del l[i - 1]
            del l[i - 1]
            changed = True
        else:
            i += 1
        if i >= len(l):
            # We went through whole string
            if changed:
                # If we have changed something, we go over it again
                changed = False
                i = 1
            else:
                # If nothing changed, the string is finished
                break
    return len(l)


with open("5.txt") as f:
    l = f.read()
    l = tuple(l.rstrip())

polymers = tuple(
    list(filter(lambda x: x not in c, l)) for c in ("aA", "bB", "cC", "dD")
)

print(min(map(polymerize, polymers)))
