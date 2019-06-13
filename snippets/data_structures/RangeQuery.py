class RangeQuery:
    def __init__(self, data, func=min):
        n = len(data)
        depth = n.bit_length() + 1
        self.func = func
        self._data = _data = [data[:] for _ in range(depth)]
        for i in range(depth - 1):
            _data_prev, _data_next = _data[i], _data[i + 1]
            for j in range(n - (1 << i)):
                _data_next[j] = func(_data_prev[j], _data_prev[j + (1 << i)])

    def query(self, begin, end):
        depth = (end - begin).bit_length() - 1
        return self.func(self._data[depth][begin], self._data[depth][end - (1 << depth)])
