def bfs(graph, start=0):
    used = [False] * len(graph)
    used[start] = True
    q = [start]
    for v in q:
        for w in graph[v]:
            if not used[w]:
                used[w] = True
                q.append(w)


def layers(graph, start=0):
    used = [False] * len(graph)
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
