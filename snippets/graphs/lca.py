class RangeQuery:
    def __init__(self, data, func=min):
        self.func = func
        self._data = _data = [list(data)]
        i, n = 1, len(_data[0])
        while 2 * i <= n:
            prev = _data[-1]
            _data.append([func(prev[j], prev[j + i]) for j in range(n - 2 * i + 1)])
            i <<= 1

    def query(self, begin, end):
        depth = (end - begin).bit_length() - 1
        return self.func(self._data[depth][begin], self._data[depth][end - (1 << depth)])


class LCA:
    def __init__(self, root, graph):
        self.time = [-1] * len(graph)
        self.path = []
        dfs = [root]
        while dfs:
            node = dfs.pop()
            self.path.append(node)
            if self.time[node] == -1:
                self.time[node] = len(self.path) - 1
                for nei in graph[node]:
                    if self.time[nei] == -1:
                        dfs.append(node)
                        dfs.append(nei)
        self.rmq = RangeQuery(self.time[node] for node in self.path)

    def lca(self, a, b):
        a = self.time[a]
        b = self.time[b]
        if a > b:
            a, b = b, a
        return self.path[self.rmq.query(a, b + 1)]
