# verification-helper: PROBLEM https://judge.yosupo.jp/problem/bipartitematching
from pyrival.misc.FastIO import input

from pyrival.graphs.hopcroft_karp import hopcroft_karp


def main():
    L, R, M = map(int, input().split())
    graph = [[] for _ in range(L)]
    for _ in range(M):
        a, b = map(int, input().split())
        graph[a].append(b)

    match1, match2 = hopcroft_karp(graph, L, R)

    edges = [(u, match1[u]) for u in range(L) if match1[u] != -1]
    print(len(edges))
    for u, v in edges:
        print(u, v)


if __name__ == '__main__':
    main()
