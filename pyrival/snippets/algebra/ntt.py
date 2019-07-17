MOD = 998244353
MODF = float(MOD)
ROOT = 3.0

MAGIC = 6755399441055744.0
SHRT = 65536.0

MODF_INV = 1.0 / MODF
SHRT_INV = 1.0 / SHRT

fround = lambda x: (x + MAGIC) - MAGIC
fmod = lambda a: a - MODF * fround(MODF_INV * a)
fmul = lambda a, b, c=0.0: fmod(fmod(a * SHRT) * fround(SHRT_INV * b) + a * (b - SHRT * fround(b * SHRT_INV)) + c)


def fpow(x, y):
    if y == 0:
        return 1.0

    res = 1.0
    while y > 1:
        if y & 1 == 1:
            res = fmul(res, x)
        x = fmul(x, x)
        y >>= 1

    return fmul(res, x)


def ntt(a, inv=False):
    n = len(a)
    w = [1.0] * (n >> 1)

    w[1] = fpow(ROOT, (MOD - 1) // n)
    if inv:
        w[1] = fpow(w[1], MOD - 2)

    for i in range(2, (n >> 1)):
        w[i] = fmul(w[i - 1], w[1])

    rev = [0] * n
    for i in range(n):
        rev[i] = rev[i >> 1] >> 1
        if i & 1 == 1:
            rev[i] |= (n >> 1)
        if i < rev[i]:
            a[i], a[rev[i]] = a[rev[i]], a[i]

    step = 2
    while step <= n:
        half, diff = step >> 1, n // step
        for i in range(0, n, step):
            pw = 0
            for j in range(i, i + half):
                v = fmul(w[pw], a[j + half])
                a[j + half] = a[j] - v
                a[j] += v
                pw += diff

        step <<= 1

    if inv:
        inv_n = fpow(n, MOD - 2)
        for i in range(n):
            a[i] = fmul(a[i], inv_n)


def ntt_conv(a, b):
    s = len(a) + len(b) - 1
    n = 1 << s.bit_length()

    a.extend([0.0] * (n - len(a)))
    b.extend([0.0] * (n - len(b)))

    ntt(a)
    ntt(b)

    for i in range(n):
        a[i] = fmul(a[i], b[i])

    ntt(a, True)
    del a[s:]
