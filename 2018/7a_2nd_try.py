from collections import defaultdict
from pprint import pprint

# d = {consequent: set of prerequisites}
d = defaultdict(set)

with open("7.txt") as f:
    for l in f:
        antacedent = l[5]
        consequent = l[36]
        d[consequent].add(antacedent)
        if antacedent not in d:
            d[antacedent] = set()

sequence = []

# pprint(d)

while d:
    # find items without requirements:
    no_req = [(cons, req) for cons, req in d.items() if not req]
    # sort them alphabetically
    no_req.sort(key=lambda x: x[0])
    # add the FIRST one to the sequence! (because other ones may meanwhile
    # become available
    sequence.append(no_req[0][0])
    # pprint(sequence)
    # remove it from the d
    del d[no_req[0][0]]
    # remove them from values in d:
    for antacedents in d.values():
        antacedents.discard(no_req[0][0])

print("".join(sequence))
