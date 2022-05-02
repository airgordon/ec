from algebra.poly2 import poly
from ec.rationalFnc import rationalFnc


def Weil_slow(P, Q, R, S, r):
    _checkOrder(P, r)
    _checkOrder(Q, r)

    zz = P.ec.field
    pl = poly(zz)
    mil = rationalFnc(P.ec, pl)

    fp = mil.mfunc_slow(P, r)
    fq = mil.mfunc_slow(Q, r)

    f = fp * (mil.line(P, R) / mil.vertical(P + R)) ** (-r)
    g = fq * (mil.line(Q, S) / mil.vertical(Q + S)) ** (-r)

    pairing = f(Q + S) * g(R) / (f(S) * g(P + R))
    return pairing

def Weil_no_mul(P, Q, R, S, r):
    _checkOrder(P, r)
    _checkOrder(Q, r)

    zz = P.ec.field
    pl = poly(zz)
    mil = rationalFnc(P.ec, pl)

    f_QS = mil.mfunc_no_mul(P, r, Q + S) / (mil.line(P, R)(Q + S) / mil.vertical(P + R)(Q + S)) ** r
    g_PR = mil.mfunc_no_mul(Q, r, P + R) / (mil.line(Q, S)(P + R) / mil.vertical(Q + S)(P + R)) ** r
    f_S = mil.mfunc_no_mul(P, r, S) / (mil.line(P, R)(S) / mil.vertical(P + R)(S)) ** r
    g_R = mil.mfunc_no_mul(Q, r, R) / (mil.line(Q, S)(R) / mil.vertical(Q + S)(R)) ** r

    pairing = f_QS * g_R / (f_S * g_PR)
    return pairing


def Weil_no_rec(P, Q, R, S, r):
    _checkOrder(P, r)
    _checkOrder(Q, r)

    zz = P.ec.field
    pl = poly(zz)
    mil = rationalFnc(P.ec, pl)

    f_QS = mil.mfunc_no_rec(P, r, Q + S) / (mil.line(P, R)(Q + S) / mil.vertical(P + R)(Q + S)) ** r
    g_PR = mil.mfunc_no_rec(Q, r, P + R) / (mil.line(Q, S)(P + R) / mil.vertical(Q + S)(P + R)) ** r
    f_S = mil.mfunc_no_rec(P, r, S) / (mil.line(P, R)(S) / mil.vertical(P + R)(S)) ** r
    g_R = mil.mfunc_no_rec(Q, r, R) / (mil.line(Q, S)(R) / mil.vertical(Q + S)(R)) ** r

    pairing = f_QS * g_R / (f_S * g_PR)
    return pairing

def Weil_no_rec_no_mul(P, Q, R, S, r):
    _checkOrder(P, r)
    _checkOrder(Q, r)

    zz = P.ec.field
    pl = poly(zz)
    mil = rationalFnc(P.ec, pl)

    f_QS = mil.mfunc_no_rec_no_mul(P, r, Q + S) / (mil.line(P, R)(Q + S) / mil.vertical(P + R)(Q + S)) ** r
    g_PR = mil.mfunc_no_rec_no_mul(Q, r, P + R) / (mil.line(Q, S)(P + R) / mil.vertical(Q + S)(P + R)) ** r
    f_S = mil.mfunc_no_rec_no_mul(P, r, S) / (mil.line(P, R)(S) / mil.vertical(P + R)(S)) ** r
    g_R = mil.mfunc_no_rec_no_mul(Q, r, R) / (mil.line(Q, S)(R) / mil.vertical(Q + S)(R)) ** r

    pairing = f_QS * g_R / (f_S * g_PR)
    return pairing


def _checkOrder(P, r):
    if r * P:
        raise Exception()
