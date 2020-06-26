from itertools import islice, groupby

from ece import ece
from ecs import *
from finField import finField
from finFieldE import finFieldE
from morph import pi, morph, I, _pi
from poly2 import poly

ec = beginners2_2_5()

zzz = ec.field
p = poly(zzz)
N2 = p.irredusable(2).__next__()
ff2 = finField(N2)

N3 = p.irredusable(3).__next__()
ff3 = finField(N3)

x1 = zzz.of(15)
y1 = zzz.of(50)
P1 = ece(ec, x1, y1)

x2 = finFieldE(p.of([zzz.of(2), zzz.of(16)]), ff2)
y2 = finFieldE(p.of([zzz.of(30), zzz.of(39)]), ff2)
P2 = ece(ec, x2, y2)

x3 = finFieldE(p.of([zzz.of(15), zzz.of(4), zzz.of(8)]), ff3)
y3 = finFieldE(p.of([zzz.of(44), zzz.of(30), zzz.of(21)]), ff3)
P3 = ece(ec, x3, y3)

q = zzz.N
t = -11
print((pi ** 2 - t * pi + q * I) & P2)
print(_pi(_pi(P2)) + (-t) * P2 + q * P2)
print(_pi(_pi(P2)) + (-t) * _pi(P2) + q * P2)
print()



print((pi - 1 * pi) & P2)
print(P2 + (-1) * P2)


# print(pi & P2)
# print(pi & P3)
# print(pi & (pi & P3) == pi @ pi & P3)
# print(pi @ pi @ pi & P3 == P3)
