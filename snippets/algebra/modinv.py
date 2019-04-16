def egcd(a, m):
    if a == 0:
        return (m, 0, 1)

    g, y, x = egcd(m % a, a)
    return (g, x - (m // a) * y, y)


def modinv(a, m):
    g, x, _ = egcd(a % m, m)
    """Sanity Check
    if g != 1:
        return None
    """
    return x % m
