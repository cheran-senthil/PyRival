import random

import pyrival.misc


def test_ordersort():
    for _ in range(10000):
        l = random.randint(1, 100)

        arr = [random.randint(0, 1000) for _ in range(l)]

        got = pyrival.misc.ordersort(range(l), arr)
        expected = sorted(range(l), key=arr.__getitem__)

        assert [arr[i] for i in got] == [arr[i] for i in expected]


def test_ordersort_reverse():
    for _ in range(10000):
        l = random.randint(1, 100)

        arr = [random.randint(0, 1000) for _ in range(l)]

        got = pyrival.misc.ordersort(range(l), arr, reverse=True)
        expected = sorted(range(l), key=arr.__getitem__, reverse=True)

        assert [arr[i] for i in got] == [arr[i] for i in expected]
