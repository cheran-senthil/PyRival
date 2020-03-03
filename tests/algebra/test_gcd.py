import math
import random

import pyrival.algebra


def test_gcd():
    for _ in range(10000):
        x, y = random.randint(1, 1000), random.randint(1, 1000)
        assert pyrival.algebra.gcd(x, y) == math.gcd(x, y)


def test_extended_gcd():
    for _ in range(10000):
        x, y = random.randint(1, 1000), random.randint(1, 1000)
        g, s, r = pyrival.algebra.extended_gcd(x, y)

        assert g == math.gcd(x, y)
        assert s * x + r * y == g


def test_lcm():
    for _ in range(10000):
        x, y = random.randint(1, 1000), random.randint(1, 1000)
        assert pyrival.algebra.lcm(x, y) == x * y // math.gcd(x, y)
