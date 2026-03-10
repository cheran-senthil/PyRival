# verification-helper: PROBLEM https://judge.yosupo.jp/problem/unionfind
from pyrival.misc.FastIO import input

from pyrival.data_structures.DisjointSetUnion import DisjointSetUnion


def main():
    N, Q = map(int, input().split())
    dsu = DisjointSetUnion(N)
    for _ in range(Q):
        t, u, v = map(int, input().split())
        if t == 0:
            dsu.union(u, v)
        else:
            print(1 if dsu.find(u) == dsu.find(v) else 0)


if __name__ == '__main__':
    main()
