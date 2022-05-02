from ec.ecs import *
from algebra.finField import finField
from algebra.poly2 import poly

from ec.pairings import Weil_slow, Weil_no_rec, Weil_no_rec_no_mul, Weil_no_mul

ec = beginners5_3_1()

zzz = ec.field
p = poly(zzz)
u = p.u
u2 = u * u
u3 = u * u * u
u4 = u * u * u * u

ff = finField(u4 - u2 * 4 + 5)

P = ec.of(zzz(45), zzz(23))

qx = u2 * 31 + 29
qy = u3 * 35 + u * 11

Q = ec.of(ff.of(qx), ff.of(qy))

it = ec.all()
it.__next__()
R = it.__next__()
S = it.__next__()

r = 17


def assertTrue(ex):
    if not ex:
        raise Exception


def test(weil):
    ex1 = ff.of(u3 * 22 + u2 * 12 + u * 32 + 13)
    ex2 = ff.of(u3 * 17 + u2 * 21 + u * 11 + 14)
    ex3 = ff.of(u3 * 9 + u2 * 26 + u * 22 + 4)
    ex4 = ff.one

    assertTrue(weil(P, Q, R, S, r) == ex1)
    assertTrue(weil(2 * P, 6 * Q, R, S, r) == ex2)
    assertTrue(weil(6 * P, 2 * Q, R, S, r) == ex2)
    assertTrue(weil(2 * P, 7 * Q, R, S, r) == ex3)
    assertTrue(weil(7 * P, 2 * Q, R, S, r) == ex3)
    assertTrue(weil(P, Q, R, S, r) ** r == ex4)

test(Weil_slow)
test(Weil_no_mul)
test(Weil_no_rec)
test(Weil_no_rec_no_mul)