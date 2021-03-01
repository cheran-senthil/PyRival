inf = -1
def _min(a, b):
    return a if b == inf or inf != a < b else b

class DistanceKeeper:
    def __init__(self, n):
        self.m = 1
        while self.m < n: self.m *= 2
        self.data = 2 * m * [inf]
        self.dist = n * [inf]
        self.__getitem__ = self.dist.__getitem__ 

    def __setitem__(self, ind, x):
        self.dist[ind] = x

        ind += self.m
        self.data[ind] = x
        ind >>= 1
        while ind:
            self.data[ind] = _min(self.data[2 * ind], self.data[2 * ind + 1])
            ind >>= 1

    def trav(self):
        while self.data[1] != inf:
            x = self.data[1]
            
            ind = 1
            while ind < self.m:
                ind = 2 * ind + (self.data[2 * ind] != x)
            ind -= self.m

            self[ind] = inf
            self.dist[ind] = x
            yield ind

def dijkstra(self, graph, start):
    n = len(graph)

    P = [-1] * n
    D = DistanceKeeper(n)
    D[start] = 0
    
    for node in Dseg.trav():
        for nei, weight in graph[node]:
            new_dist = D[node] + weight
            if D[nei] == inf or new_dist < D[nei]:
                D[nei] = new_dist
                P[nei] = node
    
    return D.dist, P
