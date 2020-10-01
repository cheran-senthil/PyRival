import random

HMOD = 2147483647
HBASE1 = random.randrange(HMOD)
HBASE2 = random.randrange(HMOD)


class Hashing:
    def __init__(self, s, mod=HMOD, base1=HBASE1, base2=HBASE2):
        self.mod, self.base1, self.base2 = mod, base1, base2
        self._len = _len = len(s)
        f_hash, f_pw = [0] * (_len + 1), [1] * (_len + 1)
        s_hash, s_pw = f_hash[:], f_pw[:]
        for i in range(_len):
            f_hash[i + 1] = (base1 * f_hash[i] + s[i]) % mod
            s_hash[i + 1] = (base2 * s_hash[i] + s[i]) % mod
            f_pw[i + 1] = (base1 * f_pw[i]) % mod
            s_pw[i + 1] = (base2 * s_pw[i]) % mod
        self.f_hash, self.f_pw = f_hash, f_pw
        self.s_hash, self.s_pw = s_hash, s_pw

    def hashed(self, start, stop):
        return (
            (self.f_hash[stop] - self.f_pw[stop - start] * self.f_hash[start]) % self.mod,
            (self.s_hash[stop] - self.s_pw[stop - start] * self.s_hash[start]) % self.mod,
        )

    def get_hashes(self, length):
        mod = self.mod
        return (
            [(self.f_hash[i + length] - self.f_pw[length] * self.f_hash[i]) % mod for i in range(self._len - length + 1)],
            [(self.s_hash[i + length] - self.s_pw[length] * self.s_hash[i]) % mod for i in range(self._len - length + 1)],
        )
