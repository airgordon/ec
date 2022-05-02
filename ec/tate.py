from algebra.poly2 import poly
from ec.rationalFnc import rationalFnc


def tate(P, Q, R, r):
    zz = P.ec.field
    pl = poly(zz)
    mil = rationalFnc(P.ec, pl)

    f_QR = mil.mfunc_explicit(P, r)(Q + R)
    f_R = mil.mfunc_explicit(P, r)(R)

    pairing = f_QR / f_R
    return pairing