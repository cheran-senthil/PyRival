# verification-helper: PROBLEM https://judge.yosupo.jp/problem/suffixarray
from pyrival.misc.FastIO import input

from pyrival.strings.suffix_array import SAIS


def main():
    S = input()
    sa = SAIS([ord(c) for c in S])
    print(*sa)


if __name__ == '__main__':
    main()
