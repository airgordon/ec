from itertools import islice, groupby

from ece import ece
from ecs import *
from finField import finField
from finFieldE import finFieldE
from morph import pi, morph, I, _pi
from poly2 import poly
from tortion import tortion

ec = beginners5_0_1()

zzz = ec.field
p = poly(zzz)
N5 = p.irredusable(4).__next__()
ff5 = finField(N5)
p1 = p.of([zzz.one, zzz.of(2), zzz.of(2), zzz.of(5)])
p2 = p.of([zzz.one, zzz.of(16)])
print(divmod(p1, p2))

P = ec.of(zzz.of(10), zzz.of(7))



print(1 * P)
print(2 * P)
print(3 * P)
print(4 * P)
print(5 * P)
print(6 * P)
print("!$%")
t = tortion(ec, 5, ff5)
l = []
for ghy in t.all():
    print(ghy)
    l.append(ghy)
