from collections import defaultdict


with open('2.txt') as f:
    lines = f.readlines()
    lines = map(lambda x: x.rstrip(), lines)
    tuples = 0
    triples = 0
    for x in lines:
        d = defaultdict(int)
        for c in x:
            d[c] += 1
        v = d.values()
        # Is there a tuple?
        if 2 in v:
            tuples += 1
        # Is there a triple?
        if 3 in v:
            triples += 1
    print(tuples * triples)
