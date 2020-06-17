import random

from pyrival.discrete_log import *

# Good problem to test discrete log
# https://codeforces.com/gym/101853/problem/G


def test_discrete_log_corner_cases(limit=100):
    def brute(a, b, mod):
        e = 1
        for i in range(1, mod + 1):
            e = e * a % mod
            if (e == b):
                return i
        return None

    for a in range(limit):
        for b in range(limit):
            for m in range(1, limit):
                x = discrete_log(a, b, m)
                y = brute(a, b, m)
                assert x == y


def test_discrete_log_random_cases(trials=200):
    random.seed(666)

    for _ in range(trials):
        m = random.randint(0, 10**9)
        a = random.randint(0, 10**9)
        x = random.randint(0, 10**9)
        b = pow(a, x, m)

        y = pow(a, discrete_log(a, b, m), m)
        assert y == b
