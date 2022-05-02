from algebra.zzne import zzne
from ec.rationalFncE import rationalFncE


class rationalFnc:
    def __init__(self, ec, poly):
        self.ec = ec
        self.poly = poly
        self.one = rationalFncE(self.poly.one, self.poly.zero, self.poly.one, self.poly.zero, self, dict())

    def vertical(self, p):
        return self.line(-p, p)

    def line(self, u, v):
        div = self._divisor(u, v)
        if not u and not v:
            return self.one
        if not v:
            return rationalFncE(self.poly.of([self.poly.field.one, -u.x]), self.poly.zero, self.poly.one,
                                self.poly.zero,
                                self, div)
        if not u:
            return rationalFncE(self.poly.of([self.poly.field.one, -v.x]), self.poly.zero, self.poly.one,
                                self.poly.zero,
                                self, div)

        if u == v:
            _2 = zzne(2, self.ec.field)
            _3 = zzne(3, self.ec.field)

            k = (_3 * u.x * u.x + u.ec.a) / (_2 * u.y)
            b = - u.x * k + u.y
            return rationalFncE(self.poly.of([-k, -b]), self.poly.one, self.poly.one, self.poly.zero,
                                self, div)

        if v.x == u.x:
            return rationalFncE(self.poly.of([self.poly.field.one, -v.x]), self.poly.zero, self.poly.one,
                                self.poly.zero,
                                self, div)

        k = (v.y - u.y) / (v.x - u.x)
        b = - u.x * k + u.y

        p = [-k, -b] if k else [-b]  # todo убрать эту срань !!
        return rationalFncE(self.poly.of(p), self.poly.one, self.poly.one, self.poly.zero,
                            self, div)

    def _divisor(self, A, B):
        div = dict()
        C = -(A + B)

        def incr(div, P, inc=1):
            v = div.get(P, 0)
            div[P] = v + inc

        incr(div, A)
        incr(div, B)
        incr(div, C)
        incr(div, self.ec.Z, -3)

        return div

    def _double_explicit(self, f_q, qP, q2P):
        """
        :param f_q: function with divisor (f_q) = q(P) - ([q]P) - (q - 1)(Zero)
        :param qP: [q]P
        :param q2P: [2q]P
        :return: f_2q_P
        """
        d = self.line(qP, qP) / self.vertical(q2P)
        return f_q * f_q * d

    def _double(self, f_q, qP, q2P, x):
        """
        :param f_q: f_q_P(x)
        :param qP: [q]P
        :param q2P: [2qP]
        :param x: function argument, for which we want to calculate function
        :return: f_2q_P(x)
        """
        d = self.line(qP, qP)(x) / self.vertical(q2P)(x)
        return f_q * f_q * d

    def _mfunc_explicit(self, P, m):
        if m == 1:
            return self.one

        (q, r) = divmod(m, 2)
        f_q = self._mfunc_explicit(P, q)

        qP = q * P

        f_2q = self._double_explicit(f_q, qP, 2 * qP)
        if r:
            dr = self.line(P, (m - 1) * P) / self.vertical(m * P)
            f_m = f_2q * dr
        else:
            f_m = f_2q
        return f_m

    def _mfunc(self, P, m, x):
        if m == 1:
            return self.one(x)

        (q, r) = divmod(m, 2)
        f_q = self._mfunc(P, q, x)

        qP = q * P
        f_2q = self._double(f_q, qP, 2 * qP, x)

        if r:
            dr = self.line(P, (m - 1) * P)(x) / self.vertical(m * P)(x)
            f_m = f_2q * dr
        else:
            f_m = f_2q
        return f_m

    def _mfunc_no_mul(self, P, m, x):
        if m == 1:
            return self.one(x), P

        (q, r) = divmod(m, 2)

        f_q, qP = self._mfunc_no_mul(P, q, x)

        q2P = qP + qP

        f_2q = self._double(f_q, qP, q2P, x)

        if r:
            mP = q2P + P
            dr = self.line(P, q2P)(x) / self.vertical(mP)(x)
            f_m = f_2q * dr
        else:
            f_m = f_2q
            mP = q2P

        return f_m, mP

    def _mfunc_no_rec(self, P, m, x):

        if m == 1:
            return self.one(x)

        n = m.bit_length() - 2
        g = 1 << n

        acc = self.one(x)
        q = 1
        qP = P
        q2P = P + P

        while g:
            if m & g:
                r = 1
            else:
                r = 0

            i = 2 * q + r

            f_q = acc

            f_2q = self._double(f_q, qP, q2P, x)

            if r:
                dr = self.line(P, (i - 1) * P)(x) / self.vertical(i * P)(x)
                f_i = f_2q * dr
            else:
                f_i = f_2q

            acc = f_i
            g = g >> 1
            q = i

            if r:
                qP = q2P + P
            else:
                qP = q2P

            q2P = qP + qP

        return acc

    def _mfunc_no_rec_no_mul(self, P, m, x):

        if m == 1:
            return self.one(x)

        n = m.bit_length() - 2
        g = 1 << n

        acc = self.one(x)
        q = 1
        qP = P
        q2P = P + P

        while True:
            if m & g:
                r = 1
                iP = q2P + P
            else:
                r = 0
                iP = q2P

            i = 2 * q + r

            f_q = acc

            f_2q = self._double(f_q, qP, q2P, x)

            if r:
                dr = self.line(P, q2P)(x) / self.vertical(iP)(x)
                f_i = f_2q * dr
            else:
                f_i = f_2q

            acc = f_i
            q = i
            g = g >> 1
            if not g:
                return acc

            qP = iP
            q2P = qP + qP

    def mfunc_no_rec(self, P, r, x):
        f = self._mfunc_no_rec(P, r - 1, x)
        d = self.line(P, -P)
        return f * d(x)

    def mfunc_no_rec_no_mul(self, P, r, x):
        f = self._mfunc_no_rec_no_mul(P, r - 1, x)
        d = self.line(P, -P)
        return f * d(x)

    def mfunc_no_mul(self, P, r, x):
        f, _ = self._mfunc_no_mul(P, r - 1, x)
        d = self.line(P, -P)
        return f * d(x)

    def mfunc(self, P, r, x):
        f, _ = self._mfunc(P, r - 1, x)
        d = self.line(P, -P)
        return f * d(x)

    def mfunc_explicit(self, P, r):
        f = self._mfunc_explicit(P, r)
        # d = self.line(P, -P)
        # return f * d
        return f

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
