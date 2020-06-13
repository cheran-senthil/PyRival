import random

from pyrival.factors import *


def test_pollard_rho():
    for _ in range(1000):
        n = random.randint(2, 10000)
        assert n % pollard_rho(n) == 0


def test_prime_factors(prime_set):
    for _ in range(1000):
        n = random.randint(1, 10000)
        for f, e in prime_factors(n).items():
            assert f in prime_set
            assert n % (f**e) == 0
            n //= f**e
        assert n == 1


def test_distinct_factors():
    for _ in range(1000):
        n = random.randint(1, 10000)
        factors = set(distinct_factors(n))
        for i in range(1, n + 1):
            assert (n % i == 0) == (i in factors)


def test_all_factors():
    for _ in range(1000):
        n = random.randint(1, 10000)
        factors = all_factors(n)
        assert factors == sorted(factors)
        factors = set(factors)
        for i in range(1, n + 1):
            assert (n % i == 0) == (i in factors)
