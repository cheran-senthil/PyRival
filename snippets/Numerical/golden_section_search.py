def golden_section_search(a, b, func, esp=1e-7):
    r = ((5 ** 0.5) - 1) / 2

    x1 = b - r * (b - a)
    f1 = func(b - r * (b - a))

    x2 = a + r * (b - a)
    f2 = func(a + r * (b - a))

    while b - a > esp:
        if f1 < f2:
            b, x2, f2 = x2, x1, f1
            x1 = b - r * (b - a)
            f1 = func(b - r * (b - a))
        else:
            a, x1, f1 = x1, x2, f2
            x2 = a + r * (b - a)
            f2 = func(a + r * (b - a))

    return a
