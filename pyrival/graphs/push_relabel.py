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

graph = []
ec = []
hs = []
H = []
class PushRelabel:
    def PushRelabel(self, n):
        graph = [[] for _ in range(n)]
        ec = [0]*n
        hs = [0]*(2*n)
        H = [[] for _ in range(n)]

    def add_edge(self, src, dest, cap, rcap=0):
        if src == dest:
            return
        graph[src].append(
                [dest, len(graph[dest]), cap, 0])
        graph[dest].append(
                [src, len(graph[src]) - 1, rcap, 0])

    def add_flow(self, edge, flow):
        dest = edge[0]
        back = graph[dest][edge[1]]
        if (not ec[dest]) and flow:
            hs[H[dest]].append(dest)
        edge[2] += flow
        edge[3] -= flow
        ec[dest] += flow

        back[2] -= flow
        back[3] += flow
        ec[back[0]] -= flow
    
    def calc(src, dest):
        n = len(graph)
        H[src] = n
        ec[dest] = 1
        co = [0] * (2*n)
        co[0] = n-1

        cur = [0]*n # Pointer to the next used edge
        for edge in graph[src]:
            self.add_flow(edge, edge[3])

        hi = 0
        while True:
            while not hs[hi]:
                hi--
                if not (hi + 1):
                    return -ec[src]
            u = hs[hi].pop()
            while ec[u] > 0: // discharge u
                if cur[u] == len(graph[u]):
                    H[u] = 10**9
                    for pos, edge in enumerate(graph[u]):
                        if edge[3] and H[u] > H[edge[0]] + 1:
                            H[u] = H[edge[0]] + 1
                            cur[u] = pos
                    co[H[u]] += 1           
                    co[hi] -= 1
                    if (not co[hi]) and hi < n:
                        for i in range(n):
                            if hi < H[i] and H[i] < n:
                                co[H[i]] -= 1
                                H[i] = n + 1
                    hi = H[u]
                else:
                    edge = graph[cur[u]]
                    if edge[3] and H[u] == H[edge[0]] + 1:
                        self.addFlow(edge, min(ec[u], edge[3]))
                    else cur[u] += 1
    
    def leftOfMinCut(self, a):
        return H[a] >= len(graph)
