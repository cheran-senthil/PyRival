# verification-helper: PROBLEM https://judge.yosupo.jp/problem/shortest_path
from pyrival.misc.FastIO import input

from pyrival.graphs.dijkstra import dijkstra


def main():
    N, M, s, t = map(int, input().split())
    graph = [[] for _ in range(N)]
    for _ in range(M):
        a, b, c = map(int, input().split())
        graph[a].append((b, c))

    dist, parents = dijkstra(graph, s)

    if dist[t] == float('inf'):
        print(-1)
        return

    path = []
    v = t
    while v != s:
        path.append(v)
        v = parents[v]
    path.append(s)
    path.reverse()

    print(dist[t], len(path) - 1)
    for i in range(len(path) - 1):
        print(path[i], path[i + 1])


if __name__ == '__main__':
    main()
