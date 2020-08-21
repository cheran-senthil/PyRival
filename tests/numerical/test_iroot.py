import random

from pyrival.iroot import *


def test_iroot():
    for _ in range(10000):
        k = random.randint(1, 10)
        n = random.randint(-10000 if k & 1 else 0, 10000)
        root = iroot(n, k)

        if root < 0:
            assert (root - 1)**k < n <= root**k
        else:
            assert root**k <= n < (root + 1)**k
