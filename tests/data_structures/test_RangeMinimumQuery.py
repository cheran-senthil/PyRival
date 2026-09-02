import pytest
from pyrival.RangeMinimumQuery import *


def test_RangeQuery():
    for n in 1,2,3,4,5,6,7,8,9,10,200:
        for i in range(n):
            A = [-1] * n
            A[i] = -2
            RMQ1 = RangeMinimumQuery(A)
            RMQ2 = RangeMinimumQuery2(A)
            for l in range(n):
                for r in range(l + 1, n + 1):
                    if l <= i < r:
                        assert -2 == RMQ1.query(l, r) == RMQ2.query(l, r)
                    else:
                        assert -1 == RMQ1.query(l, r) == RMQ2.query(l, r)
