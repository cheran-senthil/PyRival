# verification-helper: PROBLEM https://judge.yosupo.jp/problem/point_add_range_sum
from pyrival.misc.FastIO import input

from pyrival.data_structures.FenwickTree import FenwickTree


def main():
    N, Q = map(int, input().split())
    a = list(map(int, input().split()))
    bit = FenwickTree(a)
    for _ in range(Q):
        t, a, b = map(int, input().split())
        if t == 0:
            bit.update(a, b)
        else:
            print(bit.query(b) - bit.query(a))


if __name__ == '__main__':
    main()
