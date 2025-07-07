"""
Implementation of heavy-light decomposition of a tree.
This is intended to be combined with a segment tree in order to handle range queries on a tree in O(log^2 n).

It assigns labels to the nodes of a tree such that
* Every subtree is contained in a contiguous interval of labels.
* Any path between two nodes can be decomposed into O(log n) contiguous intervals of labels.

Features:
    HLD.LCA(u, v): 
        Returns lowest common ancestor (LCA) of u and v. Runs in O(log n) time.
    
    HLD.node_query(u): 
        Returns the label of u.
    
    HLD.subtree_query(u): 
        Returns interval [l,r) corresponding to subtree of u.
    
    HLD.path_query(u,v): 
        A generator that yields O(log n) intervals [l,r) corresponding to 
        the path from u to v. The intervals are given in increasing order.
    
    HLD.order: 
        A list, where HLD.order[i] is the node with label i.

For how to use, see the following example:

https://codeforces.com/contest/343/problem/D
https://codeforces.com/contest/343/submission/327932478

```py
HLD = HLD(graph)
SEG = SegmentTree(n)
for _ in range(q):
    c, v = [int(x) - 1 for x in input().split()]
    if c == 0:
        # Fill v's subtree
        l,r = HLD.subtree_query(v)
        SEG.update(l, r, 1)
    elif c == 1:
        # Empty v's ancestors (including v)
        for l,r in HLD.path_query(v, 0):
            SEG.update(l, r, 0)
    else:
        # Query v
        ind = HLD.node_query(v)
        print(SEG[ind])
```
"""

class HLD:
    def __init__(self, graph, root=0):
        n = len(graph)
 
        # Iterative BFS traversal
        P = [-1] * n
        P[root] = root
        BFS = [root]
        for u in BFS:
            for v in graph[u]:
                if P[v] == -1:
                    P[v] = u
                    BFS.append(v)
 
        # Compute subtree sizes
        size = [0] * n
        for u in BFS[::-1]:
            size[u] = 1 + sum(size[v] for v in graph[u])
         
        # Modify BFS to make heaviest child last
        for i in range(1, n - 1):
            if P[BFS[i]] == P[BFS[i + 1]] and size[BFS[i]] > size[BFS[i + 1]]:
                BFS[i],BFS[i + 1] = BFS[i + 1],BFS[i]
         
        # Compute postorder traversal from BFS
        post_trav = [0] * n
        for u in BFS[1:]:
            p = P[u]
            post_trav[u] = post_trav[p]
            post_trav[p] += size[u]
         
        # Invert post_trav
        self.order = order = [0] * n
        for i in range(n):
            order[post_trav[i]] = i
         
        # Remap P and size to post_trav order
        self.P = P = [post_trav[P[u]] for u in order]
        self.size = size = [size[u] for u in order]
         
        # Compute heavy path head
        self.HPH = HPH = [0] * n
        for i in range(n)[::-1]:
            if P[i] == i + 1:
                HPH[i] = HPH[i + 1]
            else:
                HPH[i] = i
    
        self.node_query = post_trav.__getitem__
 
    def _LCA(self, u, v):
        HPH = self.HPH
        P = self.P
        u,v = min(u,v),max(u,v)
        while HPH[u] < v:
            u = P[HPH[u]]
        return max(u,v)   
    
    def _subtree_query(self, u):
        return u + 1 - self.size[u], u + 1

    def _path_query(self, u, v):
        HPH = self.HPH
        P = self.P
        u,v = min(u,v),max(u,v)
        while HPH[u] < v:
            yield u, HPH[u] + 1
            u = P[HPH[u]]
        while HPH[v] < u:
            yield v, HPH[v] + 1
            v = P[HPH[v]]
        yield min(u,v), max(u,v) + 1 
     
    def LCA(self, u, v):
        return self.order[self._LCA(self.node_query(u), self.node_query(v))]
    def subtree_query(self, u):
        return self._subtree_query(self.node_query(u))
    def path_query(self, u, v):
        return self._path_query(self.node_query(u), self.node_query(v))
