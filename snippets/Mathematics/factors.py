import random
from collections import Counter
from functools import reduce
from math import gcd


def memodict(f):
    """ Memoization decorator for a function taking a single argument. """
    class memodict(dict):
        def __missing__(self, key):
            ret = self[key] = f(key)
            return ret
    return memodict().__getitem__


def _try_composite(a, d, n, s):
    if pow(a, d, n) == 1:
        return False
    for i in range(s):
        if pow(a, 2**i * d, n) == n - 1:
            return False
    return True


def is_prime(n):
    """
    Deterministic variant of the Miller-Rabin primality test to determine
    whether a given number is prime.

    Parameters
    ----------
    n : int
        n >= 0, an integer to be tested for primality.

    Returns
    -------
    bool
        False if n is composite, otherwise True.
    """
    if n in [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37]:
        return True

    if (any((n % p) == 0 for p in [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37])) or (n in [0, 1]):
        return False

    d, s = n - 1, 0
    while not d % 2:
        d, s = d >> 1, s + 1

    if n < 2047:
        return not _try_composite(2, d, n, s)
    if n < 1373653:
        return not any(_try_composite(a, d, n, s) for a in [2, 3])
    if n < 25326001:
        return not any(_try_composite(a, d, n, s) for a in [2, 3, 5])
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
    return not any(_try_composite(a, d, n, s) for a in [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37])


def _factor(n):
    for i in [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37]:
        if n % i == 0:
            return i

    y, c, m = random.randint(1, n - 1), random.randint(1, n - 1), random.randint(1, n - 1)
    g, r, q = 1, 1, 1

    while g == 1:
        x = y
        for i in range(r):
            y = ((y * y) % n + c) % n
        k = 0
        while (k < r) and (g == 1):
            ys = y
            for i in range(min(m, r - k)):
                y = ((y * y) % n + c) % n
                q = q * (abs(x - y)) % n
            g = gcd(q, n)
            k = k + m
        r = r * 2

    if g == n:
        while True:
            ys = ((ys * ys) % n + c) % n
            g = gcd(abs(x - ys), n)
            if g > 1:
                break

    return g


@memodict
def factors(n):
    """
    Integer factorization using Pollard's rho algorithm.

    Parameters
    ----------
    n : int
        n > 1, an integer to be factorized.

    Returns
    -------
    Counter
        Counter of the prime factors of n.
    """
    if is_prime(n):
        return Counter([n])
    else:
        f = _factor(n)
        if f == n:
            return factors(n)
        else:
            return factors(f) + factors(n//f)


all_factors = lambda n: set(reduce(list.__add__,
                            ([i, n//i] for i in range(1, int(n**0.5) + 1, 2 if n % 2 else 1) if n % i == 0)))
