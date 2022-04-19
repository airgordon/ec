from algebra.zzne import zzne
from ec.rationalFncE import rationalFncE


class rationalFnc:
    def __init__(self, ec, poly):
        self.ec = ec
        self.poly = poly
        self.one = rationalFncE(self.poly.one, self.poly.zero, self.poly.one, self.poly.zero, self)

    def of(self, x, y, r):
        raise Exception()
        return rationalFncE(x, y, r, self)

    def vertical(self, p):
        if not p:
            raise Exception("p is Zero")

        return self.line(-p, p)

    def line(self, u, v):
        if not u and not v:
            raise Exception("u and v is Zero")
        if not v:
            return rationalFncE(self.poly.of([self.poly.field.one, -u.x]), self.poly.zero, self.poly.one, self.poly.zero,
                                self)
        if not u:
            return rationalFncE(self.poly.of([self.poly.field.one, -v.x]), self.poly.zero, self.poly.one, self.poly.zero,
                                self)

        if u == v:
            _2 = zzne(2, self.ec.field)
            _3 = zzne(3, self.ec.field)

            k = (_3 * u.x * u.x + u.a) / (_2 * u.y)
            b = - u.x * k + u.y
            return rationalFncE(self.poly.of([-k, -b]), self.poly.one, self.poly.one, self.poly.zero, self)

        if v.x == u.x:
            return rationalFncE(self.poly.of([self.poly.field.one, -v.x]), self.poly.zero, self.poly.one, self.poly.zero,
                                self)

        k = (v.y - u.y) / (v.x - u.x)
        b = - u.x * k + u.y

        p = [-k, -b] if k else [-b]  # todo убрать эту срань !!
        return rationalFncE(self.poly.of(p), self.poly.one, self.poly.one, self.poly.zero, self)

    def _mfunc(self, P, m, x):
        if m == 1:
            return self.one(x)

        (q, r) = divmod(m, 2)

        f_m_2 = self._mfunc(P, q, x)

        qP = q * P

        d = self.line(qP, qP)(x) / self.vertical(2 * qP)(x)

        if r:
            d = d * (self.line(P, (m - 1) * P)(x) / self.vertical(m * P)(x))

        return f_m_2 * f_m_2 * d

    def mfunc(self, P, r, x):
        f = self._mfunc(P, r - 1, x)
        d = self.line(P, -P)
        return f * d(x)

    def mfunc_slow(self, P, r):
        f = self.one
        T = P
        for m in range(2, r):
            f = f * (self.line(P, T) / self.vertical(T + P))
            T = T + P

        if P + T:
            raise Exception()
        f = f * self.line(P, T)
        return f
