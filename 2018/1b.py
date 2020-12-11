with open('1.txt') as f:
    lines = f.readlines()
    lines = map(lambda x: int(x.rstrip()), lines)
    lines = list(lines)
    total = 0
    total_set = {0}
    x = 0
    n_items = len(lines)
    while True:
        total += lines[x]
        if total in total_set:
            print(f'{total} was first reached twice')
            break
        total_set.add(total)
        x += 1
        if x == n_items:
            x = 0
    print(total)
