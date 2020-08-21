import random

from pyrival.modinv import *


def test_modinv():
    for _ in range(10000):
        a = random.randint(1, 10000)
        assert (modinv(a, 10**8 + 7) * a) % (10**8 + 7) == 1
        assert (modinv(a, 10**9 + 7) * a) % (10**9 + 7) == 1
        assert (modinv(a, 10**9 + 9) * a) % (10**9 + 9) == 1
