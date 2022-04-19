# y**2 = x**3 + a*x + b
from algebra.zzne import zzne


class ece:
    def __init__(self, eCurve, x=None, y=None):
        if not type(eCurve).__name__ is "ec":
            raise Exception

        self.ec = eCurve
        self.a = eCurve.a
        self.b = eCurve.b

        self.x = x
        self.y = y

        if (x is None) or (y is None):
            if not (x is None) and (y is None):
                raise Exception("Zero must not have coordinates")

            self.isZero = True
            return

        self.isZero = False
        self.check()

    def __bool__(self):
        return not self.isZero

    def __add__(self, other):
        if self.isZero:
            return other

        if other.isZero:
            return self

        if self.x == other.x and self.y == -other.y:
            return ece(self.ec)

        _2 = zzne(2, self.ec.field)
        _3 = zzne(3, self.ec.field)

        if self != other:
            k = (self.y - other.y) / (self.x - other.x)
        else:
            k = (_3 * self.x * self.x + self.a) / (_2 * self.y)

        xn = k * k - self.x - other.x
        yn = k * (xn - self.x) + self.y
        return ece(self.ec, xn, -yn)

    def __neg__(self):
        if self:
            return ece(self.ec, self.x, -self.y)
        return ece(self.ec)

    def __mul__(self, other):
        if not isinstance(other, int):
            return NotImplemented
        if other < 0:
            other = -other
            it = self.__neg__()
        else:
            it = self

        # other = other % it.ec.n

        if other == 0:
            return ece(it.ec)
        if other == 1:
            return it

        r, q = divmod(other, 2)
        if q == 0:
            return (it + it) * r
        else:
            return (it + it) * r + it

    def __rmul__(self, other):
        return self * other

    def __eq__(self, other):
        if self.isZero:
            return other.isZero

        if other.isZero:
            return False

        return self.x == other.x and self.y == other.y

    def order(self):
        t = self
        i = 1
        while not t.isZero:
            t = t + self
            i = i + 1
        return i

    def __hash__(self):
        if self.isZero:
            return 42
        return (self.x.x, self.y.x).__hash__()

    def check(self):
        x = self.x
        y = self.y
        if y * y != x * x * x + self.a * x + self.b:
            raise Exception("Not ec point")

    def __repr__(self):
        if self.isZero:
            return "Zero"
        else:
            return '({} {})'.format(self.x, self.y)

    def log_repr(self):
        f = lambda t: "g^" + str(t.log()) if t else "0"
        if self.isZero:
            return "Zero"
        else:
            return '({} {})'.format(f(self.x), f(self.y))
