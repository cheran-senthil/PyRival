import random

import pytest

from pyrival.data_structures.LazySegmentTree import LazySegmentTree


@pytest.mark.parametrize("default,func", [(float("inf"), min), (float("-inf"), max)])
def test_LazySegmentTree(default, func):
    rng = random.Random(0)

    for _ in range(100):
        n = rng.randint(1, 100)
        values = [rng.randint(-1000, 1000) for _ in range(n)]
        tree = LazySegmentTree(values, default, func)

        for _ in range(100):
            start = rng.randrange(n)
            stop = rng.randrange(start + 1, n + 1)
            if rng.randrange(2):
                value = rng.randint(-1000, 1000)
                tree.add(start, stop, value)
                for i in range(start, stop):
                    values[i] += value
            else:
                assert tree.query(start, stop, default) == func(values[start:stop])


class MinCountTree(LazySegmentTree):
    """Example specialization: range chmin with counts, point query."""

    INF = 10**9

    def __init__(self, n):
        super().__init__([(self.INF, 0)] * n, (self.INF, 0), self._merge)
        self._lazy = [(self.INF, 0)] * len(self._lazy)

    @staticmethod
    def _merge(a, b):
        if a[0] < b[0]:
            return a
        if b[0] < a[0]:
            return b
        return a[0], a[1] + b[1]

    def _unset_lazy(self, idx):
        self._lazy[idx] = self.INF, 0

    def _apply_to_data(self, update_idx, data_idx):
        self.data[data_idx] = self._merge(self._lazy[update_idx], self.data[data_idx])

    def _apply_to_lazy(self, update_idx, lazy_idx):
        self._lazy[lazy_idx] = self._merge(self._lazy[update_idx], self._lazy[lazy_idx])

    def apply(self, start, stop, minimum, count):
        super().apply(start, stop, (minimum, count))


def test_LazySegmentTree_custom_min_count():
    rng = random.Random(1)
    n = 100
    expected = [(MinCountTree.INF, 0) for _ in range(n)]
    tree = MinCountTree(n)

    for _ in range(1000):
        start = rng.randrange(n)
        stop = rng.randrange(start + 1, n + 1)
        minimum = rng.randrange(20)
        count = rng.randrange(1, 20)
        tree.apply(start, stop, minimum, count)

        for i in range(start, stop):
            expected[i] = tree._merge(expected[i], (minimum, count))

        idx = rng.randrange(n)
        assert tree.query(idx, idx + 1, (MinCountTree.INF, 0)) == expected[idx]
