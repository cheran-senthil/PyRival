# verification-helper: PROBLEM https://judge.yosupo.jp/problem/scc
from pyrival.misc.FastIO import input

from pyrival.graphs.scc import find_SCC


def main():
    N, M = map(int, input().split())
    graph = [[] for _ in range(N)]
    for _ in range(M):
        a, b = map(int, input().split())
        graph[a].append(b)

    sccs = find_SCC(graph)
    print(len(sccs))
    for comp in sccs:
        print(len(comp), *comp)


if __name__ == '__main__':
    main()
