import random
import math

import pyrival.algebra


def test_discrete_log():
    for _ in range(10000):
        m = random.randint(0, 100000)
        a = random.randint(0, m)
        while math.gcd(a, m) != 1:
            m = random.randint(0, 100000)
            a = random.randint(0, m)

        x = random.randint(0, 100000)
        b = pow(a, x, m)

        assert pow(a, pyrival.algebra.discrete_log(a, b, m), m) == b
