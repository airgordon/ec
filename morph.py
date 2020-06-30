from ece import ece


class morph:
    def __init__(self, f):
        self.f = f

    def __matmul__(self, other):
        if not isinstance(other, morph):
            raise Exception
        return morph(lambda x: self.f(other.f(x)))

    def __and__(self, other):
        return self.f(other)

    def __add__(self, other):
        if isinstance(other, morph):
            return morph(lambda x: (self & x) + (other & x))

        return morph(lambda x: (self & x) + other)

    def __radd__(self, other):
        if isinstance(other, morph):
            return morph(lambda x: (other.f & x) + (self.f & x))

        return morph(lambda x: other + (self.f & x))

    def __neg__(self):
        return morph(lambda x: -(self & x))

    def __sub__(self, other):
        return self + (-other)

    def __mul__(self, other):
        return NotImplemented

    def __rmul__(self, other):
        return morph(lambda x: other * (self & x))

    def __pow__(self, other):
        if not isinstance(other, int):
            raise Exception('{}'.format(other))
        if other < 0:
            return Exception
        if other == 0:
            return morph(lambda x: x)
        if other == 1:
            return self
        return self.__matmul__(self.__pow__(other - 1))


def _pi(point):
    if point:
        n = point.ec.field.N
        return ece(point.ec, point.x ** n, point.y ** n)
    else:
        return point


pi = morph(_pi)
I = morph(lambda x: x)
# (pi ** 2 - t * pi + q * I) & P2 == Zero
