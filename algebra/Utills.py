from functools import reduce

_N = 2 ** 63


def list_hash(l):
    return reduce(lambda x, y: (257 * x + y) % _N, map(hash, l))


def isPrime(x, limit=1_000):
    if x < 0:
        raise Exception()
    if x < 2:
        return False
    if x == 2:
        return True
    if x % 2 == 0:
        return False

    div = 3
    div_sq = 9

    while div_sq <= x and div < limit:
        if x % div == 0:
            return False
        div_sq = div_sq + 4 * div + 4
        div = div + 2

    return True


def distPrimes(x):
    acc = set()
    if x < 0:
        raise Exception()
    if x == 1:
        return acc
    while x % 2 == 0:
        acc.add(2)
        x = x // 2

    div = 3
    div_sq = 9

    while div_sq <= x:
        while x % div == 0:
            acc.add(div)
            x = x // div

        div_sq = div_sq + 4 * div + 4
        div = div + 2

    if x != 1:
        acc.add(x)

    return acc
