from math import gcd

mat_sub = lambda A, B: [[i - j for i, j in zip(*row)] for row in zip(A, B)]

mat_mul = lambda A, B: [[sum(i * j for i, j in zip(row, col)) for col in zip(*B)] for row in A]


def egcd(a, m):
    """extended gcd"""
    if not a:
        return m, 0, 1
    g, y, x = egcd(m % a, a)
    return g, x - (m // a) * y, y


def modinv(a, m):
    """returns the modular inverse of a w.r.t. to m"""
    amodm = a % m
    g, x, _ = egcd(amodm, m)
    return x % m if g == 1 else None


def pivot(A, m):
    """returns the pivot of A and m"""
    result = [0] * len(A)
    for i, Ai in enumerate(A):
        for j, Aij in enumerate(Ai):
            if gcd(Aij, m[i]) == 1:
                result[i] = j
    return result


def is_sol(A, x, b, m):
    """checks if Ax = b mod m"""
    ax_b = mat_sub(mat_mul(A, x), b)
    for i, mod in enumerate(m):
        if ax_b[i] % mod:
            return False
    return True


def mcrt(A, b, m):
    """returns x s.t. Ax = b mod m"""
    piv = pivot(A, m)
    x = [0] * len(A)
    m_prod = 1
    for i, Ai in enumerate(A):
        tot = sum(Ai[k] * x[k] for k in range(len(A)))
        tmp = (modinv(m_prod * Ai[piv[i]], m[i]) * (b[i] - tot)) % m[i]
        x[piv[i]] += tmp * m_prod
        m_prod *= m[i]
    return x
