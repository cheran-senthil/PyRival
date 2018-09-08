from math import sqrt

def primes_less_than(n):
    if n < 4:
        return range(2, n + 1)
    
    sieve = [False] * (n + 1)
    sieve[2:4] = (True, True)

    sqrt_n = int(sqrt(n))

    for x in range(1, sqrt_n):
        for y in range(1, sqrt_n):
            x2 = x * x
            y2 = y * y

            i = 4 * x2 + y2
            if (i <= n) and (i % 12 in (1, 5)): sieve[i] = not sieve[i]

            i = 3 * x2 + y2
            if (i <= n) and (i % 12 == 7): sieve[i] = not sieve[i]

            i = 3 * x2 - y2
            if (x > y) and (i <= n) and (i % 12 == 11): sieve[i] = not sieve[i]


    for p in range(5, sqrt_n):
        if sieve[p]:
            for i in range(p * p, n + 1, p * p):
                sieve[i] = False

    return (i for i, p in enumerate(sieve) if p)