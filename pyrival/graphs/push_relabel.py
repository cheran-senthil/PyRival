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
    def __init__(self, dest, back, f, c):
        self.dest = dest
        self.back = back
        self.f = f
        self.c = c

class PushRelabel:
    def PushRelabel(self, n):
        self.g = [[] for _ in range(n)]
        self.ec = [0]*n
        self.cur = [0]*n
        self.hs = [0]*(2*n)
        self.H = [[] for _ in range(n)]

    def add_edge(self, s, t, cap, rcap=0):
        if s == t:
            return
        self.g[s].append(Edge(t, len(self.g[t]), cap, 0))
        self.g[t].append(Edge(s, len(self.g[s]) - 1, rcap, 0))

    def add_flow(self, e, f):
        back = self.g[e.dest][e.back]
        if (not self.ec[e.dest]) and f:
            self.hs[self.H[e.dest]].append(e.dest)
		e.f += f
        e.c -= f
        self.ec[e.dest] += f

		back.f -= f
        back.c += f
        self.ec[back.dest] -= f
	
    def calc(s, t):
		v = len(self.g)
        self.H[s] = v
        self.ec[t] = 1
		co = [0] * (2*v)
        co[0] = v-1
        for i in range(v):
            self.cur[i] = 0 #.data()
        for e in self.g[s]:
            self.add_flow(e, e.c)

        hi = 0
        while True:
			while self.hs[hi].empty()
                hi--
                if not (hi + 1):
                    return -self.ec[s]
			u = self.hs[hi].pop()
            while self.ec[u] > 0: // discharge u
                if self.cur[u] == len(g[u]):
					H[u] = 10**9
                    for pos, e in enumerate(g[u]):
                        if e.c and self.H[u] > self.H[e.dest] + 1:
						    self.H[u] = self.H[e.dest] + 1
                            self.cur[u] = pos;
                    co[self.H[u]] += 1           
                    co[hi] -= 1
                    if (not co[hi]) and hi < v:
                        for i in range(v):
                            if hi < self.H[i] and self.H[i] < v:
                                co[self.H[i]] -= 1
                                self.H[i] = v + 1
					hi = self.H[u]
                else:
                    edge = self.g[self.cur[u]]
                    if edge.c and self.H[u] == self.H[edge.dest] + 1:
                        self.addFlow(edge, min(self.ec[u], edge.c))
                    else cur[u] += 1
	
    def leftOfMinCut(self, a):
        return self.H[a] >= len(self.g)
