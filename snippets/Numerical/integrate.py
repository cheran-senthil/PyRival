def quad(func, a, b, n=1000):
    h = (b - a) / 2 / n
    v = func(a) + func(b)
    for i in range(1, n * 2):
        v += func(a + i*h) * (4 if i&1 else 2)
    return v * h / 3
