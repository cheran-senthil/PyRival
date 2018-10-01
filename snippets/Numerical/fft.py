import cmath

def fft(x, roots):
    n = len(x)

    if n <= 1:
        return x

    rs = roots[0::2]
    even = fft(x[0::2], rs)
    odd = fft(x[1::2], rs)

    fft_x = x[:]

    for i in range(n//2):
        t = roots[i] * odd[i]
        fft_x[i] = even[i] + t
        fft_x[i + n//2] = even[i] - t

    return fft_x

def conv(a, b):
    s = len(a) + len(b) - 1
    n = 1 << s.bit_length()

    if s <= 0:
        return []

    roots = [cmath.rect(1, -2 * cmath.pi * i / n) for i in range(n)]

    av = fft(a + [0] * (n - len(a)), roots)
    bv = fft(b + [0] * (n - len(b)), roots)

    roots = [i.conjugate() for i in roots]

    cv = fft([i*j for i, j in zip(av, bv)], roots)

    return [i.real / n for i in cv]
