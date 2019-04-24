from collections import Counter
from math import gcd


def memodict(f):
    """Memoization decorator for a function taking a single argument"""

    class memodict(dict):
        def __missing__(self, key):
            ret = self[key] = f(key)
            return ret

    return memodict().__getitem__


def is_prime(n):
    """Deterministic variant of the Miller-Rabin primality test"""
    if n < 2 or n % 6 % 4 != 1:
        return n - 2 < 2
    s = ((n - 1) & (1 - n)).bit_length() - 1
    d = n >> s
    for a in [2, 325, 9375, 28178, 450775, 9780504, 1795265022]:
        p, i = pow(a, d, n), s
        while p != 1 and p != n - 1 and a % n and i:
            i -= 1
            p = (p * p) % n
        if p != n - 1 and i != s:
            return False
    return True


def pollard_rho(n):
    if not n & 1:
        return 2
    for i in range(2, n):
        x, y = i, (i * i + 1) % n
        f = gcd(abs(x - y), n)
        while f == 1:
            x, y = (x * x + 1) % n, (y * y + 1) % n
            y = (y * y + 1) % n
            f = gcd(abs(x - y), n)
        if f != n:
            return f


@memodict
def prime_factors(n):
    """Prime factorization using Pollard's rho algorithm"""
    if n <= 1:
        return Counter()
    if is_prime(n):
        return Counter([n])
    f = pollard_rho(n)
    return prime_factors(f) + prime_factors(n // f)
