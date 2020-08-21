import random

from pyrival.chinese_remainder import *


def test_chinese_remainder(primes):
    for _ in range(1000):
        l = random.randint(2, 100)
        p = random.sample(primes, l)
        a = [random.randint(0, p[i] - 1) for i in range(l)]
        x = chinese_remainder(a, p)
        assert [x % i for i in p] == a


def test_composite_crt():
    for _ in range(1000):
        l = random.randint(2, 100)
        s = random.randint(0, 10000)
        m = [random.randint(2, 10000) for _ in range(l)]
        a = [s % m[i] for i in range(l)]
        x = composite_crt(a, m)
        assert [x % i for i in m] == a
