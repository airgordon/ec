from itertools import islice, groupby

from ece import ece
from ecs import *
from finField import finField
from finFieldE import finFieldE
from millersF import millersF
from morph import pi, morph, I, _pi
from poly2 import poly
from tortion import tortion

ec = beginners5_1_1()

zzz = ec.field
p = poly(zzz)
N2 = p.irredusable(2).__next__()  # i^2 + 1
ff2 = finField(N2)

P = ec.of(zzz.of(2), zzz.of(11))

qx = p.of([zzz.of(21)])
qy = p.of([zzz.of(12), zzz.zero])
Q = ec.of(ff2.of(qx), ff2.of(qy))

P = 2 * P
Q = 2 * Q

rx = ff2.of(p.of([zzz.of(17), zzz.zero]))
ry = ff2.of(p.of([zzz.of(2), zzz.of(21)]))
sx = ff2.of(p.of([zzz.of(10), zzz.of(18)]))
sy = ff2.of(p.of([zzz.of(13), zzz.of(13)]))
S = ec.of(rx, ry)
R = ec.of(sx, sy)


def Weil(P, Q, R, S, r):
    zz = ec.field
    pl = poly(zz)
    mil = millersF(P.ec, pl)

    fp = mil.divisor(P, r)
    fq = mil.divisor(Q, r)

    f = fp * (mil.line(P, R) * mil.vertical(P + R)) ** (-r)
    g = fq * (mil.line(Q, S) * mil.vertical(Q + S)) ** (-r)

    pairing = f.apply(Q + S) * g.apply(R) / (f.apply(S) * g.apply(P + R))
    return pairing


print(Weil(P, Q, R, S, 3))
print(Weil(P, Q, R, S, 3) ** 3)
