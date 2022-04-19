from itertools import takewhile
from math import inf

from algebra.polye import polye


class poly:
    def __init__(self, field):
        self.field = field
        self.zero = polye(self, [field.zero])
        self.one = polye(self, [field.one])
        self.u = polye(self, [field.zero, field.one])

    """Первый элемент входного списка СТАРШАЯ степень"""
    # TODO перейти на использование u и убрать ревёрс
    def of(self, l):
        return polye(self, reversed(list(l)))

    def _of(self, l):
        return polye(self, list(l))

    def _gen(self, normalized=False):
        yield self.zero
        l = list([self.field.one])
        while True:
            yield polye(self, l)
            i = 0
            while True:
                if i < len(l):
                    x = l[i]
                    if normalized and i == len(l) - 1:
                        l[i] = self.field.zero
                    else:
                        x = x + self.field.one
                        l[i] = x
                        if x:
                            break
                    i += 1
                else:
                    l.append(self.field.one)
                    break

    def gen(self, frm=-inf, to=inf, normalized=False):
        fromPredicate = lambda x: abs(x) >= frm
        toPredicate = lambda x: abs(x) < to
        return takewhile(toPredicate, filter(fromPredicate, self._gen(normalized)))

    def irredusable(self, N):
        for i in self.gen(N, N + 1, True):
            t = True
            for j in self.gen(1, abs(i) // 2 + 1, True):
                if not divmod(i, j)[1]:
                    t = False
                    break
            if t:
                yield i
