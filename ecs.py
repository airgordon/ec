from ec import ec
from hex import h2i
from zzn import zzn



def bitcoin():
    N = pow(2, 256) \
        - pow(2, 32) \
        - pow(2, 9) \
        - pow(2, 8) \
        - pow(2, 7) \
        - pow(2, 6) \
        - pow(2, 4) \
        - pow(2, 0)

    field = zzn(N)
    a = field.of(0)
    b = field.of(7)

    n = 115792089237316195423570985008687907852837564279074904382605163141518161494337
    Gx = field.of(55066263022277343669578718895168534326250603453777594175500187360389116729240)
    Gy = field.of(32670510020758816978083085130507043184471273380659243275938904335757337482424)

    return ec(field, a, b, (Gx, Gy), n)

def paar():
    N = 17

    field = zzn(N)
    a = field.of(2)
    b = field.of(2)

    n = 19
    Gx = field.of(5)
    Gy = field.of(1)

    return ec(field, a, b, (Gx, Gy), n)

def singular():
    N = 1009

    field = zzn(N)
    a = field.of(37)
    b = field.of(0)

    n = 980
    # (11 27) -- 70 order
    Gx = None
    Gy = None

    return ec(field, a, b, (Gx, Gy), n)

def gost34_10_2001():
    N = h2i("8000000000000000000000000000000000000000000000000000000000000431")

    field = zzn(N)
    a = field.of(7)
    b = field.of(h2i("5F BF F4 98 AA 93 8C E7 39 B8 E0 22 FB AF EF 40 \
                      56 3F 6E 6A 34 72 FC 2A 51 4C 0C E9 DA E2 3B 7E"))

    n = h2i("8000000000000000000000000000000150FE8A1892976154C59CFC193ACCF5B3")
    Gx = field.of(2)
    Gy = field.of(h2i("8E2A8A0E65147D4BD6316030E16D19C85C97F0A9CA267122B96ABBCEA7E8FC8"))

    return ec(field, a, b, (Gx, Gy), n)

def id_GostR3410_2001_CryptoPro_A_ParamSet():  # a b N n x y
    N = h2i("00 FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF \
             FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FD \
             97")

    field = zzn(N)
    a = field.of(h2i("00 FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF \
                      FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FD \
                      94"))

    b = field.of(166)

    n = h2i("00 FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF \
             FF 6C 61 10 70 99 5A D1 00 45 84 1B 09 B7 61 B8 \
             93")

    Gx = field.of(1)
    Gy = field.of(h2i("00 8D 91 E4 71 E0 98 9C DA 27 DF 50 5A 45 3F 2B \
                       76 35 29 4F 2D DF 23 E3 B1 22 AC C9 9C 9E 9F 1E \
                       14"))

    return ec(field, a, b, (Gx, Gy), n)

def id_GostR3410_2001_CryptoPro_XchA_ParamSet():  # a b N n x y
    N = h2i("00 FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF \
             FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FD \
             97")

    field = zzn(N)
    a = field.of(h2i("00 FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF \
                      FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FD \
                      94"))

    b = field.of(166)

    n = h2i("00 FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF \
             FF 6C 61 10 70 99 5A D1 00 45 84 1B 09 B7 61 B8 \
             93")

    Gx = field.of(1)
    Gy = field.of(h2i("00 8D 91 E4 71 E0 98 9C DA 27 DF 50 5A 45 3F 2B \
                       76 35 29 4F 2D DF 23 E3 B1 22 AC C9 9C 9E 9F 1E \
                       14"))

    return ec(field, a, b, (Gx, Gy), n)

def secp128r1():
    N = pow(2, 128) \
        - pow(2, 97) \
        - 1

    field = zzn(N)
    a = field.of(h2i("FFFF FFFD FFFF FFFF FFFF FFFF FFFF FFFC"))
    b = field.of(h2i("E875 79C1 1079 F43D D824 993C 2CEE 5ED3"))

    n = h2i("FFFF FFFE 75A3 0D1B 9038 A115")
    Gx = field.of(h2i("161F F752 8B89 9B2D 0C28 607C A52C 5B86"))
    Gy = field.of(h2i("CF5A C839 5BAF EB13 C02D A292 DDED 7A83"))

    return ec(field, a, b, (Gx, Gy), n)

# Pairings for beginners
def beginners():
    N = 11

    field = zzn(N)
    a = field.of(4)
    b = field.of(3)

    n = 14
    Gx = field.of(0)
    Gy = field.of(5)

    return ec(field, a, b, (Gx, Gy), n)

def beginners2_2_5():
    N = 67

    field = zzn(N)
    a = field.of(4)
    b = field.of(3)

    n = 79
    Gx = None
    Gy = None

    return ec(field, a, b, (Gx, Gy), n)

def beginners2_2_6():
    N = 19

    field = zzn(N)
    a = field.of(0)
    b = field.of(5)

    n = None

    return ec(field, a, b, None, n)

def beginners4_1_1():
    N = 11

    field = zzn(N)
    a = field.of(0)
    b = field.of(4)

    n = 12

    return ec(field, a, b, None, n)

def beginners4_1_3():
    N = 11

    field = zzn(N)
    a = field.of(7)
    b = field.of(2)

    return ec(field, a, b, None, None)