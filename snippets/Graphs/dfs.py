def dfs(graph):
    parents = [[]] * len(graph)
    for v, children in enumerate(graph):
        for w in children:
            parents[w].append(v)

    return parents
