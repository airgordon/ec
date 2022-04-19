from ec.ecs import *
from algebra.finField import finField
from algebra.poly2 import poly

from ec.pairings import Weil_1, Weil_2

ec = beginners5_3_1()

zzz = ec.field
p = poly(zzz)

ff = finField(p.of([zzz.of(1), zzz.of(0), zzz.of(zzz.N - 4), zzz.of(0), zzz.of(5)]))

P = ec.of(zzz.of(45), zzz.of(23))

qx = p.of([zzz.of(31), zzz.of(0), zzz.of(29)])
qy = p.of([zzz.of(35), zzz.of(0), zzz.of(11), zzz.of(0)])

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
    ex1 = ff.of(p.of([zzz.of(22), zzz.of(12), zzz.of(32), zzz.of(13)]))
    ex2 = ff.of(p.of([zzz.of(17), zzz.of(21), zzz.of(11), zzz.of(14)]))
    ex3 = ff.of(p.of([zzz.of(9), zzz.of(26), zzz.of(22), zzz.of(4)]))
    ex4 = ff.one

    assertTrue(weil(P, Q, R, S, r) == ex1)
    assertTrue(weil(2 * P, 6 * Q, R, S, r) == ex2)
    assertTrue(weil(6 * P, 2 * Q, R, S, r) == ex2)
    assertTrue(weil(2 * P, 7 * Q, R, S, r) == ex3)
    assertTrue(weil(7 * P, 2 * Q, R, S, r) == ex3)
    assertTrue(weil(P, Q, R, S, r) ** r == ex4)

test(Weil_1)
test(Weil_2)