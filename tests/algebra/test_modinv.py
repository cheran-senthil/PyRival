import random

import pyrival.algebra


def test_modinv():
    for _ in range(10000):
        a = random.randint(1, 10000)
        assert (pyrival.algebra.modinv(a, 10**8 + 7) * a) % (10**8 + 7) == 1
        assert (pyrival.algebra.modinv(a, 10**9 + 7) * a) % (10**9 + 7) == 1
        assert (pyrival.algebra.modinv(a, 10**9 + 9) * a) % (10**9 + 9) == 1
