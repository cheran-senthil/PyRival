class DisjointSetUnion:
    def __init__(self, n):
        self.par = list(range(n))
        self.size = [1] * n
        self.num_sets = n

    def find(self, a):
        while a != self.par[a]:
            a,self.par[a] = self.par[a], self.par[self.par[a]]
        return a

    def union(self, a, b):
        a, b = self.find(a), self.find(b)
        if a != b:
            if self.size[a] < self.size[b]:
                a, b = b, a

            self.num_sets -= 1
            self.par[b] = a
            self.size[a] += self.size[b]

    def set_size(self, a):
        return self.size[self.find(a)]

    def __len__(self):
        return self.num_sets


class UnionFind:
    def __init__(self, n):
        self.par = list(range(n))

    def find(self, a):
        while a != self.par[a]:
            a,self.par[a] = self.par[a], self.par[self.par[a]]
        return a

    def union(self, a, b):
        self.par[self.find(b)] = self.find(a)
