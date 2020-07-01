from zzne import zzne


class zzn:
    def __init__(self, N, G=None):
        self.N = N
        self.zero = self.of(0)
        self.one = self.of(1)
        self._sqrt = None
        self._log = None
        if G is None:
            self.G = N - 1
        else:
            self.G = G

    def char(self):
        return self.N

    def of(self, x):
        if x < 0 or x >= self.N:
            raise Exception
        return zzne(x, self)

    def generator(self):
        for i in range(0, self.N):
            yield zzne(i, self)

    def init_sqrt(self):
        self._sqrt = {}
        for i in self.generator():
            i_2 = i * i
            if i_2 in self._sqrt:
                self._sqrt[i_2].append(i)
            else:
                self._sqrt[i_2] = [i]

    def init_log(self):
        self._log = {}
        p = self.one
        for i in range(0, self.char()):
            self._log[p] = i
            p = p * self.G

        if len(self._log) != self.char() - 1:
            raise Exception("Not a generator")
