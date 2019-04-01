from collections import deque


def is_bipartite(n, graph):
    bipartite = True
    side = [-1] * n
    q = deque()

    for st in range(n):
        if side[st] == -1:
            q.append(st)
            side[st] = 0
            while len(q):
                v = q.popleft()
                for u in graph[v]:
                    if side[u] == -1:
                        side[u] = side[v] ^ 1
                        q.append(u)
                    else:
                        bipartite &= side[u] != side[v]

    return bipartite
