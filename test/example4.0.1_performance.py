import time

from ec.ecs import *
from algebra.finField import finField
from algebra.poly2 import poly

from ec.pairings import Weil_no_rec, Weil_no_mul, Weil_no_rec_no_mul

ec = beginners4_0_1()

z = ec.field
p = poly(z)
u = p.u

f = finField(u * u + 1)

P = ec.of(z(2693), z(4312))

qx = u * 633 + 6145
qy = u * 7372 + 109

Q = ec.of(f.of(qx), f.of(qy))

R = P + Q
S = P + 2 * Q

r = 641


def assertTrue(ex):
    if not ex:
        raise Exception


def test(weil):

    ex1 = f.of(u * 6744 + 5677)
    ex2 = f.of(u * 3821 + 7025)
    ex3 = f.of(u * 248 + 5)
    ex4 = f.of(u * 2719 + 2731)

    assertTrue(weil(P, Q, R, S, r) == ex1)
    assertTrue(weil(403 * P, Q, R, S, r) == ex2)
    assertTrue(weil(P, Q, R, S, r) ** 403 == ex2)
    assertTrue(weil(P, 135 * Q, R, S, r) == ex3)
    assertTrue(weil(P, Q, R, S, r) ** 135 == ex3)
    assertTrue(weil(403 * P, 135 * Q, R, S, r) == ex4)
    assertTrue(weil(P, Q, R, S, r) ** (135 * 403) == ex4)


def no_rec_no_mul():
    test(Weil_no_rec_no_mul)


def no_mul():
    test(Weil_no_mul)


def comparePerf(prob1, prob2, N):
    t1 = 0
    t2 = 0
    t1_2 = 0
    t2_2 = 0

    for i in range(N):
        start = time.time()

        prob1()

        took = time.time() - start
        t1 += took
        t1_2 += took ** 2

        start = time.time()

        prob2()

        took = time.time() - start
        t2 += took
        t2_2 += took ** 2

    print(f'avg = {t1 / N}, sd = {(t1_2 / N - (t1 / N) ** 2) ** 0.5} for {prob1.__name__}')
    print(f'avg = {t2 / N}, sd = {(t2_2 / N - (t2 / N) ** 2) ** 0.5} for {prob2.__name__}')


comparePerf(no_mul, no_rec_no_mul, 10)
