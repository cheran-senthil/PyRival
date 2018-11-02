def bellman_ford(vertices, edges, start):
    dist = [float('inf')] * len(vertices)
    pred = [None] * len(vertices)

    dist[start] = 0

    for _ in range(len(vertices)):
        for u, v, d in edges:
            if dist[u] + d < dist[v]:
                dist[v] = dist[u] + d
                pred[v] = u

    """Sanity Check
    for u, v, d in edges:
        if dist[u] + d < dist[v]:
            return None
    """

    return dist, pred
