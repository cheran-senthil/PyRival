# verification-helper: PROBLEM https://judge.yosupo.jp/problem/longest_increasing_subsequence
from pyrival.misc.FastIO import input

from pyrival.misc.lis import lis


def main():
    N = int(input())
    A = list(map(int, input().split()))
    result = lis(A)
    K = len(result)

    indices = []
    j = 0
    for i in range(N):
        if j < K and A[i] == result[j]:
            indices.append(i)
            j += 1

    print(K)
    print(*indices)


if __name__ == '__main__':
    main()
