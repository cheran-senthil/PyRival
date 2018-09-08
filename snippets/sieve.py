from math import sqrt
from itertools import compress

def get_primes(n):
    sieve = bytearray([True]) * (n//2 + 1)
    for i in range(1, int(sqrt(n))//2 + 1):
        if sieve[i]:
            sieve[2*i*(i+1)::2*i + 1] = bytearray((n//2 - 2*i*(i+1))//(2*i + 1) + 1)
    return compress(range(3, n + 1, 2), sieve[1:])