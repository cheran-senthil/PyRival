def binary_search(a, x):
    """Locate the first value greater than x"""
    lo, hi = 0, len(a) - 1

    while lo < hi:
        mi = (lo + hi) // 2
        if a[mi] > x:
            hi = mi
        else:
            lo = mi + 1

    return lo
