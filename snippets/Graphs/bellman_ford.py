def bellman_ford(n, edges, start):
    dist = [float('inf')] * n
    pred = [None] * n

    dist[start] = 0

    for _ in range(n):
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
