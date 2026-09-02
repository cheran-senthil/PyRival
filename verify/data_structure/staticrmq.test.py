# verification-helper: PROBLEM https://judge.yosupo.jp/problem/staticrmq
from pyrival.misc.FastIO import input

from pyrival.data_structures.RangeMinimumQuery import RangeMinimumQuery


def main():
    N, Q = map(int, input().split())
    a = list(map(int, input().split()))
    rmq = RangeMinimumQuery(a)
    for _ in range(Q):
        l, r = map(int, input().split())
        print(rmq.query(l, r))


if __name__ == '__main__':
    main()
