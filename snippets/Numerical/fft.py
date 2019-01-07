import cmath


def fft(a, invert=False):
    n = len(a)
    w = [cmath.rect(1, (-2 if invert else 2) * cmath.pi * i / n) for i in range(n >> 1)]

    rev = [0] * n
    for i in range(n):
        rev[i] = rev[i >> 1] >> 1
        if i & 1:
            rev[i] |= (n >> 1)
        if i < rev[i]:
            a[i], a[rev[i]] = a[rev[i]], a[i]

    length = 2
    while length <= n:
        half, diff = length >> 1, n // length
        for i in range(0, n, length):
            pw = 0
            for j in range(i, i + half):
                v = a[j + half] * w[pw]
                a[j + half] = a[j] - v
                a[j] += v
                pw += diff

        length <<= 1

    if invert:
        for i in range(n):
            a[i] /= n


def conv(a, b):
    s = len(a) + len(b) - 1
    n = 1 << s.bit_length()

    fa = a + [0] * (n - len(a))
    fb = b + [0] * (n - len(b))

    fft(fa)
    fft(fb)

    for i in range(n):
        fa[i] *= fb[i]

    fft(fa, True)

    return [fa[i].real for i in range(s)]
