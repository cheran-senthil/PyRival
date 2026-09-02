# verification-helper: PROBLEM https://judge.yosupo.jp/problem/find_linear_recurrence
from pyrival.misc.FastIO import input

from pyrival.numerical.berlekamp_massey import berlekamp_massey


def main():
    N = int(input())
    a = list(map(int, input().split()))
    c = berlekamp_massey(a, MOD=998244353)
    print(len(c))
    print(*c)


if __name__ == '__main__':
    main()
