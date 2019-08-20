class SortedList:
    def __init__(self, iterable=[], _load=200):
        """Initialize sorted list instance."""
        values = sorted(iterable)
        self._len = _len = len(values)
        self._load = _load
        self._lists = _lists = [values[i:i + _load] for i in range(0, _len, _load)]
        self._mins = [_list[0] for _list in _lists]
        self._list_lens = [len(_list) for _list in _lists]
        self._fen_tree = []
        self._rebuild = True

    def _fen_init(self):
        """Initialize a fenwick tree instance."""
        self._rebuild = False
        self._fen_tree[:] = self._list_lens
        for i in range(len(self._fen_tree)):
            if i | i + 1 < len(self._fen_tree):
                self._fen_tree[i | i + 1] += self._fen_tree[i]

    def _fen_update(self, index, value):
        """Update `fen_tree[index] += value`."""
        if not self._rebuild:
            while index < len(self._fen_tree):
                self._fen_tree[index] += value
                index |= index + 1

    def _fen_query(self, end):
        """Return `sum(_fen_tree[:end])`."""
        if self._rebuild:
            self._fen_init()

        x = 0
        while end:
            x += self._fen_tree[end - 1]
            end &= end - 1
        return x

    def _fen_findkth(self, k):
        """Return a pair of (the largest `idx` such that `sum(_fen_tree[:idx]) <= k`, `k - sum(_fen_tree[:idx])`)."""
        if k < self._list_lens[0]:
            return 0, k
        if k >= self._len - self._list_lens[-1]:
            return len(self._list_lens) - 1, self._list_lens[-1] - 1
        if self._rebuild:
            self._fen_init()

        idx = -1
        for d in reversed(range(len(self._fen_tree).bit_length())):
            right_idx = idx + (1 << d)
            if right_idx < len(self._fen_tree) and k >= self._fen_tree[right_idx]:
                idx = right_idx
                k -= self._fen_tree[idx]
        return idx + 1, k

    def _delete(self, pos, idx):
        """Delete value at the given `(pos, idx)`."""
        del self._lists[pos][idx]
        self._len -= 1
        self._list_lens[pos] -= 1
        self._fen_update(pos, -1)
        if self._list_lens[pos]:
            self._mins[pos] = self._lists[pos][0]
        else:
            del self._lists[pos]
            del self._mins[pos]
            del self._list_lens[pos]
            self._rebuild = True

    def _loc_left(self, value):
        """Return an index pair that corresponds to the first position of `value` in the sorted list."""
        if not self._len:
            return 0, 0

        _lists = self._lists
        _mins = self._mins
        pos, hi = 1, len(_lists)
        while pos < hi:
            mi = (pos + hi) >> 1
            if _mins[mi] <= value:
                pos = mi + 1
            else:
                hi = mi

        pos -= 1
        _list = _lists[pos]
        lo, idx = -1, len(_list)
        while lo + 1 < idx:
            mi = (lo + idx) >> 1
            if value <= _list[mi]:
                idx = mi
            else:
                lo = mi

        return pos, idx

    def _loc_right(self, value):
        """Return an index pair that corresponds to the last position of `value` in the sorted list."""
        if not self._len:
            return 0, 0

        _lists = self._lists
        _mins = self._mins
        pos, hi = 1, len(_lists)
        while pos < hi:
            mi = (pos + hi) >> 1
            if _mins[mi] <= value:
                pos = mi + 1
            else:
                hi = mi

        pos -= 1
        _list = _lists[pos]
        lo, idx = -1, len(_list)
        while lo + 1 < idx:
            mi = (lo + idx) >> 1
            if value < _list[mi]:
                idx = mi
            else:
                lo = mi

        return pos, idx

    def add(self, value):
        """Add `value` to sorted list."""
        _load = self._load
        _lists = self._lists
        _mins = self._mins
        _list_lens = self._list_lens

        self._len += 1
        if _lists:
            pos, idx = self._loc_right(value)
            _lists[pos].insert(idx, value)
            _list_lens[pos] += 1
            _mins[pos] = _lists[pos][0]

            self._fen_update(pos, 1)
            if _load + _load < len(_lists[pos]):
                _lists.insert(pos + 1, _lists[pos][_load:])
                _mins.insert(pos + 1, _lists[pos][_load])
                _list_lens.insert(pos + 1, len(_lists[pos]) - _load)
                _list_lens[pos] = _load
                del _lists[pos][_load:]
                self._rebuild = True
        else:
            _lists.append([value])
            _list_lens.append(1)
            _mins.append(value)
            self._rebuild = True

    def discard(self, value):
        """Remove `value` from sorted list if it is a member."""
        _lists = self._lists
        if _lists:
            pos, idx = self._loc_right(value)
            if idx and _lists[pos][idx - 1] == value:
                self._delete(pos, idx)

    def remove(self, value):
        """Remove `value` from sorted list; `value` must be a member."""
        _len = self._len
        self.discard(value)
        if _len == self._len:
            raise ValueError('{0!r} not in list'.format(value))

    def bisect_left(self, value):
        """Return the first index to insert `value` in the sorted list."""
        pos, idx = self._loc_left(value)
        return self._fen_query(pos) + idx

    def bisect_right(self, value):
        """Return the last index to insert `value` in the sorted list."""
        pos, idx = self._loc_right(value)
        return self._fen_query(pos) + idx

    def count(self, value):
        """Return number of occurrences of `value` in the sorted list."""
        return self.bisect_right(value) - self.bisect_left(value)

    def pop(self, index=-1):
        """Remove and return value at `index` in sorted list."""
        pos, idx = self._fen_findkth(index if 0 <= index else self._len - index)
        value = self._lists[pos][idx]
        self._delete(pos, idx)
        return value

    def __contains__(self, value):
        """Return true if `value` is an element of the sorted list."""
        _lists = self._lists
        pos, idx = self._loc_left(value)
        return _lists and idx < len(_lists[pos]) and _lists[pos][idx] == value

    def __getitem__(self, index):
        """Lookup value at `index` in sorted list."""
        pos, idx = self._fen_findkth(index if 0 <= index else self._len - index)
        return self._lists[pos][idx]

    def __delitem__(self, index):
        """Remove value at `index` from sorted list."""
        pos, idx = self._fen_findkth(index if 0 <= index else self._len - index)
        self._delete(pos, idx)

    def __len__(self):
        """Return the size of the sorted list."""
        return self._len

    def __iter__(self):
        """Return an iterator over the sorted list."""
        return (value for _list in self._lists for value in _list)

    def __reversed__(self):
        """Return a reverse iterator over the sorted list."""
        return (value for _list in self._lists[::-1] for value in _list[::-1])

    def __repr__(self):
        """Return string representation of sorted list."""
        return 'SortedList({0})'.format([value for _list in self._lists for value in _list])
