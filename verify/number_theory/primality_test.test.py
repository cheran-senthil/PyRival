# verification-helper: PROBLEM https://judge.yosupo.jp/problem/primality_test
from pyrival.misc.FastIO import input

from pyrival.algebra.is_prime import is_prime


def main():
    Q = int(input())
    for _ in range(Q):
        n = int(input())
        print('Yes' if is_prime(n) else 'No')


if __name__ == '__main__':
    main()
