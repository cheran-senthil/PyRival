from operator import rshift


def get_primes(n):
    """ Input n>=6, Returns a list of primes, 2 <= p < n """
    m = (n+1) + 6 - ((n+1) % 6)
    sieve = bytearray(rshift(m//3, 3) + 1)

    for i in range(1, int(m**0.5) // 3 + 1):
        if not rshift(sieve[rshift(i, 3)], (i & 0b111)) & 1:
            k = (3 * i + 1) | 1
            for j in range(k * k // 3, m // 3, 2 * k): sieve[rshift(j, 3)] |= 1 << (j & 0b111)
            for j in range(k * (k - 2 * (i & 1) + 4) // 3, m // 3, 2 * k): sieve[rshift(j, 3)] |= 1 << (j & 0b111)
    
    return (3*i + 1|1 for i in range(1, m // 3 - (n % 6 > 1)) if not rshift(sieve[rshift(i, 3)], (i & 0b111)) & 1)