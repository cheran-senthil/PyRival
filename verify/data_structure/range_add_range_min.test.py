# verification-helper: PROBLEM https://judge.yosupo.jp/problem/range_add_range_min
from pyrival.misc.FastIO import input

from pyrival.data_structures.LazySegmentTree import LazySegmentTree


def main():
    N, Q = map(int, input().split())
    a = list(map(int, input().split()))
    st = LazySegmentTree(a, default=float('inf'), func=min)
    for _ in range(Q):
        query = list(map(int, input().split()))
        if query[0] == 0:
            _, l, r, x = query
            st.add(l, r, x)
        else:
            _, l, r = query
            print(st.query(l, r, default=float('inf')))


if __name__ == '__main__':
    main()
