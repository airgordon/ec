class zzne:

    @staticmethod
    def invert(x, N):
        res = pow(x, N - 2, N)
        if divmod(x * res, N)[1] != 1:
            raise Exception('There is no inverse of {} over {}'.format(x, N))
        return res

    def __init__(self, x, field):
        if not isinstance(x, int):
            raise Exception('{}'.format(x))

        self.x = x % field.N
        self.field = field
        self.N = field.N

        if x < 0 or x >= self.N:
            raise ValueError('{} is out of bound of this zzn: [0, {})'.format(x, self.N))

    def __bool__(self):
        return self.x != 0

    def __int__(self):
        return self.x

    def __add__(self, other):
        if isinstance(other, zzne):
            return zzne(divmod(self.x + other.x, self.N)[1], self.field)
        elif isinstance(other, int):
            return self + zzne(other, self.field)
        else:
            return NotImplemented

    def __neg__(self):
        return zzne(divmod(self.N - self.x, self.N)[1], self.field)

    def __sub__(self, other):
        if isinstance(other, zzne):
            return self + (-other)
        elif isinstance(other, int):
            return self - zzne(other, self.field)
        else:
            return NotImplemented

    def __mul__(self, other):
        if isinstance(other, zzne):
            return zzne(divmod(self.x * other.x, self.N)[1], self.field)
        elif isinstance(other, int):
            return zzne(divmod(self.x * other, self.N)[1], self.field)
        else:
            return NotImplemented

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
        return zzne(zzne.invert(self.x, self.N), self.field)

    def __truediv__(self, other):
        if isinstance(other, zzne):
            return self * ~other
        elif isinstance(other, int):
            return self / zzne(other, self.field)
        else:
            return NotImplemented

    def __eq__(self, other):
        if isinstance(other, zzne):
            return self.x == other.x
        elif isinstance(other, int):
            return self == zzne(other, self.field)
        else:
            return NotImplemented

    def __hash__(self):
        return self.x

    def __str__(self):
        return '{}'.format(self.x)

    def __repr__(self):
        return '{}'.format(self.x)
