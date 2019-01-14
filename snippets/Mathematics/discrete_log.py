from math import gcd


def egcd(a, m):
    if a == 0:
        return (m, 0, 1)

    g, y, x = egcd(m % a, a)
    return (g, x - (m // a) * y, y)


def mod_inv(a, m):
    amodm = a % m
    g, x, _ = egcd(amodm, m)

    """Sanity Check
    if g != 1:
        return None
    """
    return x % m


def discrete_log(a, b, m):
    if a == 0:
        return 1

    g, x = gcd(a, m), 0
    while 1 not in [a, b, m, g]:
        m //= g
        b = (b // g) * mod_inv(a // g, m)
        g = gcd(a, m)
        x += 1

    if 1 in [a, b, m]:
        return x

    n = int(m**0.5) + 1

    an = 1
    for i in range(n):
        an = (an * a) % m

    vals = dict()

    cur = an
    for i in range(1, n + 1):
        if cur not in vals:
            vals[cur] = i
        cur = (cur * an) % m

    cur = b
    for i in range(n + 1):
        try:
            ans = vals[cur] * n - i
            if ans < m:
                return x + ans
        except KeyError:
            pass

        cur = (cur * a) % m

    return -1
