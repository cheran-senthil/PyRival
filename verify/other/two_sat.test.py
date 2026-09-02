# verification-helper: PROBLEM https://judge.yosupo.jp/problem/two_sat
from pyrival.misc.FastIO import input

from pyrival.data_structures.TwoSat import TwoSat


def main():
    header = input().split()
    N, M = int(header[2]), int(header[3])
    ts = TwoSat(N)

    for _ in range(M):
        a, b, _ = map(int, input().split())
        x = (a - 1) if a > 0 else ~(-a - 1)
        y = (b - 1) if b > 0 else ~(-b - 1)
        ts.either(x, y)

    sat, assignment = ts.solve()
    if sat:
        print('s SATISFIABLE')
        print('v', *((i + 1) if assignment[i] else -(i + 1) for i in range(N)), 0)
    else:
        print('s UNSATISFIABLE')


if __name__ == '__main__':
    main()
