MOD = 10**9 + 7
MODF = float(MOD)

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
