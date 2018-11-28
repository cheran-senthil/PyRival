def dfs(tree):
    out = [-1] * len(tree)
    for i, j in enumerate(tree):
        for k in j:
            out[k] = i
    return out
