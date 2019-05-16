import math


def as_integer_ratio(x, prec=53):
    if x == 0:
        return 0, 1
    a, b = math.frexp(x)
    a = int(a * (1 << prec))
    g = (a & -a).bit_length() - 1
    a >>= g
    b += g - prec
    return (a << b, 1) if b > 0 else (a, 1 << -b)
