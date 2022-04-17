from functools import reduce
from operator import neg, add
from itertools import zip_longest

import math

from Utills import list_hash
from zzne import zzne


class polye:
    def __init__(self, poly, l):
        self.poly = poly
        self.l = list(l)
        self.checkNorm()

    def __bool__(self):
        return self != self.poly.zero

    def __abs__(self):
        if not self:
            return -math.inf
        return len(self.l) - 1

    def checkNorm(self):
        if (not self.l):
            raise Exception("Empty poly")
        if (abs(self) > 0 and self.l[-1] == self.poly.field.zero):
            raise Exception("Not a normalized poly")

    def normalize(self, l):
        if not l:
            l.append(self.poly.field.zero)
            return
        while len(l) > 1:
            if l[-1] == self.poly.field.zero:
                l.pop()
            else:
                return
        return

    @staticmethod
    def _add(l1, l2, zero):
        return list(map(lambda p: p[0] + p[1], zip_longest(l1, l2, fillvalue=zero)))

    def __bool__(self):
        return len(self.l) != 1 or self.l[0] != self.poly.field.zero

    def __add__(self, other):
        if isinstance(other, polye):
            l = polye._add(self.l, other.l, self.poly.field.zero)
            self.normalize(l)
            return polye(self.poly, l)
        elif self.poly.field == other.field:
            res = self.l.copy()
            res[0] = res[0] + other
            return polye(self.poly, res)
        else:
            return NotImplemented

    def __neg__(self):
        return polye(self.poly, map(neg, self.l))

    def __sub__(self, other):
        return self + (-other)

    @staticmethod
    def _mulConst(c, l, field):
        if c == field.zero:
            return [field.zero]
        elif c == field.one:
            return l
        else:
            return list(map(lambda x: x * c, l))

    def __mul__(self, other):
        if isinstance(other, polye):
            acc = [self.poly.field.zero]
            l1 = list(other.l)
            l1.reverse()
            l2 = list(self.l)
            while (l1):
                x = l1.pop()
                acc = polye._add(acc, polye._mulConst(x, l2, self.poly.field), self.poly.field.zero)
                l2 = [self.poly.field.zero] + l2
            self.normalize(acc)
            return polye(self.poly, acc)
        elif self.poly.field == other.field:
            return polye(self.poly, polye._mulConst(other, self.l, self.poly.field))
        else:
            return NotImplemented

    def __rmul__(self, other):
        if isinstance(other, zzne) or isinstance(other, polye):
            return self.__mul__(other)
        return NotImplemented

    @staticmethod
    def _divPlus(divisible, incr, zero):
        result = list(map(lambda p: p[0] + p[1], zip_longest(reversed(divisible), reversed(incr), fillvalue=zero)))
        result.reverse()
        return result

    def __divmod__(self, other):
        if not other:
            raise ZeroDivisionError
        divisible = list(self.l)
        divisor = list(other.l)
        i = len(self.l) - len(other.l)
        head = divisor[-1]
        divisor = polye._mulConst(~head, divisor, self.poly.field)
        divisible = polye._mulConst(~head, divisible, self.poly.field)
        divisor.pop()
        acc = []
        while i >= 0:
            lead = divisible.pop()
            incr = polye._mulConst(-lead, divisor, self.poly.field)
            divisible = polye._divPlus(divisible, incr, self.poly.field.zero)
            acc.append(lead)
            i = i - 1
        if acc:
            acc.reverse()
        else:
            acc = [self.poly.field.zero]
        self.normalize(divisible)
        return (polye(self.poly, acc), polye(self.poly, polye._mulConst(head, divisible, self.poly.field)))

    def __hash__(self):
        return list_hash(self.l)

    def __eq__(self, other):
        if isinstance(other, polye):
            return self.l == other.l
        elif isinstance(other, zzne):
            return len(self.l) == 1 and self.l[0] == other
        return NotImplemented

    def __str__(self):
        reversed = list(self.l)
        reversed.reverse()
        return '{}'.format(reversed)

    def __repr__(self):
        return self.__str__()

    def __getitem__(self, x):
        pows = map(lambda t: t[1] * x ** t[0], enumerate(self.l))
        return reduce(add, pows)

    def asFieldElement(self):
        if len(self.l) != 1:
            raise Exception("Impossible!")
        return self.l[0]

    def at(self, x):
        acc = self.poly.field.zero
        m = self.poly.field.one
        for t in self.l:
            acc = acc + t * m
            m = m * x
        return acc
