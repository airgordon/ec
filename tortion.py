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
            raise Exception("Not a valid field extension")
        self.ec = ec
        self.r = r
        self.exField = exField

    def all(self):
        return filter(lambda x: not (self.r * x), self.ec.all(self.exField))