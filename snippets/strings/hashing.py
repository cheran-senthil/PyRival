import random

MAXVAL = 10**9 + 1
MOD1 = 2147483629
MOD2 = 2147483647
# BASE = random.choice(numbers not in s)
BASE1 = random.randint(MAXVAL, MOD1 - 1)
BASE2 = random.randint(MAXVAL, MOD2 - 1)


class Hashing:
    def __init__(self, s):
        self.n = n = len(s)
        hash1, hash2 = [0] * (n + 1), [0] * (n + 1)
        for i in range(n):
            hash1[i + 1] = (BASE1 * hash1[i] + s[i]) % MOD1
            hash2[i + 1] = (BASE2 * hash2[i] + s[i]) % MOD2
        self.hash1, self.hash2 = hash1, hash2

    def hashed(self, start, stop):
        return ((self.hash1[stop] - pow(BASE1, stop - start, MOD1) * self.hash1[start]) % MOD1,
                (self.hash2[stop] - pow(BASE2, stop - start, MOD2) * self.hash2[start]) % MOD2)

    def get_hashes(self, length):
        shift1, shift2 = pow(BASE1, length, MOD1), pow(BASE2, length, MOD2)
        hash1 = [(self.hash1[i + length] - shift1 * self.hash1[i]) % MOD1 for i in range(self.n - length + 1)]
        hash2 = [(self.hash2[i + length] - shift2 * self.hash2[i]) % MOD2 for i in range(self.n - length + 1)]
        return hash1, hash2


def hashed(s):
    n = len(s)
    hash1, hash2 = 0, 0
    for i in range(n):
        hash1 = (BASE1 * hash1 + s[i]) % MOD1
        hash2 = (BASE2 * hash2 + s[i]) % MOD2
    return hash1, hash2
