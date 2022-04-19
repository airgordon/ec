from algebra.zzne import zzne


class gost34_10_2001:
    def __init__(self, ec, prng):
        self.ec = ec
        self.prng = prng

    def privateToPublic(self, d):
        return self.ec.G * d

    def randEthKey(self):
        return self.prng.getK()

    def sign(self, d, h):
        P = self.ec.G
        q = self.ec.n

        e = divmod(h, q)[1]
        if e == 0:
            e = 1

        while (True):
            k = self.randEthKey()

            C = k * P

            r = divmod(C.x.x, q)[1]

            s = divmod(r * d + k * e, q)[1]

            if s != 0:
                break

        return r, s

    def checkSign(self, Q, sign, h):
        P = self.ec.G
        q = self.ec.n

        r, s = sign

        e = divmod(h, q)[1]
        if e == 0:
            e = 1

        v = zzne.invert(e, q)  # e ** -1

        z1 = divmod(-v * s, q)[1]
        z2 = divmod(v * r, q)[1]

        C = z1 * P + z2 * Q
        return divmod(C.x.x, q)[1] == r
