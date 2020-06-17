import random

from pyrival.as_integer_ratio import *


def test_as_integer_ratio_0():
    num, den = as_integer_ratio(0, 53)
    assert abs(num / den) <= 1e-53


def test_as_integer_ratio():
    for _ in range(100000):
        number = (random.random() - 0.5) * 10000
        num, den = as_integer_ratio(number, 53)
        assert abs((num / den) - number) <= 1e-53
