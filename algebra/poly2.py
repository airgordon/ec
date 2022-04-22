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

    def _gen(self, from_=-1, normalized=False):
        if from_ == -1:
            yield self.zero
            polyList = [self.field.one]
        else:
            polyList = [self.field.zero] * from_ + [self.field.one]
        while True:
            yield polye(self, polyList)
            i = 0
            while True:
                if i < len(polyList):
                    x = polyList[i]
                    if normalized and i == len(polyList) - 1:
                        polyList[i] = self.field.zero
                    else:
                        x = x + self.field.one
                        polyList[i] = x
                        if x:
                            break
                    i += 1
                else:
                    polyList.append(self.field.one)
                    break

    def gen(self, from_=-1, to=inf, normalized=False):
        toPredicate = lambda x: abs(x) < to
        return takewhile(toPredicate, self._gen(from_, normalized))

    def irredusable(self, N):
        for i in self.gen(N, N + 1, normalized=True):
            t = True
            for j in self.gen(1, abs(i) // 2 + 1, True):
                if not divmod(i, j)[1]:
                    t = False
                    break
            if t:
                yield i
