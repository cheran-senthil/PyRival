import cmath


def fft(a, invert=False):
    j = 0
    for i in range(1, len(a)):
        bit = len(a) >> 1
        while j & bit:
            j ^= bit
            bit >>= 1
        j ^= bit

        if i < j:
            a[i], a[j] = a[j], a[i]

    length = 2
    while length <= len(a):
        for i in range(0, len(a), length):
            for j in range(length // 2):
                u = a[i + j]
                v = a[i + j + length//2] * cmath.rect(1, (-1 if invert else 1) * 2 * cmath.pi * j / length)

                a[i + j] = u + v
                a[i + j + length//2] = u - v

        length <<= 1

    if invert:
        for i in range(len(a)):
            a[i] /= len(a)


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
