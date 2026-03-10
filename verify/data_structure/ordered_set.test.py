# verification-helper: PROBLEM https://judge.yosupo.jp/problem/ordered_set
from pyrival.misc.FastIO import input

from pyrival.data_structures.SortedList import SortedList


def main():
    N, Q = map(int, input().split())
    if N:
        a = list(map(int, input().split()))
    else:
        a = []
        input()
    sl = SortedList(a)

    for _ in range(Q):
        t, x = map(int, input().split())
        if t == 0:
            if x not in sl:
                sl.insert(x)
        elif t == 1:
            if x in sl:
                sl.pop(sl.lower_bound(x))
        elif t == 2:
            print(-1 if len(sl) < x else sl[x - 1])
        elif t == 3:
            print(sl.upper_bound(x))
        elif t == 4:
            i = sl.upper_bound(x)
            print(-1 if i == 0 else sl[i - 1])
        else:
            i = sl.lower_bound(x)
            print(-1 if i == len(sl) else sl[i])


if __name__ == '__main__':
    main()
