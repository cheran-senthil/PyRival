def mod_sqrt(a, p):
    """returns x s.t. x**2 == a (mod p)"""
    a %= p
    if a == 0:
        return 0
    assert pow(a, (p - 1) // 2, p) == 1
    if p & 3 == 3:
        return pow(a, (p + 1) // 4, p)

    r = ((p - 1) & (1 - p)).bit_length() - 1
    s, n = p >> r, 2
    while pow(n, (p - 1) // 2, p) != p - 1:
        n += 1

    x, b, g = pow(a, (s + 1) // 2, p), pow(a, s, p), pow(n, s, p)
    while True:
        t = b
        for m in range(r):
            if t == 1:
                break
            t = (t * t) % p
        if m == 0:
            return x

        gs = pow(g, 1 << (r - m - 1), p)
        g, x = (gs * gs) % p, (x * gs) % p
        b, r = (b * g) % p, m
