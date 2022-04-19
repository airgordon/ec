from typing import List

from algebra.finFieldE import finFieldE
from algebra.polye import polye
from algebra.Utills import distPrimes


class finField:
    def __init__(self, N, G=None):
        if abs(N) <= 0:
            raise Exception("Modulo degree should not be zero")
        self.N = N
        self.zero = finFieldE(N.poly.zero, self)
        self.one = finFieldE(N.poly.one, self)
        self._sqrt = None
        self._log = None
        self.G = self.getPrimitive()

    def getPrimitive(self):
        N = len(self.N.poly.field) ** abs(self.N)
        pows = list(map(lambda x: N // x, distPrimes(N - 1)))
        irredusables = self.N.poly.irredusable(abs(self.N))
        for elem in irredusables:
            fieldElem = finFieldE(elem, self)
            isPrimitive = True
            for p in pows:
                if fieldElem ** p == self.one:
                    isPrimitive = False
                    break
            if isPrimitive:
                return fieldElem

    def of(self, x):
        if not isinstance(x, polye):
            raise Exception
        (r, q) = divmod(x, self.N)
        if r:
            raise Exception("Remainder should be zero")
        return finFieldE(x, self)

    def __len__(self):
        return len(self.N.poly.field) ** abs(self.N)

    def char(self):
        return self.N.poly.field.char()

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

    def fromInt(self, x):
        if x == 0:
            return (0, self.zero)
        acc = []
        for i in range(0, abs(self.N)):
            (x, mod) = self.N.poly.field.fromInt(x)
            acc.append(mod)

        self.N.normalize(acc)
        p = self.N.poly._of(acc)
        return (x, finFieldE(p, self))

    def __str__(self):
        return f'GF({len(self.N.poly.field)}^{abs(self.N)})'

    def __repr__(self):
        return f'GF({len(self.N.poly.field)}^{abs(self.N)})'
