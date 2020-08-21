import random

import pytest
from pyrival.RangeQuery import *

params = [
    (float('inf'), min),
    (float('-inf'), max),
]


@pytest.mark.parametrize("default,func", params)
def test_RangeQuery(default, func):
    for _ in range(1000):
        l = random.randint(2, 100)

        arr = [random.randint(-1000, 1000) for _ in range(l)]
        range_query = RangeQuery(arr, func)

        q = random.randint(0, 100)
        for _ in range(q):
            start = random.randrange(0, l)
            stop = random.randrange(start + 1, l + 1)

            m = default
            for i in range(start, stop):
                m = func(m, arr[i])

            assert range_query.query(start, stop) == m
