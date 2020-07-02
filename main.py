from itertools import islice, groupby

from ece import ece
from ecs import *
from finField import finField
from finFieldE import finFieldE
from millersF import millersF
from morph import pi, morph, I, _pi
from poly2 import poly
from tortion import tortion

ec = beginners5_0_1()

zzz = ec.field
p = poly(zzz)

P = ec.of(zzz.of(10), zzz.of(7))
ff = finField(p.of([zzz.of(1), zzz.of(0), zzz.of(0), zzz.of(1), zzz.of(2)]))
# t = tortion(ec, 5, ff)
# tor_points = list(t.all())

qx = p.of([zzz.of(2), zzz.of(21), zzz.of(12), zzz.of(18)])
qy = p.of([zzz.of(8), zzz.of(15), zzz.of(14), zzz.of(6)])

# Q = tor_points[6]
Q = ec.of(ff.of(qx), ff.of(qy))

it = ec.all()
it.__next__()
R = ec.of(zzz.of(0), zzz.of(11))
S = ec.of(zzz.of(0), zzz.of(12))

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


print(Weil(P, Q, R, S, 5))
print(Weil(P, Q, R, S, 5) ** 5)

print(1)


