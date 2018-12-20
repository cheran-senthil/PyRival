def bfs(n, graph, start=0):
    used = [False] * n
    used[start] = True

    q, ret = [start], []

    while q:
        nq = []
        ret.append(q)

        for v in q:
            for w in graph[v]:
                if not used[w]:
                    used[w] = True
                    nq.append(w)

        q = nq

    return ret
