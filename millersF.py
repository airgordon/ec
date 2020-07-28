from millersFe import millersFe
from zzne import zzne


class millersF:
    def __init__(self, ec, poly):
        self.ec = ec
        self.poly = poly
        self.one = millersFe(self.poly.one, self.poly.zero, self.poly.one, self.poly.zero, self)

    def of(self, x, y, r):
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

    # def _divisor(self, P, m):
    #     if m == 1:
    #         return self.one
    #
    #     (q, r) = divmod(m, 2)
    #
    #     f = self._divisor(P, q) * self._divisor(P, q) * self.line(q * P, q * P) * self.vertical(2 * q * P)
    #
    #     if r:
    #         return f * (self.line(P, (m - 1) * P) * self.vertical(m * P))
    #     else:
    #         return f

    def _mfunc(self, P, m, xs):
        if m == 1:
            return map(lambda x: self.one.apply(x), xs)

        (q, r) = divmod(m, 2)

        f_m_2 = self._mfunc(P, q, xs)

        sq = map(lambda x: x * x, f_m_2)
        d = self.line(q * P, q * P) * self.vertical(2 * q * P)

        if r:
            d = d * (self.line(P, (m - 1) * P) * self.vertical(m * P))

        return list(map(lambda t: t[0] * d.apply(t[1]), zip(sq, xs)))

    def mfunc(self, P, r, xs):
        if P.order() != r:
            raise Exception()
        f = self._mfunc(P, r - 1, xs)
        d = self.line(P, -P)
        return list(map(lambda t: t[0] * d.apply(t[1]), zip(f, xs)))

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
        f = f * (self.line(P, T))
        return f
