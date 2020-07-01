from typing import List

from finFieldE import finFieldE
from polye import polye
from zzne import zzne


class finField:

    def __init__(self, N, G = None):
        if abs(N) <= 0:
            raise Exception("Modulo degree should not be zero")
        self.N = N
        self.zero = finFieldE(N.poly.zero, self)
        self.one = finFieldE(N.poly.one, self)
        self._sqrt = None
        self._log = None
        if G is None:
            self.G = finFieldE(N.poly.of([N.poly.field.one, N.poly.field.zero]), self)
        else:
            self.G = G

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
            if i_2 in self._sqrt:
                self._sqrt[i_2].append(i)
            else:
                self._sqrt[i_2] = [i]

    def init_log(self):
        self._log = {}
        p = self.one
        for i in range(0, self.char()):
            self._log[p] = i
            p = p * self.G

        if len(self._log) != self.char() - 1:
            raise Exception("Not a generator")
