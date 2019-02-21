def ternary_search(func, lo, hi, abs_prec):
    """
    Find maximum of unimodal function func() within [lo, hi]
    """
    while True:
        if abs(hi - lo) < abs_prec:
            return (lo + hi) / 2

        lo_third = lo + (hi - lo) / 3
        hi_third = hi - (hi - lo) / 3

        if func(lo_third) < func(hi_third):
            lo = lo_third
        else:
            hi = hi_third


def discrete_ternary_search(func, lo, hi):
    """
    Find the first maximum of unimodal function func() within [lo, hi]
    """
    while lo <= hi:
        lo_third = lo + (hi - lo) // 3
        hi_third = lo + (hi - lo) // 3 + (1 if 0 < hi - lo < 3 else (hi - lo) // 3)

        if func(lo_third) < func(hi_third):
            lo = lo_third + 1
        else:
            hi = hi_third - 1

    return lo
