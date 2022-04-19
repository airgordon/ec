import time

from algebra.matrix import matrix
from algebra.poly2 import poly
from algebra.Fourier import ft


class ReedSolomon:

    def _calcVandermondeMatrix(self):

        deg = self.k + self.e
        res = [[] for _ in range(0, self.n)]

        for i in range(0, self.n):
            acc = self.poly.field.one
            for j in range(0, deg):
                res[i].append(acc)
                acc = acc * self.a[i]

        return matrix(res, self.field)

    def __init__(self, field, k, n):
        self.field = field
        self.poly = poly(field)
        self.k = k
        self.n = n
        self.e = (n - k) // 2

        self.a = [field.G ** i for i in range(0, n)]

        start_time = time.time()
        self.V = self._calcVandermondeMatrix()
        print(f'_calcMatrix took {time.time() - start_time}')

    def int2field(self, x):
        (q, f) = self.field.fromInt(x)
        if q:
            raise Exception(f'{x} is too big to fit in {self.field}')
        return f

    def encode(self, m_int):
        if not len(m_int) == self.k:
            raise Exception("")
        m_field = list(map(self.int2field, m_int))

        start_time = time.time()
        m = self.poly._of(m_field)
        s = list(map(int, map(m.at, self.a)))
        print(f'encode simple took {time.time() - start_time}')

        start_time = time.time()
        s1 = list(map(int, ft(m_field, K=self.n)))
        print(f'encode ft took {time.time() - start_time}')

        return s

    def solutionMatrix(self, r, M):
        rows = []
        for i in range(0, self.n):  # for each alpha
            row = []
            for j in range(0, self.e + 1):  # for each D(x) coeff
                row.append(r[i] * M.rows[i][j])
            for j in range(0, self.k + self.e):  # for each Q(x) coeff
                row.append(-M.rows[i][j])
            rows.append(row)
        row = []
        for j in range(0, self.k + 2 * self.e + 1):
            if j == self.e:
                row.append(self.field.one)
            else:
                row.append(self.field.zero)
        rows.append(row)
        return matrix(rows, self.field)

    def decode(self, r_int):
        if not len(r_int) == self.n:
            raise Exception("")

        r = list(map(self.int2field, r_int))

        S = self.solutionMatrix(r, self.V)

        v = [self.field.zero] * self.n + [self.field.one]

        h = S.solve(v)

        print(S * h)

        D = h[0:self.e + 1]
        Q = h[self.e + 1:self.k + 2 * self.e + 1]

        D.reverse()
        Q.reverse()

        self.poly.u.normalize(D)
        self.poly.u.normalize(Q)

        pD = self.poly.of(D)
        pQ = self.poly.of(Q)

        (rm, b) = divmod(pQ, pD)
        if b:
            raise Exception()

        return list(map(int, rm.l))
