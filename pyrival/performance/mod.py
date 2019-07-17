import __pypy__

int_add = __pypy__.intop.int_add
int_sub = __pypy__.intop.int_sub
int_mul = __pypy__.intop.int_mul


def make_mod_mul(mod=10**9 + 7):
    fmod_inv = 1.0 / mod

    def mod_mul(a, b, c=0):
        res = int_sub(int_add(int_mul(a, b), c), int_mul(mod, int(fmod_inv * a * b + fmod_inv * c)))
        if res >= mod:
            return res - mod
        elif res < 0:
            return res + mod
        else:
            return res

    return mod_mul


mod_mul = make_mod_mul()


def mod_pow(x, y):
    if y == 0:
        return 1
    res = 1
    while y > 1:
        if y & 1 == 1:
            res = mod_mul(res, x)
        x = mod_mul(x, x)
        y >>= 1
    return mod_mul(res, x)
