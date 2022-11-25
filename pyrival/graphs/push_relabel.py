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
        self.cur = [0]*n
        self.hs = [0]*(2*n)
        self.H = [[] for _ in range(n)]

    def add_edge(self, src, dest, cap, rcap=0):
        if src == dest:
            return
        self.graph[src].append(
                Edge(dest, len(self.graph[dest]), cap, 0))
        self.graph[dest].append(
                Edge(src, len(self.graph[src]) - 1, rcap, 0))

    def add_flow(self, edge, flow):
        back = self.graph[edge.dest][edge.back]
        if (not self.ec[edge.dest]) and flow:
            self.hs[self.H[edge.dest]].append(edge.dest)
		edge.flow += flow
        edge.cap -= flow
        self.ec[edge.dest] += flow

		back.flow -= flow
        back.cap += flow
        self.ec[back.dest] -= flow
	
    def calc(src, dest):
		n = len(self.graph)
        self.H[src] = n
        self.ec[dest] = 1
		co = [0] * (2*n)
        co[0] = n-1
        for i in range(n):
            self.cur[i] = 0 #.data()
        for edge in self.graph[src]:
            self.add_flow(edge, edge.cap)

        hi = 0
        while True:
			while self.hs[hi].empty()
                hi--
                if not (hi + 1):
                    return -self.ec[src]
			u = self.hs[hi].pop()
            while self.ec[u] > 0: // discharge u
                if self.cur[u] == len(graph[u]):
					H[u] = 10**9
                    for pos, edge in enumerate(graph[u]):
                        if edge.cap and self.H[u] > self.H[edge.dest] + 1:
						    self.H[u] = self.H[edge.dest] + 1
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
                    if edge.cap and self.H[u] == self.H[edge.dest] + 1:
                        self.addFlow(edge, min(self.ec[u], edge.cap))
                    else cur[u] += 1
	
    def leftOfMinCut(self, a):
        return self.H[a] >= len(self.graph)
