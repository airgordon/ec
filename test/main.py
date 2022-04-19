import time

from ec.ecs import *
from algebra.finField import finField
from algebra.poly2 import poly

from ec.pairings import Weil_2

ec = beginners4_0_1()

zzz = ec.field
p = poly(zzz)
u = p.u

ff = finField(p.of([zzz.of(1), zzz.of(0), zzz.of(1)]))

P = ec.of(zzz.of(2693), zzz.of(4312))

qx = p.of([zzz.of(633), zzz.of(6145)])
qy = p.of([zzz.of(7372), zzz.of(109)])

Q = ec.of(ff.of(qx), ff.of(qy))

R = P + Q
S = P + 2 * Q

r = 641


def assertTrue(ex):
    if not ex:
        raise Exception


def test(weil):
    start_time = time.time()

    ex1 = ff.of(p.of([zzz.of(6744), zzz.of(5677)]))
    ex2 = ff.of(p.of([zzz.of(3821), zzz.of(7025)]))
    ex3 = ff.of(p.of([zzz.of(248), zzz.of(5)]))
    ex4 = ff.of(p.of([zzz.of(2719), zzz.of(2731)]))

    assertTrue(weil(P, Q, R, S, r) == ex1)
    assertTrue(weil(403 * P, Q, R, S, r) == ex2)
    assertTrue(weil(P, Q, R, S, r) ** 403 == ex2)
    assertTrue(weil(P, 135 * Q, R, S, r) == ex3)
    assertTrue(weil(P, Q, R, S, r) ** 135 == ex3)
    assertTrue(weil(403 * P, 135 * Q, R, S, r) == ex4)
    assertTrue(weil(P, Q, R, S, r) ** (135 * 403) == ex4)

    print("--- %s seconds ---" % (time.time() - start_time))


test(Weil_2)
