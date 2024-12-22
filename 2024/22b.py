from aoc import *
from itertools import pairwise, starmap
from more_itertools import windowed


def main(infi: str):
    inp = load_ints(infi)
    all_prices = []
    all_diffs = []
    maps = []
    for n in inp:
        prices = []
        prices.append(n % 10)
        # sequence to number of bananas
        m = {}
        for i in range(2000):
            n = ((n * 64) ^ n) % 16777216
            n = ((n // 32) ^ n) % 16777216
            n = ((n * 2048) ^ n) % 16777216
            prices.append(n % 10)
        all_prices.append(prices)
        all_diffs.append(list(starmap(lambda x, y: y - x, pairwise(prices))))
        for seq, bananas in zip(windowed(all_diffs[-1], 4), prices[4:]):
            if seq not in m:
                m[seq] = bananas
        maps.append(m)
    possible_seq = set(key for m in maps for key in m)
    total_bananas = {
        seq: sum(m.get(seq, 0) for m in maps) for seq in possible_seq
    }
    return max(total_bananas.items(), key=lambda x: x[1])[1]


DAY = 22
FILE_TEST = f"{DAY}_testa.txt"
FILE_TEST = f"{DAY}_testb.txt"
FILE_EXP = f"{DAY}_exp.txt"
FILE = f"{DAY}.txt"
# test_and_submit(main, FILE_TEST, FILE_EXP, FILE, DAY)
# print(main(FILE_TEST))
print(main(FILE))
