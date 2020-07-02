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
            return millersFe(self.poly.of([self.poly.field.one, -u.x]), self.poly.zero, self.poly.one, self.poly.zero, self)
        if not u:
            return millersFe(self.poly.of([self.poly.field.one, -v.x]), self.poly.zero, self.poly.one, self.poly.zero, self)

        if u == v:
            _2 = zzne(2, self.ec.field)
            _3 = zzne(3, self.ec.field)

            k = (_3 * u.x * u.x + u.a) / (_2 * u.y)
            b = - u.x * k + u.y
            return millersFe(self.poly.of([-k, -b]), self.poly.one, self.poly.one, self.poly.zero, self)

        if v.x == u.x:
            return millersFe(self.poly.of([self.poly.field.one, -v.x]), self.poly.zero, self.poly.one, self.poly.zero, self)

        k = (v.y - u.y) / (v.x - u.x)
        b = - u.x * k + u.y
        return millersFe(self.poly.of([-k, -b]), self.poly.one, self.poly.one, self.poly.zero, self)

    def divisor(self, P, r):
        if P.order() != r:
            raise Exception()
        f = self.one
        R = P
        for i in range(2, r - 1):
            f = f * (self.line(P, R) * self.vertical(R + P))
            R = R + P
        f = f * (self.line(P, R))
        return f
