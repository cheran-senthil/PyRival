def floyd_warshall(n, edges):
    dist = [[0 if i == j else float('inf') for i in range(n)] for j in range(n)]
    pred = [[None] * n for _ in range(n)]

    for u, v, d in edges:
        dist[u][v] = d
        pred[u][v] = u

    for k in range(n):
        for i in range(n):
            for j in range(n):
                if dist[i][k] + dist[k][j] < dist[i][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]
                    pred[i][j] = pred[k][j]
    """Sanity Check
    for u, v, d in edges:
        if dist[u] + d < dist[v]:
            return None
    """

    return dist, pred
