from ecs import *
from finField import finField
from millersF import millersF
from poly2 import poly
from pairings import Weil_1, Weil_2, Weil_3

ec = beginners5_1_1()

zzz = ec.field
p = poly(zzz)
N2 = p.irredusable(2).__next__()  # i^2 + 1
ff2 = finField(N2)

P = ec.of(zzz.of(2), zzz.of(11))

qx = p.of([zzz.of(21)])
qy = p.of([zzz.of(12), zzz.zero])
Q = ec.of(ff2.of(qx), ff2.of(qy))

rx = ff2.of(p.of([zzz.of(17), zzz.zero]))
ry = ff2.of(p.of([zzz.of(2), zzz.of(21)]))
sx = ff2.of(p.of([zzz.of(10), zzz.of(18)]))
sy = ff2.of(p.of([zzz.of(13), zzz.of(13)]))
S = ec.of(rx, ry)
R = ec.of(sx, sy)


def Weil(P, Q, R, S, r):
    zz = P.ec.field
    pl = poly(zz)
    mil = millersF(P.ec, pl)

    fp = mil.mfunc_slow(P, r)
    fq = mil.mfunc_slow(Q, r)

    f = fp * (mil.line(P, R) * mil.vertical(P + R)) ** (-r)
    g = fq * (mil.line(Q, S) * mil.vertical(Q + S)) ** (-r)

    pairing = f[Q + S] * g[R] / (f[S] * g[P + R])
    return pairing


def test(weil):
    ex1 = ff2.of(p.of([zzz.of(15), zzz.of(11)]))
    if weil(P, Q, R, S, 3) != ex1:
        raise Exception("Test failed")

    ex2 = ff2.of(p.of([zzz.of(8), zzz.of(11)]))

    if weil(2 * P, Q, R, S, 3) != ex2:
        raise Exception("Test failed")

    if weil(P, 2 * Q, R, S, 3) != ex2:
        raise Exception("Test failed")

    if ex1 ** 3 != ff2.one:
        raise Exception("Test failed")

    if weil(2 * P, 2 * Q, R, S, 3) != ex1:
        raise Exception("Test failed")


test(Weil)
test(Weil_1)
test(Weil_2)
test(Weil_3)
