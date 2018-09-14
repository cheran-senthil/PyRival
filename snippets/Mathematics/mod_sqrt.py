def mod_sqrt(n, p):
    if p == 2:
        return n % 2

    if pow(n, (p - 1) // 2, p) != 1:
        return None

    q = (p - 1) // ((p - 1) & (1 - p))
    s = ((p - 1) & (1 - p)).bit_length() - 1

    if s == 1:
        r = pow(n, (p + 1) // 4, p)
        return r, p - r

    z = next(i for i in range(2, p) if pow(i, (p - 1) // 2, p) == p - 1)

    c = pow(z, q, p)
    r = pow(n, (q + 1) // 2, p)
    t = pow(n, q, p)

    m, t2 = s, 0

    while (t - 1) % p != 0:
        t2 = (t * t) % p

        for i in range(1, m):
            if (t2 - 1) % p == 0:
                break

            t2 = (t2 * t2) % p

        b = pow(c, 1 << (m - i - 1), p)

        r = (r * b) % p
        c = (b * b) % p
        t = (t * c) % p

        m = i

    return r, p - r
