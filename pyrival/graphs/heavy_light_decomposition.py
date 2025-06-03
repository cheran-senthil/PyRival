
"""
Example Usage:
 >>> adj = [[1],[0,2,3],[1],[1]]
 >>> values = [1,5,3,2] 
 >>> hld = HLD(adj,values)
 >>> print("Max on path from 0 to 2: ",hld.query(0,2))
 Max on path from 0 to 2: 5
"""

class HLD:
    def __init__(self, adj, values, root=0,func=max,unit=float('-inf')):
        """
        Given a Tree, Heavy Light Decomposition supports querying on simple path between 
        any two vertices in O(log2n), change the value of unit, max_val and function func
        according to the range query type. Recursion has not been used so as avoid 
        having to use decorater and to avoid overhead.
        """
        self.n = len(adj)
        self.adj = adj
        self.values = values
        self.root = root
        self.parent = [-1] * self.n
        self.depth = [0] * self.n
        self.size = [0] * self.n
        self.heavy = [-1] * self.n
        self.head = [0] * self.n
        self.pos = [0] * self.n
        self.flat = [0] * self.n
        self.time = 0
        self.unit = unit
        self.func = func
        self._dfs(self.root)
        self._decompose(self.root, self.root)
        self.seg = SegmentTree([self.values[self.flat[i]] for i in range(self.n)],func,unit)

    def _dfs(self,start=0):
        graph = self.adj
        n = self.n
        visited = [False] * n
        stack = [start]
        while stack:
            start = stack[-1]
            if not visited[start]:
                visited[start] = True
                for child in graph[start]:
                    if not visited[child]:
                        self.parent[child] = start
                        self.depth[child] = self.depth[start]+1
                        stack.append(child)
            else:
                stack.pop()
                self.size[start] = 1
                k = 0
                for child in graph[start]:
                    if self.parent[start]!=child:
                        self.size[start] += self.size[child]
                        if self.size[child]>k:
                            k = self.size[child]
                            self.heavy[start] = child
        return visited
    
    def _decompose(self, root, h):
        stack = [(root, h)]
        while stack:
            u, h = stack.pop()
            self.head[u] = h
            self.flat[self.time] = u
            self.pos[u] = self.time
            self.time += 1
            for v in reversed(self.adj[u]):
                if v!=self.parent[u] and v!=self.heavy[u]:
                    stack.append((v, v))
            if self.heavy[u] != -1:
                stack.append((self.heavy[u], h))

    def query(self, u, v):
        res = self.unit
        while self.head[u] != self.head[v]:
            if self.depth[self.head[u]] < self.depth[self.head[v]]:
                u, v = v, u
            res = self.func(res, self.seg.query(self.pos[self.head[u]], self.pos[u] + 1))
            u = self.parent[self.head[u]]
        if self.depth[u] > self.depth[v]:
            u, v = v, u
        res = self.func(res, self.seg.query(self.pos[u], self.pos[v] + 1))
        return res
    
    def update(self, u, value):
        self.seg.update(self.pos[u], value)


# Segment Tree for range queries in HLD
class SegmentTree:
    def __init__(self, data,func=max,unit=float('-inf')):
        self.func = func
        self.unit = unit
        self.n = len(data)
        self.tree = [0] * (2 * self.n)
        self.build(data)

    def build(self, data):
        for i in range(self.n):
            self.tree[self.n + i] = data[i]
        for i in range(self.n - 1, 0, -1):
            self.tree[i] = self.func(self.tree[i * 2], self.tree[i * 2 + 1])

    def update(self, pos, value):
        pos += self.n
        self.tree[pos] = value
        while pos > 1:
            pos //= 2
            self.tree[pos] = self.func(self.tree[2 * pos], self.tree[2 * pos + 1])

    def query(self, left, right):
        left += self.n
        right += self.n
        max_val = self.unit
        while left < right:
            if left % 2:
                max_val = self.func(max_val, self.tree[left])
                left += 1
            if right % 2:
                right -= 1
                max_val = self.func(max_val, self.tree[right])
            left //= 2
            right //= 2
        return max_val
