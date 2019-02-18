def ternary_search(f, left, right, absolute_precision):
    """
    Find maximum of unimodal function f() within [left, right]
    """
    while True:
        if abs(right - left) < absolute_precision:
            return (left + right) / 2

        left_third = left + (right - left) / 3
        right_third = right - (right - left) / 3

        if f(left_third) < f(right_third):
            left = left_third
        else:
            right = right_third


def discrete_ternary_search(a):
    """
    Find the first maximum of unimodal array a
    """
    left, right = 0, len(a) - 1

    while left <= right:
        third = (right - left) // 3
        left_third = left + third
        right_third = max(left + 2 * third, left + third + (1 if left < right else 0))

        if a[left_third] < a[right_third]:
            left = left_third + 1
        else:
            right = right_third - 1

    return left
