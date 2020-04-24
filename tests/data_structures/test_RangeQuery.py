import random

import pyrival.data_structures

import pytest

params = [
    (float('inf'), min),
    (float('-inf'), max),
]


@pytest.mark.parametrize("default,func", params)
def test_RangeQuery(default, func):
    for _ in range(1000):
        l = random.randint(2, 100)

        arr = [random.randint(-1000, 1000) for _ in range(l)]
        range_query = pyrival.data_structures.RangeQuery(arr, func)

        q = random.randint(0, 100)
        for _ in range(q):
            begin = random.randrange(0, l - 1)
            end = random.randrange(begin + 1, l)

            m = default
            for i in range(begin, end):
                m = func(m, arr[i])

            assert range_query.query(begin, end) == m
