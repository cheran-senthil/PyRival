# verification-helper: PROBLEM https://judge.yosupo.jp/problem/lca
from pyrival.misc.FastIO import input

from pyrival.graphs.lca import LCA


def main():
    N, Q = map(int, input().split())
    parents = list(map(int, input().split()))

    graph = [[] for _ in range(N)]
    for i, p in enumerate(parents, 1):
        graph[p].append(i)
        graph[i].append(p)

    lca = LCA(0, graph)

    for _ in range(Q):
        u, v = map(int, input().split())
        print(lca(u, v))


if __name__ == '__main__':
    main()
