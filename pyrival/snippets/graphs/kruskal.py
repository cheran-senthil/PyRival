class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))

    def find(self, a):
        acopy = a
        while a != self.parent[a]:
            a = self.parent[a]
        while acopy != a:
            self.parent[acopy], acopy = a, self.parent[acopy]
        return a

    def merge(self, a, b):
        self.parent[self.find(b)] = self.find(a)


def kruskal(n, U, V, W):
    union = UnionFind(n)
    cost, merge_cnt = 0, 0
    mst_u, mst_v = [], []
    order = sorted(range(len(W)), key=lambda x: W[x])
    for i in range(len(W)):
        u, v = U[order[i]], V[order[i]]
        find_u, find_v = union.find(u), union.find(v)
        if find_u != find_v:
            cost += W[order[i]]
            merge_cnt += 1
            union.parent[find_v] = find_u
            mst_u.append(u), mst_v.append(v)

    return cost, mst_u, mst_v, n == 1 + merge_cnt
