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

    def push(self, seg_ind):
        """push query on seg_ind to its children"""
        # Let the children know of the queries
        q = self._lazy[seg_ind]

        self._lazy[2 * seg_ind] += q
        self._lazy[2 * seg_ind + 1] += q
        self._data[2 * seg_ind] += q
        self._data[2 * seg_ind + 1] += q

        # Remove queries from seg_ind
        self._data[seg_ind] = self._func(self._data[2 * seg_ind], self._data[2 * seg_ind + 1])
        self._lazy[seg_ind] = 0

    def update(self, seg_ind):
        """updates the node seg_ind to know of all queries applied to it via its ancestors"""
        # Find all indecies to be updated
        seg_ind >>= 1
        idxs = []
        while seg_ind > 0:
            idxs.append(seg_ind)
            seg_ind >>= 1

        # Push the queries down the segment tree
        idxs.reverse()
        while idxs:
            self.push(idxs.pop())

    def build(self, seg_ind):
        """make the changes to seg_ind be known to its ancestors"""
        seg_ind >>= 1
        while seg_ind > 0:
            self._data[seg_ind] = self._func(self._data[2 * seg_ind], self._data[2 * seg_ind + 1]) + self._lazy[seg_ind]
            seg_ind >>= 1

    def add(self, begin, end, value):
        """lazily add value to [begin, end)"""
        begin += self._size
        end += self._size
        _start, _end = begin, end

        while _start < _end:
            if _start & 1:
                self._lazy[_start] += value
                self._data[_start] += value
                _start += 1
            if _end & 1:
                _end -= 1
                self._lazy[_end] += value
                self._data[_end] += value
            _start >>= 1
            _end >>= 1

        # Tell all nodes above of the updated area of the updates
        self.build(begin)
        self.build(end - 1)

    def bisect(self, val, cmp):
        if not cmp(self._data[1], val):
            return -1

        idx = 1
        while idx < self._size:
            self.push(idx)
            idx <<= 1
            if cmp(self._data[idx + 1], val):
                idx += 1

        return idx - self._size

    def query(self, begin, end):
        """func of data[begin, end)"""
        begin += self._size
        end += self._size

        # Apply all the lazily stored queries
        self.update(begin)
        self.update(end - 1)
        res = self._default
        while begin < end:
            if begin & 1:
                res = self._func(res, self._data[begin])
                begin += 1
            if end & 1:
                end -= 1
                res = self._func(res, self._data[end])
            begin >>= 1
            end >>= 1

        return res
