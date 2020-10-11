from ecs import *
from finField import finField
from millersF import millersF
from pairings import Weil_1, Weil_2
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


print(Weil_2(P, Q, R, S, r))
print(Weil_2(2 * P, 6 * Q, R, S, r))
print(Weil_2(6 * P, 2 * Q, R, S, r))
print(Weil_2(2 * P, 7 * Q, R, S, r))
print(Weil_2(7 * P, 2 * Q, R, S, r))
print(Weil_2(P, Q, R, S, r) ** r)

print(1)
