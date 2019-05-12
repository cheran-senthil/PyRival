import random

MAXVAL = 10**9 + 1
MOD1 = 2147483629
MOD2 = 2147483647
# BASE = random.choice(numbers not in s)
BASE1 = random.randint(MAXVAL, MOD1 - 1)
BASE2 = random.randint(MAXVAL, MOD2 - 1)


def get_hashes(s):
    n = len(s) + 1
    hash1, hash2 = [0] * n, [0] * n
    for i, si in enumerate(s):
        hash1[i + 1] = (BASE1 * hash1[i] + s[i]) % MOD1
        hash2[i + 1] = (BASE2 * hash2[i] + s[i]) % MOD2
    return hash1, hash2
