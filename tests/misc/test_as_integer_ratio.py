import random

import pyrival.misc


def test_as_integer_ratio_0():
    num, den = pyrival.misc.as_integer_ratio(0, 53)
    assert abs(num / den) <= 1e-53


def test_as_integer_ratio():
    for _ in range(100000):
        number = (random.random() - 0.5) * 10000
        num, den = pyrival.misc.as_integer_ratio(number, 53)
        assert abs((num / den) - number) <= 1e-53
