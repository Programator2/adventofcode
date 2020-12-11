from collections import defaultdict, namedtuple
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

pprint(d)

second = 0
workers = []
Worker = namedtuple("Worker", ("min_left", "letter"))
for i in range(5):
    workers.append({"min_left": 0, "letter": None})

while True:
    # lower counters of workers
    for w in workers:
        if w["letter"] is not None:
            w["min_left"] -= 1

    # record finished workers and prepare them for work
    for w in workers:
        if w["min_left"] == 0 and w["letter"] is not None:
            sequence.append(w["letter"])
            # since one letter was finished, we can remove it from requirements
            for antacedents in d.values():
                antacedents.discard(w["letter"])
            w["letter"] = None

    if not d and not tuple(w for w in workers if w["letter"] is not None):
        print(second)
        break

    # find items without requirements:
    no_req = [(cons, req) for cons, req in d.items() if not req]
    # sort them alphabetically
    no_req.sort(key=lambda x: x[0])

    # Add them to free workers
    for l, *_ in no_req:
        for w in workers:
            if w["letter"] is None:
                w["letter"] = l
                w["min_left"] = 60 + ord(l) - ord("A") + 1
                # letter is assigned to someone, we delete it from the list
                del d[w["letter"]]
                break

    # print(f'{second}   {workers[0]}   {workers[1]}   {workers[2]}   {workers[3]}   {workers[4]}')

    second += 1

print("".join(sequence))
