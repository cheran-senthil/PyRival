# verification-helper: PROBLEM https://judge.yosupo.jp/problem/number_of_substrings
from pyrival.misc.FastIO import input

from pyrival.strings.suffix_array import SAIS, KASAI


def main():
    S = input()
    n = len(S)
    sa = SAIS([ord(c) for c in S])
    lcp = KASAI(S, sa)
    print(n * (n + 1) // 2 - sum(lcp))


if __name__ == '__main__':
    main()
