from heapq import heappop, heappush


def topo_sort(n, edges):
    idx, indeg = [0] * n, [0] * n

    for i in range(n):
        for e in edges[i]:
            indeg[e] += 1

    queue = []
    for i in range(n):
        if indeg[i] == 0:
            heappush(queue, -i)

    nr = 0
    while queue:
        i = -heappop(queue)
        idx[i], nr = nr, nr + 1
        for e in edges[i]:
            indeg[e] -= 1
            if indeg[e] == 0:
                heappush(queue, -e)

    return idx, nr == n
