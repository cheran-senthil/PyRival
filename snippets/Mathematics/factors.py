import random
from collections import Counter
from fractions import gcd


def memodict(f):
    """ Memoization decorator for a function taking a single argument """
    class memodict(dict):
        def __missing__(self, key):
            ret = self[key] = f(key)
            return ret
    return memodict().__getitem__


def _try_composite(a, d, n, s):
    if pow(a, d, n) == 1:
        return False
    for i in range(s):
        if pow(a, 2**i * d, n) == n-1:
            return False
    return True


def is_prime(n):
    if n in [0, 1, 2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43]:
        return True
    if any((n % p) == 0 for p in [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53]):
        return False
    d, s = n - 1, 0
    while not d % 2:
        d, s = d >> 1, s + 1

    if n < 2047:
        return not _try_composite(2, d, n, s)
    if n < 1373653:
        return not any(_try_composite(a, d, n, s) for a in (2, 3))
    if n < 25326001:
        return not any(_try_composite(a, d, n, s) for a in (2, 3, 5))
    if n < 118670087467:
        if n == 3215031751:
            return False
        return not any(_try_composite(a, d, n, s) for a in [2, 3, 5, 7])
    if n < 2152302898747:
        return not any(_try_composite(a, d, n, s) for a in [2, 3, 5, 7, 11])
    if n < 3474749660383:
        return not any(_try_composite(a, d, n, s) for a in [2, 3, 5, 7, 11, 13])
    if n < 341550071728321:
        return not any(_try_composite(a, d, n, s) for a in [2, 3, 5, 7, 11, 13, 17])
    if n < 3825123056546413051:
        return not any(_try_composite(a, d, n, s) for a in [2, 3, 5, 7, 11, 13, 17, 19, 23])
    return not any(_try_composite(a, d, n, s) for a in [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53])


def factor(N):
    for i in [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53]:
        if N % i == 0:
            return i

    y, c, m = random.randint(1, N-1), random.randint(1, N-1), random.randint(1, N-1)
    g, r, q = 1, 1, 1

    while g == 1:
        x = y
        for i in range(r):
            y = ((y * y) % N + c) % N
        k = 0
        while (k < r) and (g == 1):
            ys = y
            for i in range(min(m, r - k)):
                y = ((y * y) % N + c) % N
                q = q * (abs(x - y)) % N
            g = gcd(q, N)
            k = k + m
        r = r * 2

    if g == N:
        while True:
            ys = ((ys * ys) % N + c) % N
            g = gcd(abs(x - ys), N)
            if g > 1:
                break

    return g


@memodict
def factors(N):
    if is_prime(N):
        return Counter([N])
    else:
        f = factor(N)
        if f == N:
            return factors(N)
        else:
            return factors(f) + factors(N//f)
