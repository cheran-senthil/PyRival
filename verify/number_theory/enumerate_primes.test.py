# verification-helper: PROBLEM https://judge.yosupo.jp/problem/enumerate_primes
from pyrival.misc.FastIO import input

from pyrival.algebra.sieve import prime_list


def main():
    N, A, B = map(int, input().split())
    primes = prime_list(N)
    pi = len(primes)
    selected = primes[B::A]
    print(pi, len(selected))
    print(*selected)


if __name__ == '__main__':
    main()
