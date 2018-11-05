from math import gcd


lcm = lambda a, b: a * b // gcd(a, b)


mul_inv = lambda a, p: pow(a, p-2, p)


def gcdm(a, *r):
    for b in r:
        a = gcd(a, b)
    return a


def lcmm(a, *r):
    for b in r:
        a = lcm(a, b)
    return a
