# verification-helper: PROBLEM https://judge.yosupo.jp/problem/zalgorithm
from pyrival.misc.FastIO import input

from pyrival.strings.z_algorithm import z_function


def main():
    S = input()
    print(*z_function(S))


if __name__ == '__main__':
    main()
