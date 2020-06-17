import random

from pyrival.order_statistic import *


def test_order_statistic():
    for _ in range(1000):
        arr = [random.randint(-100, 100) for _ in range(random.randint(0, 100))]
        sor = sorted(arr)

        for i in range(len(arr)):
            assert order_statistic(arr, i) == sor[i]
