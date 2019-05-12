import random


def extended_gcd(a, b):
    """returns gcd(a, b), s, r s.t. a * s + b * r == gcd(a, b)"""
    s, old_s = 0, 1
    r, old_r = b, a
    while r:
        q = old_r // r
        old_r, r = r, old_r - q * r
        old_s, s = s, old_s - q * s
    return old_r, old_s, (old_r - old_s * a) // b if b else 0


def modinv(a, m):
    """returns the modular inverse of a w.r.t. to m, works when a and m are coprime"""
    g, x, _ = extended_gcd(a % m, m)
    return x % m if g == 1 else None


MAXVAL = 10**9 + 1
MOD1 = 2147483629
MOD2 = 2147483647
# BASE = random.choice(numbers not in s)
BASE1 = random.randint(MAXVAL, MOD1 - 1)
BASE2 = random.randint(MAXVAL, MOD2 - 1)
INV1 = modinv(BASE1, MOD1)
INV2 = modinv(BASE2, MOD2)


class Hashing:
    def __init__(self, s):
        n = len(s)
        hash1, hash2 = [0]*(n + 1), [0]*(n + 1)
        inv1, inv2 = [0]*(n + 1), [0]*(n + 1)
        inv1[0] = inv2[0] = 1

        p1 = p2 = 1
        for i in range(n):
            hash1[i + 1] = (hash1[i] + s[i] * p1) % MOD1
            p1 = p1 * MAXVAL % MOD1
            inv1[i + 1] = inv1[i] * INV1 % MOD1

            hash2[i + 1] = (hash2[i] + s[i] * p2) % MOD2
            p2 = p2 * MAXVAL % MOD2
            inv2[i + 1] = inv2[i] * INV2 % MOD2
        self.hash1, self.hash2 = hash1, hash2
        self.inv1, self.inv2 = inv1, inv2

    def get_hash(self, i, len):
        return (self.hash1[i + len] - self.hash1[i] + MOD1) * self.inv1[i] % MOD1, \
               (self.hash2[i + len] - self.hash2[i] + MOD2) * self.inv2[i] % MOD2
