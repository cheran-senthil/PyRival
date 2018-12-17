def dfs(graph):
    parents = [[] for _ in range(len(graph))]
    for v, children in enumerate(graph):
        for w in children:
            parents[w].append(v)

    return parents
