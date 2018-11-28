def bfs(tree, start=0):
    q, ret = [start], []
    while q:
        ret.append(q)
        q = [i for node in q for i in tree[node]]
    return ret
