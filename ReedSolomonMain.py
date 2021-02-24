from matrix import matrix
from zzn import zzn
from finField import finField
from poly2 import poly

Bit = zzn(2)
bitPoly = poly(Bit)
GF256 = finField(bitPoly.irredusable(8).__next__())
p = poly(GF256)


# convert int to field element
def f(x):
    l = []
    while (x != 0):
        (x, b) = divmod(x, 2)
        if b:
            l.append(Bit.one)
        else:
            l.append(Bit.zero)
    if not l:
        l.append(Bit.zero)
    l.reverse()
    return GF256.of(bitPoly.of(l))

k = 2
n = 6
e = (n - k) // 2

a = [f(1), f(2), f(3), f(4), f(5), f(6)]


def calcMatrix(alpha, deg):
    acc = p.one
    res = [[] for _ in alpha]

    for j in range(0, deg):
        for i in range(0, len(alpha)):
            res[i].append(acc.at(alpha[i]))
        acc = acc * p.u

    return matrix(res, GF256)


M = calcMatrix(a, k + e)
M2 = matrix([[f(1), f(1), f(1)],
             [f(1), f(2), f(4)],
             [f(1), f(3), f(5)],
             [f(1), f(4), f(16)]], GF256)

m = p.u * f(15) + f(88)
s = list(map(m.at, a))
r = s.copy()
r[1] = f(17)
# r[4] = f(83)


def solutionMatrix(r, M):
    rows = []
    for i in range(0, n):  # for each alpha
        row = []
        for j in range(0, e + 1):  # for each D(x) coeff
            row.append(r[i] * M.rows[i][j])
        for j in range(0, k + e):  # for each Q(x) coeff
            row.append(-M.rows[i][j])
        rows.append(row)
    row = []
    for j in range(0, k + 2 * e + 1):
        if j == e:
            row.append(f(1))
        else:
            row.append(f(0))
    rows.append(row)
    return matrix(rows, GF256)


S = solutionMatrix(r, M)
# print(len(S.rows[0]))
# print(len(S.rows))
#
D = p.u * (p.u - a[1])
Q = m * D

V = D.l + Q.l
# print(S * V)

v = [GF256.zero] * n + [GF256.one]

h = S.solve(v)
print(S * h)

D = h[0:e + 1]
Q = h[e + 1:k + 2 * e + 1]
# print(D)
D.reverse()
Q.reverse()
p.u.normalize(D)
p.u.normalize(Q)
pD = p.of(D)
pQ = p.of(Q)
(rm, b) = divmod(pQ, pD)
if b:
    raise Exception()

print(f'{list(map(int, s))}')
print(f'{list(map(int, r))}')

print(f'{list(map(int, rm.l))}')
print(f'{list(map(int, m.l))}')
