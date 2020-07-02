from itertools import dropwhile


class subField:
    def __init__(self, exField):
        self.exField = exField

    def generator(self):
        return dropwhile(lambda x: abs(x.x) < 1, self.exField.generator())

    pass


class tortion:
    @staticmethod
    def k(r, q):
        t = 1
        p = q
        while (p - 1) % r != 0:
            t = t + 1
            p = p * q
        return t

    def __init__(self, ec, r, exField):
        if ec.field.char() ** tortion.k(r, ec.field.char()) != exField.char():
            raise Exception('Not a valid field extension ({} {})'.format(tortion.k(r, ec.field.char()), len(exField.N.l))
)
        self.ec = ec
        self.r = r
        self.exField = exField

    def all(self):
        it1 = filter(lambda x: not (self.r * x), self.ec.all()) #

        it1.__next__()
        P = it1.__next__()

        it2 = self.ec.all(subField(self.exField))
        it2.__next__()
        Q = filter(lambda x: not (self.r * x), it2).__next__()

        for i in range(0, self.r):
            for j in range(0, self.r):
                yield i * Q + j * P
