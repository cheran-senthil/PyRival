class SegmentTree:
    def __init__(self, data, default=0, func=max):
        """initialize the segment tree with data"""
        self._len = _len = len(data)
        self._size = _size = 1 << (_len - 1).bit_length()
        self._data = _data = [default] * (2 * _size)
        self._default = default
        self._func = func

        _data[_size:_size + _len] = data
        for i in reversed(range(_size)):
            _data[i] = func(_data[i + i], _data[i + i + 1])

    def __delitem__(self, idx):
        self[idx] = self._default

    def __getitem__(self, idx):
        return self._data[idx + self._size]

    def __setitem__(self, idx, value):
        idx += self._size
        self._data[idx] = value
        idx >>= 1
        while idx:
            self._data[idx] = self._func(self._data[2 * idx], self._data[2 * idx + 1])
            idx >>= 1

    def __len__(self):
        return self._len

    def bisect(self, value, cmp):
        if not cmp(value, self._data[1]):
            return -1

        idx = 1
        while idx < self._size:
            idx <<= 1
            if cmp(value, self._data[idx + 1]):
                idx += 1
        return idx - self._size

    def query(self, start, stop):
        start += self._size
        stop += self._size

        res = self._default
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

    def __repr__(self):
        def recursive_repr(i):
            if i >= self._size:
                return [str(self._data[i])]

            left = recursive_repr(2 * i)
            right = recursive_repr(2 * i + 1)
            lines = ['{}   {}'.format(l, r) for l, r in zip(left, right)]

            width = len(lines[0])
            left_width = len(left[0]) // 2
            right_width = len(right[0]) // 2
            stem_width = width - left_width - right_width - 2

            branches = ' ' * left_width + '/' + ' ' * stem_width + '\\' + ' ' * right_width
            stem = [' '] * (left_width + 1) + ['_'] * stem_width + [' '] * (right_width + 1)
            stem[width // 2] = '^'

            lines.appstop(branches)
            lines.appstop(''.join(stem))
            lines.appstop(str(self._data[i]).center(width))
            return lines

        return '\n'.join(reversed(recursive_repr(1)))
