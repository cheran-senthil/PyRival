from collections import Counter
from math import gcd

import _random


class Random(_random.Random):
    def shuffle(self, x):
        for i in range(len(x) - 1, 0, -1):
            j = int(self.random() * (i + 1))
            x[i], x[j] = x[j], x[i]

    randrange = lambda self, a, b, step=1: a + step * int(self.random() * ((
        b - a + step + [1, -1][step < 0]) // step))
    randint = lambda self, a, b: a + int(self.random() * (b - a + 1))
    choice = lambda self, seq: seq[int(self.random() * len(seq))]


randint = Random().randint


def memodict(f):
    """ Memoization decorator for a function taking a single argument. """

    class memodict(dict):
        def __missing__(self, key):
            ret = self[key] = f(key)
            return ret

    return memodict().__getitem__


@memodict
def pollard_rho(n):
    if n == 1:
        return Counter()

    d, s = n - 1, 0
    while not d & 1:
        d, s = d >> 1, s + 1

    def try_composite(a):
        if pow(a, d, n) == 1:
            return False

        p = pow(a, d, n)
        for _ in range(s):
            if p == n - 1:
                return False
            p = (p * p) % n

        return True

    if not any(
            try_composite(w)
            for w in [2, 325, 9375, 28178, 450775, 9780504, 1795265022]):
        return Counter({n: 1})

    y, c, m = randint(1, n - 1), randint(1, n - 1), randint(1, n - 1)
    g, r, q = 1, 1, 1

    while g == 1:
        x, k = y, 0

        for _ in range(r):
            y = (y * y + c) % n

        while (k < r) and (g == 1):
            ys = y

            for _ in range(min(m, r - k)):
                y = (y * y + c) % n
                q = (q * abs(x - y)) % n

            g = gcd(q, n)
            k += m

        r *= 2

    if g == n:
        while True:
            ys = (ys * ys + c) % n
            g = gcd(abs(x - ys), n)
            if g > 1:
                break

    return pollard_rho(g) + pollard_rho(n // g)


@memodict
def prime_factors(n):
    """ Prime factorization using Pollard's rho algorithm. """
    factors = Counter()

    for p in [2, 3, 5, 13, 19, 73, 193, 407521, 299210837]:
        if n % p == 0:
            cnt = 0
            while n % p == 0:
                n, cnt = n // p, cnt + 1
            factors[p] = cnt

    return factors + pollard_rho(n)
