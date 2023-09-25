"""
Binary lifting technique applied to a tree.
There are four different uses of this implementation

1. Computing LCA in O(log n) time.
   
   Example:
           0
           |
           1
          / \
         2   3

       graph = [[1], [0, 2, 3], [1], [1]]
       BL = binary_lift(graph, root=0)
       print(BL.lca(2, 3)) # prints 1

2. Compute the k-th ancestor of a node in O(log k) time.

   Example:
       graph = [[1], [0, 2, 3], [1], [1]]
       BL = binary_lift(graph, root=0)
       print(BL.kth_ancestor(2, 2)) # prints 0
       print(BL.kth_ancestor(2, 3)) # prints -1

3. Compute the distance between two nodes in O(log n) time.

   Example:
       graph = [[1], [0, 2, 3], [1], [1]]
       BL = binary_lift(graph)
       print(BL.distance(2, 3)) # prints 2

4. Compute the sum/min/max/... of the weight 
   of a path between a pair of nodes in O(log n) time.

   res = data[Path[0]]
   for node in Path[1:]:
     res = f(res, data[node])
   return res
   
   Example:
       
       graph = [[1], [0, 2, 3], [1], [1]]
       data = [1, 10, 20, 5]
       BL = binary_lift(graph, data, f = lambda a,b: a + b)
       print(BL(2, 3)) # prints 35
"""

class binary_lift:
    def __init__(self, graph, data=(), f=min, root=0):
        n = len(graph)

        parent = [-1] * (n + 1)
        depth = self.depth = [-1] * n
        bfs = [root]
        depth[root] = 0
        for node in bfs:
            for nei in graph[node]:
                if depth[nei] == -1:
                    parent[nei] = node
                    depth[nei] = depth[node] + 1
                    bfs.append(nei)

        data = self.data = [data]
        parent = self.parent = [parent]
        self.f = f

        for _ in range(max(depth).bit_length()):
            old_data = data[-1]
            old_parent = parent[-1]
            
            data.append([f(val, old_data[p]) for val,p in zip(old_data, old_parent)])
            parent.append([old_parent[p] for p in old_parent])
    
    def lca(self, a, b):
        depth = self.depth
        parent = self.parent

        if depth[a] < depth[b]:
            a,b = b,a
        
        d = depth[a] - depth[b]
        for i in range(d.bit_length()):
            if (d >> i) & 1:
                a = parent[i][a]

        for i in range(depth[a].bit_length())[::-1]:
            if parent[i][a] != parent[i][b]:
                a = parent[i][a]
                b = parent[i][b]

        if a != b:
            return parent[0][a]
        else:
            return a
    
    def distance(self, a, b):
        return self.depth[a] + self.depth[b] - 2 * self.depth[self.lca(a,b)]

    def kth_ancestor(self, a, k):
        parent = self.parent
        if self.depth[a] < k:
            return -1
        for i in range(k.bit_length()):
            if (k >> i) & 1:
                a = parent[i][a]
        return a

    def __call__(self, a, b):
        depth = self.depth
        parent = self.parent
        data = self.data
        f = self.f
        
        c = self.lca(a, b)
        val = data[0][c]
        for x,d in (a, depth[a] - depth[c]), (b, depth[b] - depth[c]):
            for i in range(d.bit_length()):
                if (d >> i) & 1:
                    val = f(val, data[i][x])
                    x = parent[i][x]

        return val
