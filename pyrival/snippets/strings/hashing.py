import random


class Hashing:
    def __init__(self, s):
        self.MOD = 2147483647
        self.BASE1 = random.randrange(self.MOD)
        self.BASE2 = random.randrange(self.MOD)

        self._len = _len = len(s)
        f_hash, s_hash = [0] * (_len + 1), [0] * (_len + 1)
        for i in range(_len):
            f_hash[i + 1] = (self.BASE1 * f_hash[i] + s[i]) % self.MOD
            s_hash[i + 1] = (self.BASE2 * s_hash[i] + s[i]) % self.MOD
        self.f_hash, self.s_hash = f_hash, s_hash

    def hashed(self, start, stop):
        return ((self.f_hash[stop] - pow(self.BASE1, stop - start, self.MOD) * self.f_hash[start]) % self.MOD,
                (self.s_hash[stop] - pow(self.BASE2, stop - start, self.MOD) * self.s_hash[start]) % self.MOD)

    def get_hashes(self, length):
        pow_base1, pow_base2 = pow(self.BASE1, length, self.MOD), pow(self.BASE2, length, self.MOD)
        f_hash = [(self.f_hash[i + length] - pow_base1 * self.f_hash[i]) % self.MOD
                  for i in range(self._len - length + 1)]
        s_hash = [(self.s_hash[i + length] - pow_base2 * self.s_hash[i]) % self.MOD
                  for i in range(self._len - length + 1)]
        return f_hash, s_hash
