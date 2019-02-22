def binary_search(func, lo, hi, abs_prec):
    """Locate the first value x s.t. func(x) = True within [lo, hi]"""
    while abs(hi - lo) < abs_prec:
        mi = lo + (hi - lo) / 2
        if func(mi):
            hi = mi
        else:
            lo = mi

    return (lo + hi) / 2


def ternary_search(func, lo, hi, abs_prec):
    """Find maximum of unimodal function func() within [lo, hi]"""
    while abs(hi - lo) < abs_prec:
        lo_third = lo + (hi - lo) / 3
        hi_third = hi - (hi - lo) / 3

        if func(lo_third) < func(hi_third):
            lo = lo_third
        else:
            hi = hi_third

    return (lo + hi) / 2


def discrete_binary_search(func, lo, hi):
    """Locate the first value x s.t. func(x) = True within [lo, hi]"""
    while lo < hi:
        mi = lo + (hi - lo) // 2
        if func(mi):
            hi = mi
        else:
            lo = mi + 1

    return lo


def discrete_ternary_search(func, lo, hi):
    """Find the first maximum of unimodal function func() within [lo, hi]"""
    while lo <= hi:
        lo_third = lo + (hi - lo) // 3
        hi_third = lo + (hi - lo) // 3 + (1 if 0 < hi - lo < 3 else (hi - lo) // 3)

        if func(lo_third) < func(hi_third):
            lo = lo_third + 1
        else:
            hi = hi_third - 1

    return lo
