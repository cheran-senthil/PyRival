# from heapq import heappop, heappush


def toposort(graph):
    n = len(graph)
    res, visited = [], [False] * n

    def dfs(start):
        stack = [start]
        while stack:
            start = stack[-1]
            if not visited[start]:
                visited[start] = True
                for child in graph[start]:
                    if not visited[child]:
                        stack.append(child)
            else:
                res.append(stack.pop())

    for i in range(n):
        if not visited[i]:
            dfs(i)

    return res


def kahn(graph):
    n = len(graph)

    indeg, idx = [0] * n, [0] * n
    for i in range(n):
        for e in graph[i]:
            indeg[e] += 1

    q, res = [], []
    for i in range(n):
        if indeg[i] == 0:
            q.append(i)  # heappush(q, -i)

    nr = 0
    while q:
        res.append(q.pop())  # res.append(-heappop(q))
        idx[res[-1]], nr = nr, nr + 1
        for e in graph[res[-1]]:
            indeg[e] -= 1
            if indeg[e] == 0:
                q.append(e)  # heappush(q, -e)

    return res, idx, nr == n
