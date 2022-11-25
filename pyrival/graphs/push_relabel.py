"""
Original C++
Author: Simon Lindholm
Date: 2015-02-24
License: CC0
Source: Wikipedia, tinyKACTL
Description: Push-relabel using the highest label selection rule and the gap heuristic. Quite fast in practice.
 To obtain the actual flow, look at positive values only.
Time: $O(V^2\sqrt E)$
Status: Tested on Kattis and SPOJ, and stress-tested

Translated by: Whosyourjay
Date: 2022-11-25
"""

class Edge:
    def __init__(self, dest, back, flow, cap):
        self.dest = dest
        self.back = back
        self.flow = flow
        self.cap = cap

class PushRelabel:
    def PushRelabel(self, n):
        self.graph = [[] for _ in range(n)]
        self.ec = [0]*n
        self.cur = [0]*n # Pointer to the next used edge
        self.hs = [0]*(2*n)
        self.H = [[] for _ in range(n)]

    def add_edge(self, src, dest, cap, rcap=0):
        if src == dest:
            return
        self.graph[src].append(
                [dest, len(self.graph[dest]), cap, 0])
        self.graph[dest].append(
                [src, len(self.graph[src]) - 1, rcap, 0])

    def add_flow(self, edge, flow):
        dest = edge[0]
        back = self.graph[dest][edge[1]]
        if (not self.ec[dest]) and flow:
            self.hs[self.H[dest]].append(dest)
        edge[2] += flow
        edge[3] -= flow
        self.ec[dest] += flow

        back[2] -= flow
        back[3] += flow
        self.ec[back[0]] -= flow
    
    def calc(src, dest):
        n = len(self.graph)
        self.H[src] = n
        self.ec[dest] = 1
        co = [0] * (2*n)
        co[0] = n-1
        for i in range(n):
            self.cur[i] = 0
        for edge in self.graph[src]:
            self.add_flow(edge, edge[3])

        hi = 0
        while True:
            while not self.hs[hi]:
                hi--
                if not (hi + 1):
                    return -self.ec[src]
            u = self.hs[hi].pop()
            while self.ec[u] > 0: // discharge u
                if self.cur[u] == len(graph[u]):
                    H[u] = 10**9
                    for pos, edge in enumerate(graph[u]):
                        if edge[3] and self.H[u] > self.H[edge[0]] + 1:
                            self.H[u] = self.H[edge[0]] + 1
                            self.cur[u] = pos;
                    co[self.H[u]] += 1           
                    co[hi] -= 1
                    if (not co[hi]) and hi < n:
                        for i in range(n):
                            if hi < self.H[i] and self.H[i] < n:
                                co[self.H[i]] -= 1
                                self.H[i] = n + 1
                    hi = self.H[u]
                else:
                    edge = self.graph[self.cur[u]]
                    if edge[3] and self.H[u] == self.H[edge[0]] + 1:
                        self.addFlow(edge, min(self.ec[u], edge[3]))
                    else cur[u] += 1
    
    def leftOfMinCut(self, a):
        return self.H[a] >= len(self.graph)
