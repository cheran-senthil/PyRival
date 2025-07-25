class LazySegmentTree:
    def __init__(self, data):
        """initialize the lazy segment tree with data"""
        self._len = len(data)
        self._size = _size = 1 << (self._len - 1).bit_length()
        self._buffer_idx = 2 * _size

        self.lazy = [0] * (2 * _size + 1)
        self.data = [0] * (2 * _size + 1)
        self.data[_size:_size + self._len] = data
        for i in reversed(range(_size)):
            self._merge_data(i + i, i + i + 1, i)

    def __len__(self):
        return self._len

    def _get_range(self, a):
        shift = self._size.bit_length() - a.bit_length()
        return a << shift, (a << shift) + (1 << shift)

    def _unset_lazy(self, a):
        """a: lazy_idx; unset a"""
        self.lazy[a] = 0

    def _apply_to_data(self, a, b):
        """a: lazy_idx, b: data_idx; apply a to b"""
        l, r = self._get_range(b)
        self.data[b] += self.lazy[a] * (r - l)

    def _apply_to_lazy(self, a, b):
        """a: lazy_idx, b: lazy_idx; apply a to b"""
        self.lazy[b] += self.lazy[a]

    def _merge_data(self, a, b, c):
        """a: data_idx, b: data_idx, c: data_idx; merge a and b store result in c"""
        self.data[c] = self.data[a] + self.data[b]

    def _update(self, idx):
        """updates the node idx to know of all queries applied to it via its ancestors"""
        for i in reversed(range(1, idx.bit_length())):
            _idx = idx >> i
            self._apply_to_data(_idx, 2 * _idx)
            self._apply_to_lazy(_idx, 2 * _idx)
            self._apply_to_data(_idx, 2 * _idx + 1)
            self._apply_to_lazy(_idx, 2 * _idx + 1)
            self._unset_lazy(_idx)

    def _build(self, idx):
        """make the changes to idx be known to its ancestors"""
        idx >>= 1
        while idx:
            self._merge_data(2 * idx, 2 * idx + 1, idx)
            self._apply_to_data(idx, idx)
            idx >>= 1

    def apply(self, start, stop, value):
        """lazily apply value to [start, stop)"""
        start = start_copy = start + self._size
        stop = stop_copy = stop + self._size

        self.lazy[self._buffer_idx] = value

        while start < stop:
            if start & 1:
                self._apply_to_lazy(self._buffer_idx, start)
                self._apply_to_data(self._buffer_idx, start)
                start += 1
            if stop & 1:
                stop -= 1
                self._apply_to_lazy(self._buffer_idx, stop)
                self._apply_to_data(self._buffer_idx, stop)
            start >>= 1
            stop >>= 1

        # Tell all nodes above of the updated area of the updates
        self._build(start_copy)
        self._build(stop_copy - 1)

    def query(self, start, stop):
        """func of data[start, stop)"""
        start += self._size
        stop += self._size

        # Apply all the lazily stored queries
        self._update(start)
        self._update(stop - 1)

        self.data[self._buffer_idx] = 0

        while start < stop:
            if start & 1:
                self._merge_data(self._buffer_idx, start, self._buffer_idx)
                start += 1
            if stop & 1:
                stop -= 1
                self._merge_data(self._buffer_idx, stop, self._buffer_idx)
            start >>= 1
            stop >>= 1

        return self.data[self._buffer_idx]

    def __repr__(self):
        return "LazySegmentTree({0})".format(self.data)
