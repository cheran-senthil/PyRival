def ternary_search(f, left, right, absolute_precision):
    """
    Find maximum of unimodal function f() within [left, right]
    """
    while True:
        if abs(right - left) < absolute_precision:
            return (left + right)/2

        left_third = left + (right - left)/3
        right_third = right - (right - left)/3

        if f(left_third) < f(right_third):
            left = left_third
        else:
            right = right_third
