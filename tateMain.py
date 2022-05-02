import time

from ec.ecs import *
from ec.tate import tate
from algebra.finField import finField
from algebra.poly2 import poly

ec = beginners5_2_1()

z = ec.field
p = poly(z)
u = p.u
N2 = p.of([z.one, z.zero, z(2)])
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
Q = ec.of(ff.of(u + 1), ff.of(4 * u + 2))
R = ec.of(ff.of(2 * u), ff.of(u + 2))


def assertTrue(ex):
    if not ex:
        raise Exception


def test():
    start_time = time.time()

    ex1 = ff.of(4 * u + 4)
    ex2 = ff.of(2 * u + 4)
    ex3 = ff.of(3 * u + 2)

    assertTrue(tate(P, Q, R, r) == ex1)
    assertTrue(tate(P, 2 * Q, R, r) == ex2)
    assertTrue(tate(2 * P, Q, R, r) == ex3)

    print("--- %s seconds ---" % (time.time() - start_time))


test()
