def prim(n, adj):
    total_weight = 0
    selected, min_e = [False] * n, [[float('inf'), -1] for _ in range(n)]
    mst_edges = []

    min_e[0][0] = 0

    for i in range(n):
        v = -1

        for j in range(n):
            if (not selected[j]) and ((v == -1) or (min_e[j][0] < min_e[v][0])):
                v = j

        if min_e[v][0] == float('inf'):
            return None, None

        selected[v] = True
        total_weight += min_e[v][0]

        if min_e[v][1] != -1:
            mst_edges.append((v, min_e[v][1]))

        for to in range(n):
            if adj[v][to] < min_e[to][0]:
                min_e[to] = [adj[v][to], v]

    return mst_edges, total_weight
