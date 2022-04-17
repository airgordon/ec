import operator
from functools import reduce
from Utills import distPrimes


def ft2(x, a=None):
    N = len(x)
    if N == 0:
        return []
    if a == None:
        a = x[0].field.G

    return [reduce(operator.add, [x[i] * a ** (k * i) for i in range(0, N)]) for k in range(0, N)]


def ft(x, a=None, K=None):
    N = len(x)
    one = x[0].field.one
    if K == None:
        K = N
    if a == None:
        a = x[0].field.G

    divisors = []
    multipliers = []
    p_idx = 0
    primes = list(distPrimes(N))
    while N != 1:
        p = primes[p_idx]
        if N % p != 0:
            p_idx = p_idx + 1
        else:
            divisors.append(p)
            N = N // p
            multiplier_d = []
            A_j = one
            for j in range(0, p):
                multiplier_d_j = []
                A_j_k = one
                for k in range(0, K):
                    multiplier_d_j.append(A_j_k)
                    A_j_k = A_j_k * A_j
                multiplier_d.append(multiplier_d_j)
                A_j = A_j * a

            multipliers.append(multiplier_d)
            a = A_j
    return _ftRec(x, divisors, multipliers, 0, K)


def _ftRec(x, divisors, multipliers, depth, K):
    N = len(x)
    if N == 1:
        return [x[0] for _ in range(0, K)]

    P = divisors[depth]
    sub_x = [[] for _ in range(0, P)]
    j = 0
    for i in range(0, N):
        sub_x[j].append(x[i])
        j = j + 1
        if j == P:
            j = 0

    results = [[] for _ in range(0, K)]
    for j in range(0, P):
        r = _ftRec(sub_x[j], divisors, multipliers, depth + 1, K)
        for k in range(0, K):
            A = multipliers[depth][j][k]
            results[k].append(A * r[k])
    return list(map(lambda l: reduce(operator.add, l), results))
