import random

import pyrival.misc


def test_order_statistic():
    for _ in range(1000):
        arr = [random.randint(-100, 100) for _ in range(random.randint(0, 100))]
        sor = sorted(arr)

        for i in range(len(arr)):
            assert pyrival.misc.order_statistic(arr, i) == sor[i]
