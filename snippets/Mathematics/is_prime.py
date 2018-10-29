def _try_composite(a, d, n, s):
    if pow(a, d, n) == 1:
        return False
    for i in range(s):
        if pow(a, 2**i * d, n) == n - 1:
            return False
    return True


def is_prime(n):
    """
    Deterministic variant of the Miller-Rabin primality test to determine
    whether a given number is prime.

    Parameters
    ----------
    n : int
        n >= 0, an integer to be tested for primality.

    Returns
    -------
    bool
        False if n is composite, otherwise True.
    """
    if n in [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37]:
        return True

    if (any((n % p) == 0 for p in [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37])) or (n in [0, 1]):
        return False

    d, s = n - 1, 0
    while not d % 2:
        d, s = d >> 1, s + 1

    if n < 2047:
        return not _try_composite(2, d, n, s)
    if n < 1373653:
        return not any(_try_composite(a, d, n, s) for a in [2, 3])
    if n < 25326001:
        return not any(_try_composite(a, d, n, s) for a in [2, 3, 5])
    if n < 118670087467:
        if n == 3215031751:
            return False
        return not any(_try_composite(a, d, n, s) for a in [2, 3, 5, 7])
    if n < 2152302898747:
        return not any(_try_composite(a, d, n, s) for a in [2, 3, 5, 7, 11])
    if n < 3474749660383:
        return not any(_try_composite(a, d, n, s) for a in [2, 3, 5, 7, 11, 13])
    if n < 341550071728321:
        return not any(_try_composite(a, d, n, s) for a in [2, 3, 5, 7, 11, 13, 17])
    if n < 3825123056546413051:
        return not any(_try_composite(a, d, n, s) for a in [2, 3, 5, 7, 11, 13, 17, 19, 23])
    return not any(_try_composite(a, d, n, s) for a in [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37])
