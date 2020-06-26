from zzne import zzne


class zzn:
    def __init__(self, N):
        self.N = N
        self.zero = self.of(0)
        self.one = self.of(1)

    def of(self, x):
        if x < 0 or x >= self.N:
            raise Exception
        return zzne(x, self)

    def generator(self):
        for i in range(0, self.N):
            yield zzne(i, self)
