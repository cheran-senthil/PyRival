FMOD = 1000000007.0
SHRT = 65536.0

FMOD_INV = 1.0 / FMOD
SHRT_INV = 1.0 / SHRT

fmod = lambda x: x - FMOD * int(x * FMOD_INV)
fmul = lambda a, b, c=0.0: fmod(fmod(a * SHRT) * int(SHRT_INV * b) + a * (b - SHRT * int(b * SHRT_INV)) + c)


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
