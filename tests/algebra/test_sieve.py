import pyrival.algebra


def test_prime_list(primes):
    assert primes == pyrival.algebra.prime_list(primes[-1])
