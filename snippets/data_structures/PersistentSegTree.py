BIG = 10**9

vals = []
L = []
R = []


# Create a persistant segmenttree of size n
def create(n):
    ind = len(vals)
    vals.append(BIG)

    L.append(-1)
    R.append(-1)

    if n == 1:
        L[ind] = -1
        R[ind] = -1
    else:
        mid = n // 2
        L[ind] = create(mid)
        R[ind] = create(n - mid)

    return ind


# Set seg[i]=val for segment tree ind, of size n,
def setter(ind, i, val, n):
    ind2 = len(vals)
    vals.append(BIG)

    L.append(-1)
    R.append(-1)

    if n == 1:
        vals[ind2] = val
        return ind2

    mid = n // 2
    if i < mid:
        L[ind2] = setter(L[ind], i, val, mid)
        R[ind2] = R[ind]
    else:
        L[ind2] = L[ind]
        R[ind2] = setter(R[ind], i - mid, val, n - mid)

    vals[ind2] = min(vals[L[ind2]], vals[R[ind2]])
    return ind2


# Find minimum of seg[l:r] for segment tree ind, of size n
def minimum(ind, l, r, n):
    if l == 0 and r == n:
        return vals[ind]

    mid = n // 2
    if r <= mid:
        return minimum(L[ind], l, r, mid)
    elif mid <= l:
        return minimum(R[ind], l - mid, r - mid, n - mid)
    else:
        return min(minimum(L[ind], l, mid, mid), minimum(R[ind], 0, r - mid, n - mid))
