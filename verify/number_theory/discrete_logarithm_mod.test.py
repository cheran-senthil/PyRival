# verification-helper: PROBLEM https://judge.yosupo.jp/problem/discrete_logarithm_mod
from pyrival.misc.FastIO import input

from pyrival.algebra.discrete_log import discrete_log


def main():
    T = int(input())
    for _ in range(T):
        X, Y, M = map(int, input().split())
        if Y % M == 1 % M:
            print(0)
        else:
            result = discrete_log(X, Y, M)
            print(result if result is not None else -1)


if __name__ == '__main__':
    main()
