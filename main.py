from ecs import *
from finField import finField
from millersF import millersF
from poly2 import poly
from tortion import tortion

ec = beginners5_3_1()

zzz = ec.field
p = poly(zzz)

ff = finField(p.of([zzz.of(1), zzz.of(0), zzz.of(zzz.N - 4), zzz.of(0), zzz.of(5)]))

P = ec.of(zzz.of(45), zzz.of(23))

qx = p.of([zzz.of(31), zzz.of(0), zzz.of(29)])
qy = p.of([zzz.of(35), zzz.of(0), zzz.of(11), zzz.of(0)])

# Q = tor_points[6]
Q = ec.of(ff.of(qx), ff.of(qy))

it = ec.all()
it.__next__()
R = it.__next__()
S = it.__next__()
# R = ec.of(zzz.of(0), zzz.of(11))
# S = ec.of(zzz.of(0), zzz.of(12))
r = 17
print(tortion.k(r, zzz.N))


def Weil(P, Q, R, S, r):
    zz = ec.field
    pl = poly(zz)
    mil = millersF(P.ec, pl)

    fp = mil.mfunc_slow(P, r)
    [a , b] = mil.mfunc(P, r, [Q + Q, Q])
    fq = mil.mfunc_slow(Q, r)
    fq2 = mil.mfunc(Q, r)

    f = fp * (mil.line(P, R) * mil.vertical(P + R)) ** (-r)
    g = fq * (mil.line(Q, S) * mil.vertical(Q + S)) ** (-r)

    pairing = f.apply(Q + S) * g.apply(R) / (f.apply(S) * g.apply(P + R))
    return pairing


print(Weil(P, Q, R, S, r))
print(Weil(2 * P, 6 * Q, R, S, r))
print(Weil(6 * P, 2 * Q, R, S, r))
print(Weil(2 * P, 7 * Q, R, S, r))
print(Weil(7 * P, 2 * Q, R, S, r))
print(Weil(P, Q, R, S, r) ** r)

print(1)
