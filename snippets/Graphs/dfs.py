def dfs(tree):
    parents = [-1] * len(tree)
    for v, children in enumerate(tree):
        for w in children:
            parents[w] = v

    return parents
