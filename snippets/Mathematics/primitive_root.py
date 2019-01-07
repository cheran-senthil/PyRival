from collections import Counter


def is_prime(n):
    if n in [2, 3, 5, 13, 19, 73, 193, 407521, 299210837]:
        return True

    if (n in [0, 1]) or (any((n % p) == 0 for p in [2, 3, 5, 13, 19, 73, 193, 407521, 299210837])):
        return False

    d, s = n - 1, 0
    while not d % 2:
        d, s = d >> 1, s + 1

    def try_composite(a):
        if pow(a, d, n) == 1:
            return False
        for i in range(s):
            if pow(a, 2**i * d, n) == n - 1:
                return False
        return True

    return not any(try_composite(w) for w in [2, 325, 9375, 28178, 450775, 9780504, 1795265022])


def factors(n):
    prime_factors = Counter()

    def ilog(n, p):
        cnt = 0
        while not n % p:
            n, cnt = n // p, cnt + 1
        return n, cnt

    if n % 2 == 0:
        n, prime_factors[2] = ilog(n, 2)
    if n % 3 == 0:
        n, prime_factors[3] = ilog(n, 3)

    i = 5
    while i * i <= n:
        if n % i == 0:
            n, prime_factors[i] = ilog(n, i)
        i += 2 if i % 3 == 2 else 4

    if n > 1:
        prime_factors[n] = 1
    return prime_factors


def perfect_base(n):
    b = n.bit_length()
    for a in range(b, 0, -1):
        lo, hi = 1, 1 << (b//a + 1)
        while lo < hi:
            mi = (lo + hi) // 2

            a_b = mi**a
            if a_b == n:
                return mi

            if a_b > n:
                hi = mi
            else:
                lo = mi + 1


def primitive_root(p):
    if p == 4:
        return 3
    if -p & p == p:
        return None

    factor = perfect_base(p if p & 1 else p >> 1)
    if not is_prime(factor):
        return None

    phi = (factor - 1) * ((p if p & 1 else p >> 1) // factor)

    for res in range(2 + (1 ^ (p & 1)), factor, 1 + (1 ^ (p & 1))):
        if all(pow(res, phi // i, p) != 1 for i in factors(phi).keys()):
            return res
