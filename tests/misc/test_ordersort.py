import random

import pyrival.misc


def test_ordersort():
    for _ in range(10000):
        l = random.randint(1, 100)

        r = list(range(l))
        arr = [random.randint(-1000, 1000) for _ in range(l)]

        got = pyrival.misc.ordersort(r, key=arr.__getitem__)
        expected = sorted(r, key=arr.__getitem__)

        for i, j in zip(got, expected):
            assert arr[i] == arr[j]


def test_ordersort_reverse():
    for _ in range(10000):
        l = random.randint(1, 100)

        r = list(range(l))
        arr = [random.randint(-1000, 1000) for _ in range(l)]

        got = pyrival.misc.ordersort(r, key=arr.__getitem__, reverse=True)
        expected = sorted(r, key=arr.__getitem__, reverse=True)

        for i, j in zip(got, expected):
            assert arr[i] == arr[j]
