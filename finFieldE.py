from euqlid import gcd
from polye import polye
from zzne import zzne


class finFieldE:

    def __init__(self, x, field):
        if not isinstance(x, polye):
            raise Exception('{}'.format(x))

        self.x = x
        self.field = field

    def __bool__(self):
        return self.x.__bool__()

    def __add__(self, other):
        if isinstance(other, finFieldE):
            return finFieldE(self.x + other.x, self.field)
        elif isinstance(other, zzne):
            return finFieldE(self.x + self.field.N.poly.of([other]), self.field)
        return NotImplemented

    def __radd__(self, other):
        return self.__add__(other)

    def __neg__(self):
        return finFieldE(-self.x, self.field)

    def __sub__(self, other):
        return self + (-other)

    def __rsub__(self, other):
        return self.__sub__(other)

    def __mul__(self, other):
        if isinstance(other, finFieldE):
            return finFieldE(divmod(self.x * other.x, self.field.N)[1], self.field)
        elif isinstance(other, zzne):
            return finFieldE(self.x * other, self.field)
        return NotImplemented

    def __rmul__(self, other):
        return self.__mul__(other)

    def __pow__(self, other):
        if not isinstance(other, int):
            raise Exception('{}'.format(other))
        if other < 0:
            return self.__invert__().__pow__(-other)
        if other == 0:
            return self.field.one
        if other == 1:
            return self
        r, q = divmod(other, 2)
        t = self.__mul__(self).__pow__(r)
        if q:
            return t.__mul__(self)
        else:
            return t

    def sqrt(self):
        if not self.field._sqrt:
            self.field.init_sqrt()
        if self in self.field._sqrt:
            return self.field._sqrt[self]
        else:
            return []

    def log(self):
        if not self.field._log:
            self.field.init_log()

        return self.field._log[self]

    def __invert__(self):
        g, a, b = gcd(self.x, self.field.N, self.field.N.poly.zero, self.field.N.poly.one)
        if abs(g) > 0:
            raise Exception('{} have no inverse over {}'.format(self.x, self.field.N))
        return finFieldE(~g.asFieldElement() * a, self.field)

    def __hash__(self):
        return self.x.__hash__()

    def __truediv__(self, other):
        return self * ~other

    def __eq__(self, other):
        if isinstance(other, finFieldE):
            return self.x == other.x
        elif isinstance(other, zzne):
            return self.x == other
        return NotImplemented

    # convert field element to int
    def __int__(self):
        acc = 0
        m = 1
        for t in self.x.l:
            acc = acc + m * int(t)
            m = m * self.field.N.poly.field.N
        return acc

    def __str__(self):
        return '{}'.format(int(self))

    def __repr__(self):
        return '{}'.format(int(self))

