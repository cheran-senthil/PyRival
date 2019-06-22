class LazySegmentTree:
    def __init__(self, data, default=0, func=max):
        """maximum segment tree"""
        self._len = _len = len(data)
        self._size = _size = 1 << (_len - 1).bit_length()
        self._data = _data = [default] * (2 * _size)
        self._lazy = [0] * (2 * _size)
        self._default = default
        self._func = func

        _data[_size:_size + _len] = data
        for i in reversed(range(_size)):
            _data[i] = func(_data[i + i], _data[i + i + 1])

    def __len__(self):
        return self._len

    def _push(self, idx):
        """push query on idx to its children"""
        # Let the children know of the queries
        q = self._lazy[idx]

        self._data[2 * idx] += q
        self._data[2 * idx + 1] += q
        self._lazy[2 * idx] += q
        self._lazy[2 * idx + 1] += q

        # Remove queries from idx
        self._data[idx] = self._func(self._data[2 * idx], self._data[2 * idx + 1])
        self._lazy[idx] = 0

    def _update(self, idx):
        """updates the node idx to know of all queries applied to it via its ancestors"""
        # Find all indecies to be updated
        idx >>= 1
        to_update = []
        while idx > 0:
            to_update.append(idx)
            idx >>= 1

        # Push the queries down the segment tree
        to_update.reverse()
        while to_update:
            self._push(to_update.pop())

    def _build(self, idx):
        """make the changes to idx be known to its ancestors"""
        idx >>= 1
        while idx > 0:
            self._data[idx] = self._func(self._data[2 * idx], self._data[2 * idx + 1]) + self._lazy[idx]
            idx >>= 1

    def add(self, start, stop, value):
        """lazily add value to [start, stop)"""
        start += self._size
        stop += self._size

        _start, _stop = start, stop
        while _start < _stop:
            if _start & 1:
                self._lazy[_start] += value
                self._data[_start] += value
                _start += 1
            if _stop & 1:
                _stop -= 1
                self._lazy[_stop] += value
                self._data[_stop] += value
            _start >>= 1
            _stop >>= 1

        # Tell all nodes above of the updated area of the updates
        self._build(start)
        self._build(stop - 1)

    def bisect(self, value, cmp):
        if not cmp(value, self._data[1]):
            return -1

        idx = 1
        while idx < self._size:
            self._push(idx)
            idx <<= 1
            if cmp(value, self._data[idx + 1]):
                idx += 1
        return idx - self._size

    def query(self, start, stop, default=0):
        """func of data[start, stop)"""
        start += self._size
        stop += self._size

        # Apply all the lazily stored queries
        self._update(start)
        self._update(stop - 1)

        res = default
        while start < stop:
            if start & 1:
                res = self._func(res, self._data[start])
                start += 1
            if stop & 1:
                stop -= 1
                res = self._func(res, self._data[stop])
            start >>= 1
            stop >>= 1
        return res
