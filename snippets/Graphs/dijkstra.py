from heapq import heappop, heappush


def dijkstra(n, graph, start):
    """
    Uses Dijkstra's algortihm to find the shortest path between in a graph.

    Parameters
    ----------
    graph : list[list[tuple]]
        A list of lists of adjacent vertices and their weights.
    start : int
        The vertex relative to which distances and paths are calculated.

    Returns
    -------
    dist : list[int]
        The relative distances of vertices relative to start.
    parents : list[int]
        The parent of a vertex on its path to start.
    """
    queue = [(0, start)]

    parents = [-1] * n
    visited = [False] * n
    dist = [float('inf')] * n

    dist[start] = 0

    while queue:
        path_len, v = heappop(queue)
        if not visited[v]:
            for (w, edge_len) in graph[v]:
                if (not visited[w]) and (edge_len + path_len < dist[w]):
                    dist[w], parents[w] = edge_len + path_len, v
                    heappush(queue, (edge_len + path_len, w))
            visited[v] = True

    return dist, parents
