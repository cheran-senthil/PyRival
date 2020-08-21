import math
import random

from pyrival.gcd import *


def test_gcd():
    for _ in range(10000):
        x, y = random.randint(1, 1000), random.randint(1, 1000)
        assert gcd(x, y) == math.gcd(x, y)


def test_extended_gcd():
    for _ in range(10000):
        x, y = random.randint(1, 1000), random.randint(1, 1000)
        g, s, r = extended_gcd(x, y)

        assert g == math.gcd(x, y)
        assert s * x + r * y == g


def test_lcm():
    for _ in range(10000):
        x, y = random.randint(1, 1000), random.randint(1, 1000)
        assert lcm(x, y) == x * y // math.gcd(x, y)
