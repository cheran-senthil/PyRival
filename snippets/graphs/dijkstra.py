from heapq import heappop, heappush


def dijkstra(n, graph, start):
    """ Uses Dijkstra's algortihm to find the shortest path between in a graph. """
    dist, parents = [float('inf')] * n, [-1] * n
    dist[start] = 0

    queue = [(0, start)]
    while queue:
        path_len, v = heappop(queue)
        if path_len == dist[v]:
            for w, edge_len in graph[v]:
                if edge_len + path_len < dist[w]:
                    dist[w], parents[w] = edge_len + path_len, v
                    heappush(queue, (edge_len + path_len, w))

    return dist, parents
