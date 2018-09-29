class UnionFind:
    def __init__(self, n): 
        self.e = [-1] * n 

    def find(self, x): 
        if self.e[x] < 0:
            return x
        self.e[x] = self.find(self.e[x])
        return self.e[x]

    def same_set(self, a, b): 
        return self.find(a) == self.find(b)

    def size(self, x): 
        return -self.e[self.find(x)]

    def join(self, a, b): 
        a1 = self.find(a)
        b1 = self.find(b)

        if (a1 != b1):
            if self.e[a1] > self.e[b1]:
                a1, b1 = b1, a1
            self.e[a] += self.e[b]
            self.e[b] = a 
