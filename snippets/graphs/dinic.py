from collections import deque

INF = float("inf")

SCALING = False


class Dinic:
    def __init__(self, maxv, var=int):
        self.lim = 1
        self.s = maxv - 2
        self.t = maxv - 1

        self.level = [0] * maxv
        self.ptr = [0] * maxv
        self.adj = [[] for _ in range(maxv)]

    def add_edge(self, a, b, cap, is_directed=True):
        self.adj[a].append([b, len(self.adj[b]), cap, 0])
        self.adj[b].append([a, len(self.adj[a]) - 1, 0 if is_directed else cap, 0])

    def bfs(self):
        q = deque([self.s])
        self.level = [-1] * len(self.level)

        while q and self.level[self.t] == -1:
            v = q.popleft()
            for e in self.adj[v]:
                if (self.level[e[0]] == -1 and e[3] < e[2] and ((not SCALING) or (e[2] - e[3] >= self.lim))):
                    q.append(e[0])
                    self.level[e[0]] = self.level[v] + 1

        return self.level[self.t] != -1

    def dfs(self, v, flow):
        if v == self.t or not flow:
            return flow
        while self.ptr[v] < len(self.adj[v]):
            e = self.adj[v][self.ptr[v]]
            if self.level[e.to] != self.level[v] + 1:
                continue
            pushed = self.dfs(e.to, min(flow, e.cap - e.flow))
            if pushed:
                e.flow += pushed
                self.adj[e.to][e.rev].flow -= pushed
                return pushed
            return 0

    def calc(self):
        flow = 0
        self.lim = 1 << 30 if SCALING else 1
        while self.lim > 0:
            while self.bfs():
                self.ptr = [0] * len(self.ptr)
                pushed = self.dfs(self.s, INF)
                while pushed:
                    flow += pushed
                    pushed = self.dfs(self.s, INF)
            self.lim >>= 1

        return flow
