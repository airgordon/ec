import time

from ec.ecs import *
from algebra.finField import finField
from algebra.poly2 import poly

from ec.pairings import Weil_2

ec = beginners5_2_1()

zzz = ec.field
p = poly(zzz)
N2 = p.of([zzz.one, zzz.zero, zzz.of(2)])
ff = finField(N2)

all = list(ec.all(field=ff))
print(all)
print(len(all))

r = 3
h = len(all) / r ** 2

rE = set([r * P for P in all])
print(rE)

rTor = list(filter(lambda P: P.order() == r, all))
print(rTor)


P = all[6]
Q = ec.of(ff.of(qx), ff.of(qy))
R = P + Q
S = P + 2 * Q


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
