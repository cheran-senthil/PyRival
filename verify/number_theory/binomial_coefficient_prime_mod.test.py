# verification-helper: PROBLEM https://judge.yosupo.jp/problem/binomial_coefficient_prime_mod
from pyrival.misc.FastIO import input

from pyrival.combinatorics.nCr_mod import make_nCr_mod


def main():
    T, m = map(int, input().split())
    nCr = make_nCr_mod(max_n=10**7, mod=m)
    for _ in range(T):
        n, r = map(int, input().split())
        print(nCr(n, r))


if __name__ == '__main__':
    main()
