def lis(arr):
    P = [0] * len(arr)
    M = [0] * (len(arr) + 1)
    L = 0

    for i in range(len(arr)):
        lo, hi = 1, L

        while lo <= hi:
            mid = (lo + hi) // 2
            if arr[M[mid]] < arr[i]:
                lo = mid + 1
            else:
                hi = mid - 1

        newL = lo
        P[i] = M[newL - 1]
        M[newL] = i

        L = max(L, newL)

    S = [0] * L
    k = M[L]

    for i in range(L - 1, -1, -1):
        S[i], k = arr[k], P[k]

    return S
