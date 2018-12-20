from queue import Queue


def is_bipartite(n, graph):
    side = [-1] * n
    res = True
    q = Queue()

    for st in range(n):
        if side[st] == -1:
            q.put(st)
            side[st] = 0
            while not q.empty():
                v = q.get()
                for u in graph[v]:
                    if side[u] == -1:
                        side[u] = side[v] ^ 1
                        q.put(u)
                    else:
                        res &= (side[u] != side[v])

    return res
