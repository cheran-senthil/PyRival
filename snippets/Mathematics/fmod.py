import math

FMOD = 1000000007.0
SHRT = 65536.0

fmod = lambda x: x - FMOD * math.trunc(x / FMOD)

fmul = lambda a, b, c=0: fmod(math.trunc(a / SHRT) * fmod(b * SHRT) + (a - SHRT * math.trunc(a / SHRT)) * b + c)


def fpow(x, y):
    res = 1.0
    while y > 0:
        if y & 1 == 1:
            res = fmul(res, x)
        x = fmul(x, x)
        y >>= 1

    return res
