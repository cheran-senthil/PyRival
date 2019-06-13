class RangeQuery:
    def __init__(self, data, func=min):
        n = len(data)
        depth = n.bit_length() + 1
        self.func = func
        self._data = _data = [data[:]]
        for i in range(depth - 1):
            _data_prev = _data[-1]
            _data.append([func(_data_prev[j], _data_prev[min(n - 1, j + (1 << i))]) for j in range(n)])

    def query(self, begin, end):
        depth = (end - begin).bit_length() - 1
        return self.func(self._data[depth][begin], self._data[depth][end - (1 << depth)])
