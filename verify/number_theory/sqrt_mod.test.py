# verification-helper: PROBLEM https://judge.yosupo.jp/problem/sqrt_mod
from pyrival.misc.FastIO import input

from pyrival.algebra.mod_sqrt import mod_sqrt


def main():
    T = int(input())
    for _ in range(T):
        Y, P = map(int, input().split())
        if Y == 0:
            print(0)
        elif pow(Y, (P - 1) // 2, P) != 1:
            print(-1)
        else:
            print(mod_sqrt(Y, P))


if __name__ == '__main__':
    main()
