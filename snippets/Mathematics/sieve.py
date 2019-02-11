def get_primes(n):
    """ Input n>=6, Returns a generator of primes, 5 <= p < n """
    sieve = bytearray((n // 3 + (n % 6 == 2) >> 3) + 1)

    for i in range(1, int(n**0.5) // 3 + 1):
        if not (sieve[i >> 3] >> (i & 7)) & 1:
            k = (3 * i + 1) | 1
            for j in range(k * k // 3, n // 3 + (n % 6 == 2), 2 * k):
                sieve[j >> 3] |= 1 << (j & 7)
            for j in range(k * (k - 2 * (i & 1) + 4) // 3, n // 3 + (n % 6 == 2), 2 * k):
                sieve[j >> 3] |= 1 << (j & 7)

    return (3 * i + 1 | 1 for i in range(1, n // 3 + (n % 6 == 2)) if not (sieve[i >> 3] >> (i & 7)) & 1)
