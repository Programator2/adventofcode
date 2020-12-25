from math import ceil, sqrt


# Baby-Step-Giant-Step implementation by 0xTowel
# https://gist.github.com/0xTowel/b4e7233fc86d8bb49698e4f1318a5a73
def bsgs(g, h, p):
    '''
    Solve for x in h = g^x mod p given a prime p.
    If p is not prime, you shouldn't use BSGS anyway.
    '''
    N = ceil(sqrt(p - 1))  # phi(p) is p-1 if p is prime

    # Store hashmap of g^{1...m} (mod p). Baby step.
    tbl = {pow(g, i, p): i for i in range(N)}

    # Precompute via Fermat's Little Theorem
    c = pow(g, N * (p - 2), p)

    # Search for an equivalence in the table. Giant step.
    for j in range(N):
        y = (h * pow(c, j, p)) % p
        if y in tbl:
            return j * N + tbl[y]

    # Solution not found
    return None


def main():
    mod = 20201227
    card_pub = 3418282
    door_pub = 8719412

    card_loop = bsgs(7, card_pub, mod)
    door_loop = bsgs(7, door_pub, mod)
    print(card_loop)
    print(door_loop)

    # Check if the computation was correct
    print(pow(7, card_loop, mod))
    print(pow(7, door_loop, mod))

    # This is the answer
    print(pow(door_pub, card_loop, mod))
    print(pow(card_pub, door_loop, mod))


main()
