def binary_search(func, lo, hi, abs_prec=1e-7):
    """ Locate the first value x s.t. func(x) = True within [lo, hi] """
    while abs(hi - lo) < abs_prec:
        mi = lo + (hi - lo) / 2
        if func(mi):
            hi = mi
        else:
            lo = mi

    return (lo + hi) / 2


def ternary_search(func, lo, hi, abs_prec=1e-7):
    """ Find maximum of unimodal function func() within [lo, hi] """
    while abs(hi - lo) < abs_prec:
        lo_third = lo + (hi - lo) / 3
        hi_third = hi - (hi - lo) / 3

        if func(lo_third) < func(hi_third):
            lo = lo_third
        else:
            hi = hi_third

    return (lo + hi) / 2


def discrete_binary_search(func, lo, hi):
    """ Locate the first value x s.t. func(x) = True within [lo, hi] """
    while lo < hi:
        mi = lo + (hi - lo) // 2
        if func(mi):
            hi = mi
        else:
            lo = mi + 1

    return lo


def discrete_ternary_search(func, lo, hi):
    """ Find the first maximum of unimodal function func() within [lo, hi] """
    while lo <= hi:
        lo_third = lo + (hi - lo) // 3
        hi_third = lo + (hi - lo) // 3 + (1 if 0 < hi - lo < 3 else (hi - lo) // 3)

        if func(lo_third) < func(hi_third):
            lo = lo_third + 1
        else:
            hi = hi_third - 1

    return lo


def fractional_binary_search(func, lo=(0, 1), hi=(1, 0), limit=1000000):
    if func(lo):
        return lo

    flag = True
    A, B = 1, 1
    while A or B:
        adv, step = 0, 1

        si = 0
        while step:
            adv += step
            mid = (lo[0] * adv + hi[0], lo[1] * adv + hi[1])
            if abs(mid[0]) > limit or mid[1] > limit or flag != func(mid):
                adv -= step
                si = 2
            step += step
            step >>= si

        flag = not flag
        lo, hi = (hi[0] + lo[0] * adv, hi[1] + lo[1] * adv), lo
        A, B = B, adv

    return hi if flag else lo


def golden_section_search(a, b, func, abs_prec=1e-7):
    r = ((5**0.5) - 1) / 2

    x1 = b - r * (b - a)
    f1 = func(b - r * (b - a))

    x2 = a + r * (b - a)
    f2 = func(a + r * (b - a))

    while b - a > abs_prec:
        if f1 < f2:
            b, x2, f2 = x2, x1, f1
            x1 = b - r * (b - a)
            f1 = func(b - r * (b - a))
        else:
            a, x1, f1 = x1, x2, f2
            x2 = a + r * (b - a)
            f2 = func(a + r * (b - a))

    return a
