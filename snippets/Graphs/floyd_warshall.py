from collections import defaultdict


def floyd_warshall(graph):
    dist, pred = dict(), dict()

    for u, neighbours in graph.items():
        dist[u] = defaultdict(lambda: float('+inf'))
        pred[u] = defaultdict(lambda: None)

        for v, d in neighbours.items():
            dist[u][v] = d
            pred[u][v] = u

        dist[u][u] = 0

    for k in graph:
        for i in graph:
            for j in graph:
                if dist[i][k] + dist[k][j] < dist[i][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]
                    pred[i][j] = pred[k][j]

    return dist, pred
