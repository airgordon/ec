from itertools import islice, groupby

from ece import ece
from ecs import *
from finField import finField
from finFieldE import finFieldE
from morph import pi, morph, I, _pi
from poly2 import poly
from tortion import tortion

ec = beginners4_1_3()

zzz = ec.field
p = poly(zzz)
N4 = p.of([zzz.one, zzz.zero, zzz.one, zzz.of(4)])
ff4 = finField(N4)

t = tortion(ec, 7, ff4)
l = []
for ghy in t.all():
    print(ghy)
    l.append(ghy)

print(1)
