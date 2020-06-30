from typing import List

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
        self._sqrt = None

    def of(self, x):
        (r, q) = divmod(x, self.N)
        if r:
            raise Exception("Remainder should be zero")
        if x < 0 or x >= self.N:
            raise Exception
        return finFieldE(x, self)

    def char(self):
        return self.N.poly.field.char() ** abs(self.N)

    def generator(self):
        for x in self.N.poly.gen(to=abs(self.N)):
            yield finFieldE(x, self)

    def init_sqrt(self):
        self._sqrt = {}
        for i in self.generator():
            i_2 = i * i
            l: List[finFieldE] = self._sqrt[i_2]
            if l:
                l.append(i)
            else:
                self._sqrt[i_2] = [i]
