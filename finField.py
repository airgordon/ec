from finFieldE import finFieldE
from polye import polye
from zzne import zzne


class finField:
    def __init__(self, N):
        if abs(N) <= 0:
            raise Exception("Modulo degree should not be zero")
        self.N = N
        self.zero = finFieldE(N.poly.zero, self)
        self.one = finFieldE(N.poly.zero, self)
    def of(self, x):
        (r, q) = divmod(x, self.N)
        if r:
            raise Exception("Remainder should be zero")
        if x < 0 or x >= self.N:
            raise Exception
        return finFieldE(x, self)

    def generator(self):
        for x in self.N.poly.gen(to=abs(self.N)):
            yield finFieldE(x, self)
