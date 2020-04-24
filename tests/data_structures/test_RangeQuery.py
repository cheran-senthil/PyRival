import random

import pyrival.data_structures


def test_RangeQuery_min():
    for _ in range(1000):
        l = random.randint(2, 100)

        arr = [random.randint(-1000, 1000) for _ in range(l)]
        rangeQuery = pyrival.data_structures.RangeQuery(arr, min)

        q = random.randint(0, 100)
        for _ in range(q):
            begin = random.randrange(0, l - 1)
            end = random.randrange(begin + 1, l)

            m = float('inf')
            for i in range(begin, end):
                m = min(m, arr[i])

            assert rangeQuery.query(begin, end) == m


def test_RangeQuery_max():
    for _ in range(1000):
        l = random.randint(2, 100)

        arr = [random.randint(-1000, 1000) for _ in range(l)]
        rangeQuery = pyrival.data_structures.RangeQuery(arr, max)

        q = random.randint(0, 100)
        for _ in range(q):
            begin = random.randrange(0, l - 1)
            end = random.randrange(begin + 1, l)

            m = float('-inf')
            for i in range(begin, end):
                m = max(m, arr[i])

            assert rangeQuery.query(begin, end) == m
