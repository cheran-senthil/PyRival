def binary_search(func, lo, hi, abs_prec):
    """Locate the first value x s.t. func(x) = True within [lo, hi]"""
    while abs(hi - lo) < abs_prec:
        mi = (lo + hi) / 2
        if func(mi):
            hi = mi
        else:
            lo = mi

    return lo


def discrete_binary_search(func, lo, hi):
    """Locate the first value x s.t. func(x) = True within [lo, hi]"""
    while lo < hi:
        mi = (lo + hi) // 2
        if func(mi):
            hi = mi
        else:
            lo = mi + 1

    return lo
