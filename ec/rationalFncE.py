from algebra.euqlid import gcd


class rationalFncE:

    def __init__(self, x, y, rx, ry, millersF):
        self.x = x
        self.y = y
        self.rx = rx
        self.ry = ry
        self.millersF = millersF

    def __mul__(self, other):
        _0 = self.millersF.poly.zero
        _1 = self.millersF.poly.one

        y = self.y * other.x + self.x * other.y
        x = self.x * other.x + self.y * other.y * self.millersF.ec.poly()

        ry = self.ry * other.rx + self.rx * other.ry
        rx = self.rx * other.rx + self.ry * other.ry * self.millersF.ec.poly()

        g_rx_ry, _, _ = gcd(rx, ry, _0, _1)
        g_rx_ry_y, _, _ = gcd(g_rx_ry, y, _0, _1)
        g_rx_ry_y_x, _, _ = gcd(g_rx_ry_y, x, _0, _1)

        x = divmod(x, g_rx_ry_y_x)[0]
        y = divmod(y, g_rx_ry_y_x)[0]
        rx = divmod(rx, g_rx_ry_y_x)[0]
        ry = divmod(ry, g_rx_ry_y_x)[0]

        return rationalFncE(x, y, rx, ry, self.millersF)

    def __pow__(self, other):
        if not isinstance(other, int):
            return NotImplemented
        if other < 0:
            return (~self).__pow__(-other)

        if other == 0:
            return self.millersF.one
        if other == 1:
            return self

        r, q = divmod(other, 2)
        if q == 0:
            return (self * self) ** r
        else:
            return (self * self) ** r * self

    def __invert__(self):
        return rationalFncE(self.rx, self.ry, self.x, self.y, self.millersF)

    def __truediv__(self, other):
        return self * ~other

    def __call__(self, P):
        x = P.x
        y = P.y
        q = self.x(x) + y * self.y(x)
        r = self.rx(x) + y * self.ry(x)
        return q / r
