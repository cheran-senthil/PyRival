from pyrival.sieve import *


def test_prime_list(primes):
    assert primes == prime_list(primes[-1])
