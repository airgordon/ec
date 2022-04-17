from millersFe import millersFe
from zzne import zzne


class millersF:
    def __init__(self, ec, poly):
        self.ec = ec
        self.poly = poly
        self.one = millersFe(self.poly.one, self.poly.zero, self.poly.one, self.poly.zero, self)

    def of(self, x, y, r):
        raise Exception()
        return millersFe(x, y, r, self)

    def vertical(self, p):
        if not p:
            raise Exception("p is Zero")
        k = self.poly.of([self.poly.field.one, -p.x])
        return millersFe(self.poly.one, self.poly.zero, k, self.poly.zero, self)

    def line(self, u, v):
        if not u and not v:
            raise Exception("u and v is Zero")
        if not v:
            return millersFe(self.poly.of([self.poly.field.one, -u.x]), self.poly.zero, self.poly.one, self.poly.zero,
                             self)
        if not u:
            return millersFe(self.poly.of([self.poly.field.one, -v.x]), self.poly.zero, self.poly.one, self.poly.zero,
                             self)

        if u == v:
            _2 = zzne(2, self.ec.field)
            _3 = zzne(3, self.ec.field)

            k = (_3 * u.x * u.x + u.a) / (_2 * u.y)
            b = - u.x * k + u.y
            return millersFe(self.poly.of([-k, -b]), self.poly.one, self.poly.one, self.poly.zero, self)

        if v.x == u.x:
            return millersFe(self.poly.of([self.poly.field.one, -v.x]), self.poly.zero, self.poly.one, self.poly.zero,
                             self)

        k = (v.y - u.y) / (v.x - u.x)
        b = - u.x * k + u.y

        p = [-k, -b] if k else [-b]  # todo убрать эту срань !!
        return millersFe(self.poly.of(p), self.poly.one, self.poly.one, self.poly.zero, self)

    def _mfunc(self, P, m, x):
        if m == 1:
            return self.one[x]

        (q, r) = divmod(m, 2)

        f_m_2 = self._mfunc(P, q, x)


        d = self.line(q * P, q * P)[x] * self.vertical(2 * q * P)[x]

        if r:
            d = d * (self.line(P, (m - 1) * P)[x] * self.vertical(m * P)[x])

        return f_m_2 * f_m_2 * d

    def mfunc(self, P, r, x):
        if P.order() != r:
            raise Exception()
        f = self._mfunc(P, r - 1, x)
        d = self.line(P, -P)
        return f * d[x]

    def mfunc_slow(self, P, r):
        if P.order() != r:
            raise Exception()
        f = self.one
        T = P
        for m in range(2, r):
            f = f * (self.line(P, T) * self.vertical(T + P))
            T = T + P

        if P + T:
            raise Exception()
        f = f * self.line(P, T)
        return f
