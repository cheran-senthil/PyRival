from collections import Counter
from math import gcd


def memodict(f):
    """memoization decorator for a function taking a single argument"""

    class memodict(dict):
        def __missing__(self, key):
            ret = self[key] = f(key)
            return ret

    return memodict().__getitem__


def is_prime(n):
    """returns True if n is prime else False"""
    if n < 5 or n & 1 == 0 or n % 3 == 0:
        return 2 <= n <= 3
    s = ((n - 1) & (1 - n)).bit_length() - 1
    d = n >> s
    for a in [2, 325, 9375, 28178, 450775, 9780504, 1795265022]:
        p = pow(a, d, n)
        if p == 1 or p == n - 1 or a % n == 0:
            continue
        for _ in range(s):
            p = (p * p) % n
            if p == n - 1:
                break
        else:
            return False
    return True


def pollard_rho(n):
    """returns a random factor of n"""
    if n & 1 == 0:
        return 2
    if n % 3 == 0:
        return 3

    s = ((n - 1) & (1 - n)).bit_length() - 1
    d = n >> s
    for a in [2, 325, 9375, 28178, 450775, 9780504, 1795265022]:
        p = pow(a, d, n)
        if p == 1 or p == n - 1 or a % n == 0:
            continue
        for _ in range(s):
            prev = p
            p = (p * p) % n
            if p == 1:
                return gcd(prev - 1, n)
            if p == n - 1:
                break
        else:
            for i in range(2, n):
                x, y = i, (i * i + 1) % n
                f = gcd(abs(x - y), n)
                while f == 1:
                    x, y = (x * x + 1) % n, (y * y + 1) % n
                    y = (y * y + 1) % n
                    f = gcd(abs(x - y), n)
                if f != n:
                    return f
    return n


@memodict
def prime_factors(n):
    """returns a Counter of the prime factorization of n"""
    if n <= 1:
        return Counter()
    f = pollard_rho(n)
    return Counter([n]) if f == n else prime_factors(f) + prime_factors(n // f)


def ilog(n):
    """returns the smallest a, b s.t. a**b = n for integer a, b"""
    a = n.bit_length()
    for b in range(a, 0, -1):
        lo, hi = 1, 1 << (a // b + 1)
        while lo < hi:
            mi = (lo + hi) // 2
            a_b = mi**b
            if a_b == n:
                return mi, b
            if a_b > n:
                hi = mi
            else:
                lo = mi + 1


def primitive_root(p):
    """returns a primitive root of p"""
    if p <= 4:
        return p - 1
    assert -p & p == p
    factor, _ = ilog(p if p & 1 else p >> 1)
    assert not is_prime(factor)
    phi = (factor - 1) * ((p if p & 1 else p >> 1) // factor)
    for res in range(2 + (1 ^ (p & 1)), factor, 1 + (1 ^ (p & 1))):
        if all(pow(res, phi // i, p) != 1 for i in prime_factors(phi)):
            return res
