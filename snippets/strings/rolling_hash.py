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


def get_rolling_hashes(s, k):
    n = len(s)
    roll_h1, roll_h2 = [0]*(n+1-k), [0]*(n+1-k)
    hash1 = hash2 = 0
    for i in range(k):
        hash1 = (BASE1 * hash1 + s[i]) % MOD1
        hash2 = (BASE2 * hash2 + s[i]) % MOD2
    roll_h1[0], roll_h2[0] = hash1, hash2
    high_h1, high_h2 = pow(BASE1, k - 1, MOD1), pow(BASE2, k - 1, MOD2)
    left = 0
    for right in range(k, n):
        hash1 = ((hash1 - high_h1 * s[left]) * BASE1 + s[right]) % MOD1
        hash2 = ((hash2 - high_h2 * s[left]) * BASE2 + s[right]) % MOD2
        left += 1
        roll_h1[left], roll_h2[left] = hash1, hash2
    return roll_h1, roll_h2
