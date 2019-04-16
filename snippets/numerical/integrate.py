def quad(func, a, b, n=1000):
    h = (b - a) / 2 / n
    v = func(a) + func(b) + sum(func(a + i * h) * (4 if i & 1 else 2) for i in range(1, 2 * n))
    return v * h / 3


def simpson(func, a, b):
    c = (a + b) / 2
    return (func(a) + 4 * func(c) + func(b)) * (b - a) / 6


def rec(func, a, b, eps, S):
    c = (a + b) / 2
    S1, S2 = simpson(func, a, b), simpson(func, c, b)
    if (abs(S1 + S2 - S) <= 15 * eps) or (b - a < 1e-6):
        return S1 + S2 + (S1 + S2 - S) / 15
    return rec(func, a, c, eps / 2, S1) + rec(func, c, b, eps / 2, S2)


def fast_quad(func, a, b, eps=1e-6):
    return rec(func, a, b, eps, simpson(func, a, b))
