def dfs(n, graph, start=0, depth=0):
    parents, visited = [[] for _ in range(n)], [False] * n
    stack = [(start, depth)]

    while stack:
        start, depth = stack[-1]

        if visited[start]:
            stack.pop()
            continue
        else:
            visited[start] = True

        for i in graph[start]:
            if not visited[i]:
                parents[i].append(start)
                stack.append((i, depth + 1))

    return parents, visited
