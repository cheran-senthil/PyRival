# from heapq import heappop, heappush


def topo_sort(n, graph):
    idx, indeg = [0] * n, [0] * n

    for i in range(n):
        for e in graph[i]:
            indeg[e] += 1

    q = []
    for i in range(n):
        if indeg[i] == 0:
            q.append(-i)  # heappush(q, -i)

    nr = 0
    while q:
        i = -q.pop()  # -heappop(q)
        idx[i], nr = nr, nr + 1
        for e in graph[i]:
            indeg[e] -= 1
            if indeg[e] == 0:
                q.append(-e)  # heappush(q, -e)

    return idx, nr == n
