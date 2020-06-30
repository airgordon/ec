from ece import ece
from zzn import zzn


class ec:

    def __init__(self, field, a, b, G, n=None):
        if not isinstance(field, zzn):
            raise Exception

        self.field = field
        self.a = a
        self.b = b

        self.Z = ece(self)

        if G is not None:
            self.G = ece(self, G[0], G[1])
            self.n = n
            self.checkGeneratorOrder()

    def of(self, x, y):
        return ece(self, x, y)

    def checkGeneratorOrder(self):
        if (self.n * self.G != self.Z):
            raise Exception('Wrong generator order')

    def allG(self):
        yield self.Z

        t = self.G

        while not t == self.Z:
            yield t
            t = t + self.G

    def all(self, field=None):
        yield self.Z
        if not field:
            field = self.field
        for x in field.generator():
            for y in field.generator():
                try:
                    yield ece(self, x, y)
                except:
                    pass
