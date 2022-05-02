from algebra.poly2 import poly
from ec.ecs import *
from ec.rationalFnc import rationalFnc
from ec.rationalFncE import rationalFncE

ec = beginners3_1_1()

z = ec.field
p = poly(z)
u = p.u

P = ec.of(z(26), z(20))
Q = ec.of(z(63), z(78))
R = ec.of(z(59), z(95))
S = ec.of(z(24), z(25))
T = ec.of(z(77), z(84))
U = ec.of(z(30), z(99))
Z = ec.Z

ratFnc = rationalFnc(ec, p)
x = u * u * z(71) + u * z(91) + z(91)
y = p.of([z(6)])
rx = u * u + z(70) * u + z(11)
ry = p.of([z(0)])

t = ratFnc.line(P, Q) / ratFnc.line(-U, R)

f = rationalFncE(x, y,
                 rx, ry,
                 ratFnc, None)

print(t)

print(f(U))
print(f(S))
print(f(P))
print(f(Q))

print(Q + P + (-R) + (-T))

# print(f(R))
# print(f(T))
