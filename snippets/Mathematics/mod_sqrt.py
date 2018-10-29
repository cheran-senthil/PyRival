def mod_sqrt(n, p):
    """
    Uses the Tonelli-Shanks algorithm to solve for r in a congruence of the
    form r**2 = n (mod p), where p is prime.

    Parameters
    ----------
    n : int
        An element of (Z/pZ)**d such that solutions to the congruence r**2 = n exist.
    p : int
        A prime.

    Returns
    -------
    r, p - r : int, int
        r, p - r in (Z/pZ)**d such r**2 = (p - r)**2 = n
    """
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
