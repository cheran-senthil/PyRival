import random

HMOD = 2147483647
HBASE1 = random.randrange(HMOD)
HBASE2 = random.randrange(HMOD)


class Hashing:
    def __init__(self, s, mod=HMOD, base1=HBASE1, base2=HBASE2):
        self.mod, self.base1, self.base2 = mod, base1, base2
        self._len = _len = len(s)
        f_hash, s_hash = [0] * (_len + 1), [0] * (_len + 1)
        for i in range(_len):
            f_hash[i + 1] = (base1 * f_hash[i] + s[i]) % mod
            s_hash[i + 1] = (base2 * s_hash[i] + s[i]) % mod
        self.f_hash, self.s_hash = f_hash, s_hash

    def hashed(self, start, stop):
        return ((self.f_hash[stop] - pow(self.base1, stop - start, self.mod) * self.f_hash[start]) % self.mod,
                (self.s_hash[stop] - pow(self.base2, stop - start, self.mod) * self.s_hash[start]) % self.mod)

    def get_hashes(self, length):
        mod = self.mod
        pow_base1, pow_base2 = pow(self.base1, length, mod), pow(self.base2, length, mod)
        f_hash = [(self.f_hash[i + length] - pow_base1 * self.f_hash[i]) % mod for i in range(self._len - length + 1)]
        s_hash = [(self.s_hash[i + length] - pow_base2 * self.s_hash[i]) % mod for i in range(self._len - length + 1)]
        return f_hash, s_hash
