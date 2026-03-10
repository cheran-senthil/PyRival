# verification-helper: PROBLEM https://judge.yosupo.jp/problem/convolution_mod
from pyrival.misc.FastIO import input

from pyrival.algebra.ntt import ntt_conv


def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    print(*ntt_conv(A, B))


if __name__ == '__main__':
    main()
