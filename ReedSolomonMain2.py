from algebra.zzn import zzn
from algebra.finField import finField
from algebra.poly2 import poly
from reedSolomon import ReedSolomon

Bit = zzn(2)
bitPoly = poly(Bit)
irredusables = bitPoly.irredusable(8)
irredusables.__next__()
GF256 = finField(irredusables.__next__())
p = poly(GF256)


# z5 = zzn(5)
# c = list(map(z5.of, [0, 0, 1, 3]))
# print(ft2(c, z5.of(2)))
# print(ft(c, z5.of(2)))


k = 3
n = 15
e = (n - k) // 2


RS = ReedSolomon(GF256, k, n)


m = [15, 87, 94]
s = RS.encode(m)
# r = s.copy()
#
# r[1] = 17
#
# start_time = time.time()
# rm1 = RS.decode(s)
# print(f'ReedSolomon decode took {time.time() - start_time}')
# rm2 = RS.decode(r)
#
# print(f'{list(map(int, s))}')
# print(f'{list(map(int, r))}')
#
# print(f'{rm1}')
# print(f'{rm2}')
