from bisect import bisect_left, bisect_right
from functools import reduce


class SortedList:
    def __init__(self, iterable=[], _load=200):
        """Initialize sorted list instance."""
        values = sorted(iterable)
        self._len = _len = len(values)
        self._lists = [values[i:i + _load] for i in range(0, _len, _load)]
        self._load = _load
        self._bit_build()

    def _bit_build(self):
        """Build a bit instance."""
        self.bit = bit = [len(chunk) for chunk in self._lists]
        for i in range(len(bit)):
            j = i | (i + 1)
            if j < len(bit):
                bit[j] += bit[i]

    def _bit_update(self, idx, flag=False):
        """Update the bit at `idx`."""
        bit = self.bit
        while idx < len(bit):
            bit[idx] += flag
            idx |= idx + 1

    def _bit_query(self, end):
        """Return `sum(bit[:end])`."""
        bit = self.bit
        x = 0
        while end:
            x += bit[end - 1]
            end &= end - 1

        return x

    def _bit_find(self, k):
        """Return largest index such that `sum(bit[:idx]) <= k`, and `k - sum(bit[:idx])`."""
        bit = self.bit
        idx = -1
        for d in reversed(range(len(bit).bit_length())):
            right_idx = idx + (1 << d)
            if right_idx < len(bit) and k >= bit[right_idx]:
                idx = right_idx
                k -= bit[idx]

        return idx + 1, k

    def _loc(self, value, left=False):
        """Return an index pair that corresponds to the first position of `value` in the sorted list."""
        _lists = self._lists
        if not _lists:
            return 0, 0

        lo, hi = 1, len(_lists)
        while lo < hi:
            mi = (lo + hi) >> 1
            if _lists[mi][0] <= value:
                lo = mi + 1
            else:
                hi = mi

        return lo - 1, bisect_left(_lists[lo - 1], value) if left else bisect_right(_lists[lo - 1], value)

    def bisect_left(self, value):
        """Return an index to insert `value` in the sorted list."""
        i, j = self._loc(value, left=True)
        return self._bit_query(i) + j

    def bisect_right(self, value):
        """Return an index to insert `value` in the sorted list."""
        i, j = self._loc(value)
        return self._bit_query(i) + j

    def add(self, value):
        """Add `value` to sorted-key list."""
        _lists = self._lists
        _load = self._load
        self._len += 1
        if _lists:
            i, j = self._loc(value, left=True)
            _lists[i].insert(j, value)
            self._bit_update(i, flag=True)
            if _load + _load < len(_lists[i]):
                _lists.insert(i + 1, _lists[i][_load:])
                _lists[i][_load:] = []
                self._bit_build()
        else:
            _lists.append([value])
            self.bit = [1]

    def discard(self, value):
        """Remove `value` from sorted list if it is a member."""
        _lists = self._lists
        if _lists:
            i, j = self._loc(value, left=True)
            if _lists[i][j] == value:
                del _lists[i][j]
                self._len -= 1
                self._bit_update(i)

    def remove(self, value):
        """Remove `value` from sorted list; `value` must be a member."""
        _len = self._len
        self.discard(value)
        if _len == self._len:
            raise ValueError('{0!r} not in list'.format(value))

    def __contains__(self, value):
        """Return true if `value` is an element of the sorted list."""
        _lists = self._lists
        i, j = self._loc(value, left=True)
        return _lists and j < len(_lists[i]) and _lists[i][j] == value

    def __getitem__(self, i):
        """Lookup value at `index` in sorted list."""
        i, j = self._bit_find(i)
        return self._lists[i][j]

    def __len__(self):
        """Return the size of the sorted list."""
        return self._len

    def __repr__(self):
        """Return string representation of sorted list."""
        return 'SortedList({0})'.format(reduce(list.__iadd__, self._lists, []))
