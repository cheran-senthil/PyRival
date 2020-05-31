from collections import Counter


def gcd(x, y):
    """greatest common divisor of x and y"""
    while y:
        x, y = y, x % y
    return x


def memodict(f):
    """memoization decorator for a function taking a single argument"""
    class memodict(dict):
        def __missing__(self, key):
            ret = self[key] = f(key)
            return ret

    return memodict().__getitem__


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
    factors = prime_factors(p - 1)

    for i in range(2, p + 1):
        ok = True
        for j in factors:
            ok &= pow(i, (p - 1) // j, p) != 1
        if ok:
            return i

    return None
