import operator as op
from functools import reduce


def chinese_remainder(a, n):
    # solve for x = a_i (mod n_i) where n_i is prime
    x = 0
    prod = reduce(op.mul, n)

    for a_i, n_i in zip(a, n):
        p = prod // n_i
        x += a_i * pow(p, n_i - 2, n_i) * p

    return x % prod


def egcd(a, m):
    if a == 0:
        return (m, 0, 1)

    g, y, x = egcd(m % a, a)
    return (g, x - (m // a) * y, y)


def modinv(a, m):
    amodm = a % m
    g, x, _ = egcd(amodm, m)

    """Sanity Check
    if g != 1:
        return None
    """
    return x % m


def composite_crt(b, m):
    # solve for x = b_i (mod m_i)
    x = 0
    m_prod = 1

    for bi, mi in zip(b, m):
        tot = x
        tmp = (modinv(m_prod, mi) * (bi - tot)) % mi
        x += tmp * m_prod
        m_prod *= mi

    return x % m_prod
