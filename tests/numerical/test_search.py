import random

import pyrival.numerical


def test_binary_search():
    for _ in range(10000):
        n = (random.random() * 2000) - 1000
        assert abs(pyrival.numerical.binary_search(n.__le__, -1000, 1000, 1e-7) - n) <= 1e-7


def test_ternary_search():
    for _ in range(10000):
        n = (random.random() * 2000) - 1000
        h = (random.random() * 2000) - 1000
        func = lambda x: h - abs(n - x)
        assert abs(pyrival.numerical.ternary_search(func, -1000, 1000, 1e-7) - n) <= 1e-7


def test_discrete_binary_search():
    for _ in range(10000):
        n = random.randint(-1000, 1000)
        assert pyrival.numerical.discrete_binary_search(n.__le__, -1000, 1000) == n


def test_discrete_ternary_search():
    for _ in range(10000):
        n = random.randint(-1000, 1000)
        h = random.randint(-1000, 1000)
        func = lambda x: h - abs(n - x)
        assert pyrival.numerical.discrete_ternary_search(func, -1000, 1000) == n
