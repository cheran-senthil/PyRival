import random

MOD = 2147483647
BASE1 = random.randrange(MOD)
BASE2 = random.randrange(MOD)


class Hashing:
    def __init__(self, s):
        self._len = _len = len(s)
        f_hash, s_hash = [0] * (_len + 1), [0] * (_len + 1)
        for i in range(_len):
            f_hash[i + 1] = (BASE1 * f_hash[i] + s[i]) % MOD
            s_hash[i + 1] = (BASE2 * s_hash[i] + s[i]) % MOD
        self.f_hash, self.s_hash = f_hash, s_hash

    def hashed(self, start, stop):
        return ((self.f_hash[stop] - pow(BASE1, stop - start, MOD) * self.f_hash[start]) % MOD,
                (self.s_hash[stop] - pow(BASE2, stop - start, MOD) * self.s_hash[start]) % MOD)

    def get_hashes(self, length):
        pow_base1, pow_base2 = pow(BASE1, length, MOD), pow(BASE2, length, MOD)
        f_hash = [(self.f_hash[i + length] - pow_base1 * self.f_hash[i]) % MOD for i in range(self._len - length + 1)]
        s_hash = [(self.s_hash[i + length] - pow_base2 * self.s_hash[i]) % MOD for i in range(self._len - length + 1)]
        return f_hash, s_hash
