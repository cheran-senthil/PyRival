def is_prime(n):
    """ Deterministic variant of the Miller-Rabin primality test. """
    if n <= 1:
        return False

    for p in [2, 3, 5, 13, 19, 73, 193, 407521, 299210837]:
        if n % p == 0:
            return n == p

    d = n - 1
    while not d & 1:
        d >>= 1

    for a in [2, 325, 9375, 28178, 450775, 9780504, 1795265022]:
        p, i = pow(a, d, n), d
        while p != 1 and p != n - 1 and i != n - 1:
            i <<= 1
            p = (p * p) % n
        if p != n - 1 and i != d:
            return False

    return True
