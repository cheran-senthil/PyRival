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
        t, data = 0, []
        V, P, D, S = [0], [0], [0], [0]
        while V:
            v, p, d, s = V.pop(), P.pop(), D.pop(), S.pop()
            time[v], dist[v] = t, s
            if d:
                data.append((d, p))
            for u, w in graph[v]:
                if u != p:
                    V.append(u)
                    P.append(v)
                    D.append(d + 1)
                    S.append(s + w)
            t += 1

        self.rmq = RangeQuery(data)

    def query(self, a, b):
        if a == b:
            return a
        a, b = self.time[a], self.time[b]
        return self.rmq.query(min(a, b), max(a, b))[1]

    def distance(self, a, b):
        return self.dist[a] + self.dist[b] - 2 * self.dist[self.query(a, b)]
