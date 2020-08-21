import random

from pyrival.ordersort import *


def test_ordersort():
    for _ in range(10000):
        l = random.randint(1, 100)

        arr = [random.randint(0, 1000) for _ in range(l)]

        got = ordersort(range(l), arr)
        expected = sorted(range(l), key=arr.__getitem__)

        assert [arr[i] for i in got] == [arr[i] for i in expected]


def test_ordersort_reverse():
    for _ in range(10000):
        l = random.randint(1, 100)

        arr = [random.randint(0, 1000) for _ in range(l)]

        got = ordersort(range(l), arr, reverse=True)
        expected = sorted(range(l), key=arr.__getitem__, reverse=True)

        assert [arr[i] for i in got] == [arr[i] for i in expected]


def test_multikey_ordersort():
    for _ in range(10000):
        l = random.randint(1, 100)
        t = random.randint(0, 4)

        arr = [[random.randint(0, 1000) for _ in range(t)] for _ in range(l)]

        got = multikey_ordersort(range(l), *zip(*arr))
        expected = sorted(range(l), key=arr.__getitem__)

        assert [arr[i] for i in got] == [arr[i] for i in expected]


def test_long_ordersort():
    for _ in range(1000):
        l = random.randint(1, 100)

        arr = [random.randint(0, 10**18) for _ in range(l)]

        got = long_ordersort(range(l), arr)
        expected = sorted(range(l), key=arr.__getitem__)

        assert [arr[i] for i in got] == [arr[i] for i in expected]
