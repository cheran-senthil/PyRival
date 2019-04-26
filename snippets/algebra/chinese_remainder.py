import operator as op
from functools import reduce


def chinese_remainder(a, p):
    """returns x s.t. x = a[i] (mod p[i]) where p[i] is prime for all i"""
    prod = reduce(op.mul, p, 1)
    x = [prod // pi for pi in p]
    return sum(a[i] * pow(x[i], p[i] - 2, p[i]) * x[i] for i in range(len(a))) % prod


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
    """returns the modular inverse of a w.r.t. to m"""
    g, x, _ = extended_gcd(a % m, m)
    return x % m if g == 1 else None


def composite_crt(b, m):
    """returns x s.t. x = a[i] (mod m[i]) for all i"""
    x, m_prod = 0, 1
    for bi, mi in zip(b, m):
        x += ((modinv(m_prod, mi) * (bi - x)) % mi) * m_prod
        m_prod *= mi
    return x % m_prod
