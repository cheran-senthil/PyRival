# verification-helper: PROBLEM https://judge.yosupo.jp/problem/primitive_root
from pyrival.misc.FastIO import input

from pyrival.algebra.primitive_root import primitive_root


def main():
    Q = int(input())
    for _ in range(Q):
        p = int(input())
        print(primitive_root(p))


if __name__ == '__main__':
    main()
