import random

import pyrival.algebra


def test_chinese_remainder(primes):
    for _ in range(1000):
        l = random.randint(2, 100)
        p = random.sample(primes, l)
        a = [random.randint(0, 10000) % p[i] for i in range(l)]
        x = pyrival.algebra.chinese_remainder(a, p)
        assert [x % i for i in p] == a


def test_composite_crt(primes):
    for _ in range(1000):
        l = random.randint(2, 100)
        p = random.sample(primes, l)
        a = [random.randint(0, 10000) % p[i] for i in range(l)]
        x = pyrival.algebra.composite_crt(a, p)
        assert [x % i for i in p] == a
