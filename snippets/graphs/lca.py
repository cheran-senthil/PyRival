class RangeQuery:
    def __init__(self, data, func=min):
        self.func = func
        self._data = _data = [list(data)]
        i, n = 1, len(data)
        while 2 * i <= n:
            prev = _data[-1]
            _data.append([func(prev[j], prev[j + i]) for j in range(n - 2 * i + 1)])
            i <<= 1

    def query(self, begin, end):
        depth = (end - begin).bit_length() - 1
        return self.func(self._data[depth][begin], self._data[depth][end - (1 << depth)])


class LCA:
    def __init__(self, graph):
        self.time = time = [0] * len(graph)
        self.dist = dist = [0] * len(graph)
        ret = []
        T, V, P, D, Di = 0, [0], [0], [0], [0]
        while D:
            v, p, d, di = V.pop(), P.pop(), D.pop(), Di.pop()
            if d:
                ret.append((d, p))
            time[v] = T
            T += 1
            dist[v] = di
            for e in graph[v]:
                if e[0] != p:
                    V.append(e[0])
                    P.append(v)
                    D.append(d + 1)
                    Di.append(di + e[1])

        self.rmq = RangeQuery(ret)

    def query(self, a, b):
        if a == b:
            return a
        a, b = self.time[a], self.time[b]
        return self.rmq.query(min(a, b), max(a, b))[1]

    def distance(self, a, b):
        return self.dist[a] + self.dist[b] - 2 * self.dist[self.query(a, b)]
