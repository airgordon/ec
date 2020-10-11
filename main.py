import time

from ecs import *
from finField import finField
from millersF import millersF
from pairings import Weil_1, Weil_2
from poly2 import poly
from tortion import tortion

ec = beginners4_0_1()

zzz = ec.field
p = poly(zzz)

ff = finField(p.of([zzz.of(1), zzz.of(0), zzz.of(1)]))

P = ec.of(zzz.of(2693), zzz.of(4312))

qx = p.of([zzz.of(633), zzz.of(6145)])
qy = p.of([zzz.of(7372), zzz.of(109)])

Q = ec.of(ff.of(qx), ff.of(qy))

R = P + Q
S = P + 2 * Q

r = 641
print(tortion.k(r, zzz.N))

start_time = time.time()

print(Weil_2(P, Q, R, S, r))
print(Weil_2(403 * P, Q, R, S, r))
print(Weil_2(P, Q, R, S, r) ** 403)
print(Weil_2(P, 135 * Q, R, S, r))
print(Weil_2(P, Q, R, S, r) ** 135)
print(Weil_2(403 * P, 135 * Q, R, S, r))
print(Weil_2(P, Q, R, S, r) ** (135*403))

print("--- %s seconds ---" % (time.time() - start_time))
