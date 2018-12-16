from queue import Queue


def is_bipartite(adj):
    side = [-1] * len(adj)
    res = True
    q = Queue()

    for st in range(len(adj)):
        if side[st] == -1:
            q.put(st)
            side[st] = 0
            while not q.empty():
                v = q.get()
                for u in adj[v]:
                    if side[u] == -1:
                        side[u] = side[v] ^ 1
                        q.put(u)
                    else:
                        res &= (side[u] != side[v])

    return res
