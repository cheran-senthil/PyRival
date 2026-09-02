# verification-helper: PROBLEM https://judge.yosupo.jp/problem/factorize
from pyrival.misc.FastIO import input

from pyrival.algebra.factors import prime_factors


def main():
    Q = int(input())
    for _ in range(Q):
        a = int(input())
        if a <= 1:
            print(0)
        else:
            pf = prime_factors(a)
            factors = sorted(p for p, e in pf.items() for _ in range(e))
            print(len(factors), *factors)


if __name__ == '__main__':
    main()
