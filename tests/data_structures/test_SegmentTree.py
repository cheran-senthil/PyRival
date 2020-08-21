import operator as op
import random

import pytest
from pyrival.SegmentTree import *

params = [
    (float('inf'), min),
    (float('-inf'), max),
    (0, op.add),
    (0, lambda a, b: int(str(abs(a)) + (str(abs(b)) if b else ""))),
]


@pytest.mark.parametrize("default,func", params)
def test_SegmentTree(default, func):
    for _ in range(1000):
        l = random.randint(2, 100)

        arr = [random.randint(-1000, 1000) for _ in range(l)]
        seg_tree = SegmentTree(arr, default, func)

        q = random.randint(0, 100)
        for _ in range(q):
            t = random.randrange(0, 2)

            if t == 0:
                start = random.randrange(0, l)
                stop = random.randrange(start, l)

                m = default
                for i in range(start, stop):
                    m = func(m, arr[i])

                assert seg_tree.query(start, stop) == m
            else:
                idx = random.randrange(0, l)
                seg_tree[idx] = arr[idx] = random.randint(-1000, 1000)
