def is_bipartite(graph):
    n = len(graph)

    bipartite = True

    color = [-1] * n
    color[0] = 0

    visited = [False] * n

    for start in range(n):
        stack = [start]
        while stack:
            start = stack.pop()

            if not visited[start]:
                visited[start] = True
                for child in graph[start]:
                    bipartite &= color[child] != color[start]
                    color[child] = color[start] ^ 1
                    if not visited[child]:
                        stack.append(child)

    return bipartite, color
