class LazySegmentTree:
    """Lazy segment tree whose update and merge operations can be specialized."""

    def __init__(self, data, default=0, func=max):
        """initialize the lazy segment tree with data"""
        self._default = default
        self._func = func

        self._len = len(data)
        self._size = _size = 1 << (self._len - 1).bit_length()
        self._buffer_idx = 2 * _size

        # Replace these arrays and the four methods below for custom operations.
        self._lazy = [0] * (2 * _size + 1)
        self.data = [default] * (2 * _size + 1)
        self.data[_size:_size + self._len] = data
        for i in range(_size - 1, 0, -1):
            self._merge_data(i + i, i + i + 1, i)

    def __len__(self):
        return self._len

    def _get_range(self, idx):
        """return the leaf range represented by idx"""
        shift = self._size.bit_length() - idx.bit_length()
        return idx << shift, (idx + 1) << shift

    def _unset_lazy(self, idx):
        """clear the lazy update at idx"""
        self._lazy[idx] = 0

    def _apply_to_data(self, update_idx, data_idx):
        """apply the lazy update at update_idx to data_idx"""
        self.data[data_idx] += self._lazy[update_idx]

    def _apply_to_lazy(self, update_idx, lazy_idx):
        """compose the update at update_idx into lazy_idx"""
        self._lazy[lazy_idx] += self._lazy[update_idx]

    def _merge_data(self, left, right, target):
        """merge the data at left and right into target"""
        self.data[target] = self._func(self.data[left], self.data[right])

    def _update(self, idx):
        """apply all updates stored above idx"""
        for i in range(idx.bit_length() - 1, 0, -1):
            parent = idx >> i
            left = parent + parent
            self._apply_to_data(parent, left)
            self._apply_to_lazy(parent, left)
            self._apply_to_data(parent, left + 1)
            self._apply_to_lazy(parent, left + 1)
            self._unset_lazy(parent)

    def _build(self, idx):
        """make the changes to idx known to its ancestors"""
        idx >>= 1
        while idx:
            self._merge_data(idx + idx, idx + idx + 1, idx)
            self._apply_to_data(idx, idx)
            idx >>= 1

    def apply(self, start, stop, value):
        """lazily apply value to [start, stop)"""
        start = start_copy = start + self._size
        stop = stop_copy = stop + self._size
        buffer_idx = self._buffer_idx
        self._lazy[buffer_idx] = value

        while start < stop:
            if start & 1:
                self._apply_to_lazy(buffer_idx, start)
                self._apply_to_data(buffer_idx, start)
                start += 1
            if stop & 1:
                stop -= 1
                self._apply_to_lazy(buffer_idx, stop)
                self._apply_to_data(buffer_idx, stop)
            start >>= 1
            stop >>= 1

        # Tell all nodes above the updated area of the updates.
        self._build(start_copy)
        self._build(stop_copy - 1)

    add = apply

    def query(self, start, stop, default=0):
        """return func(data[start:stop])"""
        start += self._size
        stop += self._size

        # Apply all the lazily stored updates.
        self._update(start)
        self._update(stop - 1)

        buffer_idx = self._buffer_idx
        self.data[buffer_idx] = default
        while start < stop:
            if start & 1:
                self._merge_data(buffer_idx, start, buffer_idx)
                start += 1
            if stop & 1:
                stop -= 1
                self._merge_data(buffer_idx, stop, buffer_idx)
            start >>= 1
            stop >>= 1
        return self.data[buffer_idx]

    def __repr__(self):
        return "LazySegmentTree({0})".format(self.data)
