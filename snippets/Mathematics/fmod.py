import math

FMOD = 1000000007.0
SHRT = 65536.0

fmod = lambda x: x - FMOD * math.trunc(x / FMOD)

mod_prod = lambda a, b, c=0: fmod(math.trunc(a / SHRT) * fmod(b * SHRT) + (a - SHRT * math.trunc(a / SHRT)) * b + c)
