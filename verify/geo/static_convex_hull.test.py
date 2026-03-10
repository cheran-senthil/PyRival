# verification-helper: PROBLEM https://judge.yosupo.jp/problem/static_convex_hull
from pyrival.misc.FastIO import input

from pyrival.geometry.convex_hull import convex_hull


def main():
    T = int(input())
    for _ in range(T):
        N = int(input())
        P = [tuple(map(int, input().split())) for _ in range(N)]

        if N == 0:
            print(0)
            continue

        H = convex_hull(P)
        H.reverse()
        print(len(H))
        for x, y in H:
            print(x, y)


if __name__ == '__main__':
    main()
