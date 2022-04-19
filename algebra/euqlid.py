def _gcd(x, y, zero, one):
    if not x:
        return y, zero, one
    if not y:
        return x, one, zero
    if abs(x) >= abs(y):
        r, q = divmod(x, y)
        g, a, b = _gcd(q, y, zero, one)
        b = b - a * r
        return g, a, b
    else:
        r, q = divmod(y, x)
        g, a, b = _gcd(x, q, zero, one)
        a = a - b * r
        return g, a, b


def gcd(x, y, zero=0, one=1):
    g, a, b = _gcd(x, y, zero, one)
    if a * x + b * y != g:
        raise Exception()
    if divmod(x, g)[1]:
        raise Exception()
    if divmod(y, g)[1]:
        raise Exception()
    return g, a, b
