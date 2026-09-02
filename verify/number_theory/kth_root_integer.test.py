# verification-helper: PROBLEM https://judge.yosupo.jp/problem/kth_root_integer
from pyrival.misc.FastIO import input

from pyrival.numerical.iroot import iroot


def main():
    T = int(input())
    for _ in range(T):
        A, K = map(int, input().split())
        print(iroot(A, K))


if __name__ == '__main__':
    main()
