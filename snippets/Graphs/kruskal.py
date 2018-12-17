def kruskal(n, edges):
    parent, rank = list(range(n)), [0] * n

    def find_set(v):
        tmp = []
        while v != parent[v]:
            tmp.append(v)
            v = parent[v]
        for i in tmp:
            parent[i] = v

        return v

    cost, result = 0, []

    for edge in sorted(edges, key=lambda edge: edge[2]):
        find_u, find_v = find_set(edge[0]), find_set(edge[1])

        if find_u != find_v:
            cost += edge[2]
            result.append(edge)

            if rank[find_u] < rank[find_v]:
                find_v, find_u = find_u, find_v
            elif rank[find_u] == rank[find_v]:
                rank[find_u] += 1

            parent[find_v] = find_u

    return result, cost
