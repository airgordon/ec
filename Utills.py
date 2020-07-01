from functools import reduce

N = 2 ** 63


def list_hash(l):
    return reduce(lambda x, y: (257 * x + y) % N, map(hash, l))
