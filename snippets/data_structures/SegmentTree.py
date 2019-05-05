class SegmentTree:
    def __init__(self, data, default=0, func=lambda x, y: max(x, y)):
        """initialize the segment tree with data"""
        self._len = _len = len(data)
        self._size = _size = 1 << (_len - 1).bit_length()
        self._data = _data = [default] * (2 * _size)
        self._default = default
        self._func = func
        _data[_size:_size + _len] = data
        for i in reversed(range(_size)):
            _data[i] = func(_data[2 * i], _data[2 * i + 1])

    def __delitem__(self, key):
        self[key] = self._default

    def __getitem__(self, key):
        return self._data[key + self._size]

    def __setitem__(self, key, value):
        key += self._size
        self._data[key] = value
        key >>= 1
        while key:
            self._data[key] = self._func(self._data[2 * key], self._data[2 * key + 1])
            key >>= 1

    def __len__(self):
        return self._len

    def bisect_left(self, value):
        i = 1
        while i < self._size:
            i = 2 * i + 1 if value > self._data[2 * i] else 2 * i
        return i - self._size

    def bisect_right(self, value):
        i = 1
        while i < self._size:
            i = 2 * i + 1 if value >= self._data[2 * i] else 2 * i
        return i - self._size

    def query(self, begin, end):
        begin += self._size
        end += self._size
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

            lines.append(branches)
            lines.append(''.join(stem))
            lines.append(str(self._data[i]).center(width))
            return lines

        return '\n'.join(reversed(recursive_repr(1)))
